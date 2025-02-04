# Dev Memo

## fastapi dev main.py と uvicorn main:app の違い

### fastapi dev main.py

これは **FastAPI の公式 CLI コマンド** を使用して開発サーバーを起動する方法です。  
`fastapi` CLI（FastAPI の公式ツール）には、`dev` というコマンドがあり、開発環境向けに `uvicorn` をラップして提供します。

特徴:

- `--reload`（ホットリロード）がデフォルトで有効
- 設定の管理が簡単（`.env` ファイルを自動で読み込む）
- `pyproject.toml` に設定を記述できる
- 簡単なコマンドで実行可能

使い方:

```sh
fastapi dev main.py
```

### uvicorn main:app

これは **Uvicorn（ASGI サーバー）を直接使う方法** です。  
`uvicorn` は FastAPI アプリケーションを ASGI サーバーとして実行するために使われます。

特徴:

- `--reload` をつけない限りホットリロードなし（デフォルトはプロダクション向け）
- より細かいオプション指定が可能（例: `--host` や `--port`）
- `gunicorn` との組み合わせで運用可能（`gunicorn -k uvicorn.workers.UvicornWorker`）

使い方:

```sh
uvicorn main:app --reload
```

## どちらを使うべきか

| コマンド | 主な用途 | 特徴 |
|----------|--------|------|
| `fastapi dev main.py` | 開発用 | 簡単、FastAPI 公式ツール、設定を `.env` や `pyproject.toml` から読み込める |
| `uvicorn main:app --reload` | 開発用 | 公式 CLI なしでも利用可能、オプションを細かく設定可能 |
| `uvicorn main:app` | 本番環境 | 高速、安定した ASGI サーバーとして動作 |

開発では `fastapi dev` を使うと便利ですが、プロダクション環境では `uvicorn main:app` を使うのが一般的です。
