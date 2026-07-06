# Importa ferramentas de mock da biblioteca padrão do Python (não precisa instalar)
# MagicMock: cria objetos falsos que aceitam qualquer chamada
# patch: substitui temporariamente um objeto real por um falso durante o teste
from unittest.mock import MagicMock, patch

# Importa as funções que queremos testar
from app.services.review_service import review_code, get_all_reviews

# Importa o schema pra conseguir criar um ReviewRequest de mentira
from app.schemas.review import ReviewRequest, ReviewResponse

# Importa o model pra conseguir criar um Review de mentira como retorno esperado
from app.models.review import Review


def test_review_code_retorna_review_salva():
    # --- ARRANGE: prepara tudo que o teste precisa ---

    # Cria um banco de dados falso. O service recebe um `db` mas não vamos usar o banco real.
    # MagicMock() aceita qualquer chamada sem reclamar (db.add(), db.commit(), etc.)
    mock_db = MagicMock()

    # Cria um objeto Review falso que simula o que o banco retornaria após salvar
    fake_review = Review(id=1, code="print('hello')", result="review realizada para o código: print('hello')")

    # AQUI VEM A PARTE IMPORTANTE DO MOCKING!!!
    # patch() intercepta o ReviewRepository DENTRO do review_service.py e substitui por um falso.
    # O caminho é exatamente onde ele é USADO, não onde é definido.
    # MockRepo é o objeto falso que representa a classe ReviewRepository
    with patch("app.services.review_service.ReviewRepository") as MockRepo:

        # Quando o código chamar repository.create(...), retorna o fake_review em vez de ir ao banco
        MockRepo.return_value.create.return_value = fake_review

        # Cria o request de entrada que seria enviado pela API
        request = ReviewRequest(code="print('hello')")

        # --- ACT: executa a função que está sendo testada ---
        result = review_code(request, mock_db)

        # --- ASSERT: verifica se o resultado foi o esperado ---

        # Verifica se o service retornou um ReviewResponse com os valores corretos
        assert isinstance(result, ReviewResponse)
        assert result.status == "success"
        assert result.review == "review realizada para o código: print('hello')"

        # Verifica se o repository.create() foi chamado exatamente 1 vez, com esses argumentos.
        # Isso garante que o service montou o `result` corretamente antes de salvar.
        MockRepo.return_value.create.assert_called_once_with(
            code="print('hello')",
            result="review realizada para o código: print('hello')"
        )


def test_get_all_reviews_retorna_lista():
    # --- ARRANGE ---

    mock_db = MagicMock()

    # Cria uma lista com dois Reviews falsos simulando o que o banco retornaria
    fake_reviews = [
        Review(id=1, code="x = 1", result="review 1"),
        Review(id=2, code="x = 2", result="review 2"),
    ]

    with patch("app.services.review_service.ReviewRepository") as MockRepo:

        # Quando o código chamar repository.get_all(), retorna a lista falsa
        MockRepo.return_value.get_all.return_value = fake_reviews

        # --- ACT ---
        result = get_all_reviews(mock_db)

        # --- ASSERT ---

        # Verifica se o retorno é exatamente a lista que configuramos
        assert result == fake_reviews

        # Verifica se a lista tem 2 itens (checa o tamanho)
        assert len(result) == 2