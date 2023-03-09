import os

from pathlib import Path
from dotenv import load_dotenv


load_dotenv(os.path.join(Path(__file__).resolve().parent.parent.parent, ".env"))


class BaseConfig(object):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    SECRET_KEY = "flaskBooks"

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/books_db"

class ProductionConfig(BaseConfig):
    DEBUG=False

