import sys

import cv2
import face_recognition as fa_re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import BYTEA, ARRAY, CIDR

from sqlalchemy.orm import declarative_base
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    cam_id: int
    cam_pos: bool
    cam_ip: str
    door_controller: str


settings = Settings(
    _env_file='.env',
)


engine = create_engine(
    settings.db_url, pool_size=10, max_overflow=20
)

Session = sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
    )
session = Session()

Base = declarative_base()
class facesDB(Base):
    __tablename__ = "faces"

    id = Column(Integer, primary_key=True)
    file = Column(BYTEA)
    face_data = Column(BYTEA)
    personal_id = Column(Integer)


img2=cv2.imread("images\\me4.png")
face_encoding2 = fa_re.face_encodings(img2)[0]

#add new face
face_add = facesDB(
    face_data = face_encoding2,
    file =  cv2.imencode('.png', img2)[1].tobytes(),
    personal_id = 1
)

session.add(face_add)
session.commit()

sys.exit()