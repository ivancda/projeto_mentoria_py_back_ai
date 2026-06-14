# cria a "engine", que é o objeto central de conexão do SQLAlchemy com o banco
from sqlalchemy import create_engine

# cria a classe Base, que será usada pelos models/tabelas
from sqlalchemy.ext.declarative import declarative_base

# cria uma fábrica de sessões para conversar com o banco
from sqlalchemy.orm import sessionmaker

# nossas settingssssss
from app.core.config import settings

# URL do banco.
# SQLite usando um arquivo local chamado reviews.db
DATABASE_URL = settings.DATABASE_URL

# cria a engine, ou seja, o "motor" de comunicação com o banco.
# connect_args={"check_same_thread": False} para permitir uso com FastAPI em múltiplas threads (particularidade do SQLite). 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# cria a fábrica de sessões.
# autocommit=False → você decide quando salvar de verdade com commit()
# autoflush=False → evita sincronização automática antes da hora
# bind=engine → essa sessão usa a engine criada acima
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base é a classe-mãe dos models.
# Todo model/tabela vai herdar dela.
Base = declarative_base()

# metodo get_db para criar uma sessão de banco de dados e garantir que ela seja fechada depois do uso
def get_db():
    db = SessionLocal()
    try:
        # yield é usado para criar um gerenciador de contexto, permitindo que o código que chama get_db() use a sessão 
        # e depois garanta que ela seja fechada.
        yield db
    finally:
        db.close()

