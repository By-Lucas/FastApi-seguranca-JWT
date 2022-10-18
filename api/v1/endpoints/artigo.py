from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy import delete

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.artigo_model import ArtigoModels
from models.usuario_model import UsuarioModel
from schemas.artigo_schema import ArtigoSchema
from core.deps import get_session, get_current_user


router = APIRouter()


# POST artigo
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ArtigoSchema)
async def post_artigo(artigo: ArtigoSchema, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    novo_artigo: ArtigoModels = ArtigoModels(titulo = artigo.titulo, 
                                            descricao = artigo.descricao, 
                                            url_font=artigo.url_fonte, 
                                            usuario_id=usuario_logado.id)
    
    db.add(novo_artigo)
    await db.commit()

    return novo_artigo

# GET artigos
@router.get('/', response_model=List[ArtigoSchema])
async def get_artigos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModels)
        result = await session.execute(query)
        artigos: List[ArtigoModels] = result.scalars().unique().all()

        return artigos


# GET artigo
@router.get('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_200_OK)
async def get_artigo(artigo_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModels).filter(ArtigoModels.id == artigo_id)
        result = await session.execute(query)
        artigo: ArtigoModels = result.scalars().unique().one_or_none()
        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Artigo não encontrado', status_code=status.HTTP_404_NOT_FOUND)


# PUT artigo
@router.put('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_artigo(artigo_id:int, artigo: ArtigoSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        # Aqui qualquer usuario faz o update
        # Para somente usuario criador puder atualizar adicione o -> .filter(ArtigoModels.usuario_id == usuario_logado.id)
        query = select(ArtigoModels).filter(ArtigoModels.id == artigo_id)
        result = await session.execute(query)
        artigo_update: ArtigoModels = result.scalars().unique().one_or_none()
        
        if artigo_update:
            if artigo.titulo:
                artigo_update.titulo = artigo.titulo
            if artigo.descricao:
                artigo_update.descricao = artigo.descricao
            if artigo.url_fonte:
                artigo_update.url_fonte = artigo.url_fonte
            if usuario_logado.id != artigo_update.usuario_id:
                artigo_update.usuario_id = usuario_logado.id

            await session.commit()

            return artigo_update
        else:
            raise HTTPException(detail='Artigo não encontrado', status_code=status.HTTP_404_NOT_FOUND)


# DELETE artigo
@router.delete('/{artigo_id}', response_model=ArtigoSchema)
async def delete_artigo(artigo_id:int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        # Somente o usuario criador e logado pode remover seu artigo
        # .filter(ArtigoModels.usuario_id == usuario_logado.id)
        query = select(ArtigoModels).filter(ArtigoModels.id == artigo_id).filter(ArtigoModels.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        artigo_delete: ArtigoModels = result.scalars().unique().one_or_none()
        
        if artigo_delete:
            await session.delete(artigo_delete)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Artigo não encontrado', status_code=status.HTTP_404_NOT_FOUND)