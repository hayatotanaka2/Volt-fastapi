from typing import List, Optional
from pydantic import BaseModel

#クライアント・サーバー間の送受信情報が既定の方に則っているか判断するための、その判断規則自体の定義
#行動ごとに定義。これにより事前にエラーを吐き、システム全体が止まるのを防ぐ
#すでに検証済みのデータを User や Item のインスタンスに変換する(検証してない奴じゃなく検品済みの信頼できるデータを用いて)
#そのスキーマに含まれているデータを使って User や Item のインスタンスを作成します。つまり、スキーマはデータ検証と格納の役割を果たし、その後にインスタンス作成に使われる。
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
