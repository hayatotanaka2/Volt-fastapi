# Pythonのベースイメージを指定
FROM python:3.9

# 作業ディレクトリの設定（スペースを含めない）
WORKDIR /fastapi_app_docker

# requirements.txtをコンテナにコピー
COPY ./requirements.txt /fastapi_app_docker/requirements.txt

# パッケージをインストール
RUN pip install --no-cache-dir --upgrade -r /fastapi_app_docker/requirements.txt

# アプリケーションコードをコピー
COPY ./fastapi_app /fastapi_app_docker/fastapi_app

# Uvicornサーバーの実行コマンド（fastapi_appディレクトリとmain.pyを指すように）
CMD ["uvicorn", "fastapi_app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
