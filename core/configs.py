from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:123@localhost:5432/faculdade2"
    DBBaseModel = declarative_base()


    # JWT_SECRET :A VARIAVEL TEM QUE SER MAIUSCULO
    JWT_SECRET: str = 'HAu9lffR49esOAzMBRJYTLXjN-6igsPZ62iZTvav8Y0'
    """
    Se desejar criar um token aleatorio, segui comandos abaixo no python, copiar
    e colar o token acima na variavel: JWT_SECRET
    import secrets
    token: str = secrets.token_urlsafe(32)
    token
    """

    ALGORITHM: str = 'HS256'
    ''' Tempo em minutos para expiração do token
         60 minutos * 27 horas * 7 dias => 1 semana'''
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()