from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from model_utils import Base


class Mail(Base):

    __tablename__ = 'mails'
    __table_args__ = ({'schema': 'emails'})

    de = Column(String)
    para = Column(String)
    asunto = Column(String)
    cuerpo = Column(String)
    codificacion = Column(String, default='base64')
    enviado = Column(DateTime)
    respuesta = Column(String)
