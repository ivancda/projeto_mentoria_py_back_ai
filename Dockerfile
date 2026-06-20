# De qual imagem base esse container vai partir.
# É como escolher o sistema operacional + runtime já instalado.
# python:3.12-slim = Python 3.12 numa versão enxuta do Linux
FROM python:3.12-slim

# Define qual pasta dentro do container será o diretório de trabalho.
# Todos os comandos seguintes rodam a partir daqui.
# Se a pasta não existir, ele cria.
WORKDIR /app

# Copia arquivos da sua máquina para dentro do container.
# COPY <origem na sua máquina> <destino no container>
# Copiamos o requirements primeiro (sozinho) para aproveitar o cache do Docker
COPY requirements.txt .

# Executa um comando shell durante a construção da imagem.
# Aqui instala as dependências. --no-cache-dir evita guardar cache desnecessário.
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código pro container
COPY . .

# Define o comando que roda quando o container iniciar.
# Equivalente a rodar: uvicorn app.main:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]