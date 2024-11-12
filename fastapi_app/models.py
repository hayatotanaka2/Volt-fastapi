from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
#from database import Base
from fastapi_app.database import Base  # database.pyで定義したBaseを直接インポート



#DBの形式を模したDBもどきインスタンスをPythonのクラスで簡単に作れるdatabaseクラス(本来はPython上ではDBは作れない。SQLを直接編集が必要)をインポートし、その設定をしたうえで
#Pythonのクラスで作ったDBもどきインスタンス+SQLAlchemyというORM（もどきPythonクラスと実際のDBを対応付ける）(DBの上で動作)でPython完結でDBの編集まで行える
class User(Base):
    #__tablename__ は、SQLAlchemyモデルで使用される特殊な文法であり、Pythonのクラスをデータベースのテーブルに関連付けるために使用
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #ここでSQLAlchemyのrelationship内で指定するから__tablename__で定義しておく必要がある
    items = relationship("Item", back_populates="owner")


class Item(Base):
    #__tablename__ は、SQLAlchemyモデルで使用される特殊な文法であり、Pythonのクラスをデータベースのテーブルに関連付けるために使用
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    #ここでSQLAlchemyのrelationship内で指定するから__tablename__で定義しておく必要がある
    owner = relationship("User", back_populates="items")
