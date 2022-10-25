from email.policy import default
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(256), nullable=True)
    data_nascimento = Column(String(256), nullable=True)
    telefone = Column(Integer, nullable=True)
    cpf = Column(Integer, nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship(
        "ArtigoModels",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    # Se  o usuario tiver uma lista de artigos, vamos remover todos
