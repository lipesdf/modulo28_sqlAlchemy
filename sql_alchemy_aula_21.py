from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria o bando e inicia a sessão
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# As tabelas

class Usuario(Base):
    
    __tablename__ = "usuarios"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo



class Livro(Base):

    __tablename__ = "livros"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column('dono', ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

## CRUD

''' 
# Cria usuario
usuario = Usuario(nome="Felipe", email="email@gmail.com", senha="123123")
session.add(usuario)
session.commit()
'''

'''
## Read
#lista_usuarios = session.query(Usuario).all()
usuario = session.query(Usuario).filter_by(nome='Felipe').first()
print(usuario)
print(usuario.nome)


# Cria Livro
livro = Livro(titulo="Novo Livro",qtde_paginas=1000,dono=usuario.id)
session.add(livro)
session.commit()
'''

'''
## Update
usuario = session.query(Usuario).filter_by(nome='Felipe').first()
print(usuario)
print(usuario.nome)
usuario.nome = 'Felipe Sergio'
session.add(usuario)
session.commit()
'''

'''
## Delete
usuario = session.query(Usuario).filter_by(nome='Felipe').first()
session.delete(usuario)
session.commit()
'''
