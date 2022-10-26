from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings


class ArtigoModels(settings.DBBaseModel):
    __tablename__ = 'artigos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(256))
    descricao = Column(String(256))
    url_fonte = Column(String(256))
    usuario_id = Column(Integer, ForeignKey('usuarioxcapital.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')


# class CadastroXcapital(settings.DBBaseModel):
#     __tablename__ = 'xcapital'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nome_completo = Column(String(256))
#     data_nacimento = Column(String(50))
#     email = Column(String(256))
#     telefone = Column(Integer)
#     cpf = Column(Integer)
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
#     criador = relationship("UsuarioModel", back_populates='xcapital', lazy='joined')
