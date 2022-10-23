import os
from sqlmodel import create_engine

from dotenv import load_dotenv

load_dotenv()

database_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
    os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'),
    os.getenv('DB_NAME')
)

engine = create_engine(database_url)