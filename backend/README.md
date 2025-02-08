# Backend - TaskBoard API 📝

このディレクトリは TaskBoard のバックエンド部分で、FastAPI を使用した API を構築する。

## 📌 環境構築

### 1️⃣ 仮想環境のセットアップ

```sh
cd backend
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

### 2️⃣ 必要なパッケージのインストール

```sh
pip install fastapi uvicorn python-dotenv python-multipart
```

### 3️⃣ `requirements.txt` の作成・更新

必要なパッケージをインストールしたら、`requirements.txt`に依存関係を追加する

```sh
pip freeze > requirements.txt
```

以降、追加で`pip install`で追加する度に上記コマンド実行で更新する。

`requirements.txt`をもとにパッケージをインストールする場合は`pip install -r requirements.txt`をする。

### 4️⃣ `.env` ファイルの作成

`.env` ファイルを作成し、環境変数を設定する。

```plaintext
APP_NAME=TaskBoard
DEBUG=True
```

## 🚀 FastAPI の起動

```sh
uvicorn main:app --reload
```

📌 **アクセス可能な URL**

- API のルート: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📂 ディレクトリ構成

```bash
backend/
├── .env                  # 環境変数設定
├── .gitignore            # Git 管理対象外ファイル指定
├── .venv/                # 仮想環境（Git管理対象外）
├── main.py               # FastAPI エントリーポイント
├── requirements.txt      # 必要なパッケージ一覧
└── README.md
```

## ✅ 動作確認

API の動作確認を行うため、以下のエンドポイントをテストする。

### ルートエンドポイント

```sh
curl http://127.0.0.1:8000/
```

📌 **レスポンス**

```json
{"message": "Welcome to TaskBoard API"}
```

### ヘルスチェック

```sh
curl http://127.0.0.1:8000/health
```

📌 **レスポンス**

```json
{"status": "OK"}
```

## 認証

手順:

1. JWT 認証の実装（ユーザーログイン・トークン発行）
2. データベース（SQLite）のセットアップ
3. API のルーティング構成の整理

必要なライブラリをインストール。

```bash
# インストール
pip install 'passlib[bcrypt]' 'python-jose[cryptography]' python-multipart SQLAlchemy
# 依存関係更新
pip freeze > requirements.txt
```

- `passlib[bcrypt]` → パスワードのハッシュ化（bcrypt）
- `python-jose[cryptography]` → JWT のエンコード/デコード
- `python-multipart` → フォームデータ（ログイン時のリクエストなど）を処理

### 疎通確認

```bash
curl -X 'POST' 'http://127.0.0.1:8000/register/' \
     -H 'Content-Type: application/json' \
     -d '{
           "username": "testuser",
           "email": "testuser@example.com",
           "password": "password123"
         }'
```

### PostgreSQL設定

`docker-compose.yml`を設定したら、次のコマンドで起動。

```bash
docker compose up -d
```

#### Docker 内の PostgreSQL にアクセス

以下のコマンドで、PostgreSQLに接続できる。

```bash
docker compose exec db psql -U admin -d taskboard
```

### 💡Tips: FastAPI から Docker 内の PostgreSQL へ接続

この環境では、**ホスト側（Docker 外）にインストールされた FastAPI から Docker 内の PostgreSQL に接続** するため、アドレスの指定に注意が必要。

FastAPI の `.env` では、**`127.0.0.1` を指定する**。

```env
DATABASE_URL=postgresql://<username>:<password>@127.0.0.1:5432/taskboard
```

## 🔜 次のステップ

SQLite -> PostgreSQLに
