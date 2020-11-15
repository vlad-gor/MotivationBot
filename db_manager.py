import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import Aphorism

class DB_manager():

    def __init__(self):
        self.engine = sa.create_engine(f'sqlite:///motivation.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self, Model):
        '''Создает таблицу на основе модели'''
        if not self.exist(Model):
            Model.__table__.create(self.engine)
        else:
            print('Таблица уже существует')

    def drop_table(self, Model):
        '''Удаляет таблицу соответствующую модели'''
        if self.exist(Model):
            Model.__table__.drop(self.engine)
        else:
            print("Таблица не существует")

    def clear_table(self, Model):
        '''Удаляет все записи из таблицы'''
        if self.exist(Model):
            self.session.query(Model).delete()
            self.session.commit()
        else:
            print("Таблица не существует")

    def check_table(self, Model):
        if self.exist(Model):
            res = self.session.query(Model).all()
            print(f"В таблице {len(res)} значений")
        else:
            print("Таблица не существует")

    def exist(self, Model):
        return Model.__table__.exists(self.engine)

    def add_record(self, Model, params):
        if self.exist(Model):
            b1 = Model(params)
            self.session.add(b1)
            return b1
        else:
            print("Таблица не существует")
            return None

    def get_records(self, Model):
        return self.session.query(Model).all()



