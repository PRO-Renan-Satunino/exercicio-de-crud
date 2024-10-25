from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parametros para conexao com o banco de dados MySQL.
#Não esqueça do "docker-compose up"
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# URL da conexao para o db MySQL.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao bando de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as erro:
        db.rollback()
        raise erro
    finally:
        db.close()