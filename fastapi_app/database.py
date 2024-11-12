# database.pyはデータベース事態の基本作成骨格を定義
# かつdatabaseとのそもそもの接続をする
# かつdatabaseを作成する

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLiteデータベースを fastapi_app.db ファイルとして作成
#構文: sqlite:///./ファイル名.db は、カレントディレクトリにデータベースファイルを作成する形式
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_app.db"

#create_engine は、指定されたデータベースへの接続を管理するエンジンを作成
#connect_args={"check_same_thread": False}: SQLiteでは通常、1つのスレッドでしか接続できないため、マルチスレッドでの接続を許可するために check_same_thread を False
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


#sessionmaker を使って、データベースとのセッションを作成するクラスを生成
#データベースに対してクエリを実行するためのセッションを作成するために使う
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#declarative_base は、SQLAlchemyのデータベースモデル（テーブルの定義）を作成するための基本クラスを提供
# データベースのテーブルをクラスで定義するためのベースクラスを作成
Base = declarative_base()
