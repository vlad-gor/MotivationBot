import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aphorism(Base):
    __tablename__ = 'aphorisms'
    id = sa.Column(sa.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    text = sa.Column('text', sa.Text)
    author = sa.Column('author', sa.Text)

    def __init__(self, params):
        self.text = params['text'].strip()
        self.author = params['author'].strip()

    def __repr__(self):
        return f"{self.id}. {self.text} \n( {self.author} )"
