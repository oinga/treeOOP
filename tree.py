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

    def read_tree(self):
        r = select(
                   [Tree]
                   ).where(
                           Tree.location == self.location
                           )
        rs = session.execute(r)
        tree = rs.fetchall()
        return tree


def go():
    try:
        t1 = Trees("Fairy Tree", "Junk Station")
        Trees.insert_tree(t1)
        location = t1.location
        find_tree = Trees.read_tree(location)
        print(find_tree)
    except():
        print("an error has occurred")


go()
