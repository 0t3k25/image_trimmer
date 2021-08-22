# python:3.8の公式 image をベースの image として設定
FROM python:3.8-slim

# 作業ディレクトリの作成
RUN mkdir /app

# 作業ディレクトリの設定
WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY requirements.txt .

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

COPY . .

CMD ["bash"]
