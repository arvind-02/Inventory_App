from database import engine, Base
from sqlalchemy.engine import Connection
from sqlalchemy import text
from models import Base

def create_tables(connection: Connection):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    sql_emb = text("ALTER TABLE products ADD COLUMN description_embedding VECTOR(1536)")
    connection.execute(sql_emb)
    connection.commit()
    
if __name__ == "__main__":
    with engine.connect() as connection:
        create_tables(connection)

    print("Tables created successfully.")