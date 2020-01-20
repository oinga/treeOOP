from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Tree(Base):
    __tablename__ = 'tree'

    id = Column(Integer, primary_key=True, autoincrement=True)
    genus = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)


engine = create_engine(
                       'sqlite:///treedb.db',
                       connect_args={'check_same_thread': False}
                       )

Base.metadata.create_all(engine)
