from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

"""
Vai ser criado alguns Schemas devido ao retorno das informações,
se for pra retornar as informações do usuario cadastrado, a senha não deve ser retornada
podeque é algo especifico e seguro do usuario.
"""

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome_completo: str
    data_nascimento: str
    telefone: str
    cpf: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    """Caso seja chamado um usuario, vai ser chamado pelo artigo, para
    que seja mostrado os artigos apropriado pelo mesmo"""
    artigos: Optional[List[ArtigoSchema]]


class UsuarioSchemaUpdate(UsuarioSchemaBase):
    """As informações de editar cadastro são Opcionais devido o,
    usuario querer editar apenas uma informação apenas."""
    nome_completo: Optional[str]
    data_nascimento: Optional[str]
    telefone: Optional[int]
    cpf: Optional[int]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]

