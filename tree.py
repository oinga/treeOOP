# import model.treedb_setup as treedb
from treedb_setup import Base, Tree
from sqlalchemy import create_engine
# from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import not_
from sqlalchemy import and_
from sqlalchemy import update

engine = create_engine(
                       'sqlite:///treedb.db',
                       connect_args={'check_same_thread': False}
                       )

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Trees:
    def __init__(self, genus, location):
        self.genus = genus
        self.location = location

    def insert_tree(self):
        newTree = Tree(genus=self.genus, location=self.location)
        session.add(newTree)
        session.commit()


def go():
    try:
        t1 = Trees("Oak", "Piedmont Park")
        t1.insert_tree()
    except():
        print("an error has occurred")


go()
