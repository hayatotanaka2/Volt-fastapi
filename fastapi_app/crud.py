from sqlalchemy.orm import Session
#import models
#import schemas
from . import models
from . import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    #dbがセッションのインスタンスであることを考えると、この文脈においてセッションは、
    # 新規の登録情報や変更情報を一度にコミットする前に変更、登録情報を
    # 一時的にため込んでおく箱(ただし本当のDBと管のようなものでつながっている（これがセッションによるつながり）コミットがDBへの発射ボタン
    # （そもそもセッションは基本は始まりから終わりまでを示す一単位で今回はそのオブジェクト）)のようにもとらえられる。
    #そしてそこにため込んでおいた情報をコミットで一気に提出し保存する。
    #しかし、箱の提出後に自動的に変更が起こってしまうようなID情報やタイムスタンプなどの情報がある場合は
    #基本そうゆうのは自動更新だから更新された時点で変更はされてる。
    # しかしすぐ反映できるのはコミットしたやつのみだからフレッシュでリロードしてすべてを反映させる
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
