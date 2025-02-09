# TaskBoard 📝

このリポジトリは、Python（FastAPI）+ React を使用してプロジェクト管理アプリを開発するための練習用リポジトリ。📚
以下の要件に沿ってアプリを構築し、FastAPI と React の基本的な使い方を学習する。

## 1. 📌 概要

本アプリは、複数のプロジェクトを管理できるシステムであり、ユーザーごとに異なる権限を設定し、適切な操作を制御する。マスター（master）、管理者（admin）、一般ユーザー（guest）という 3 つの権限レベルを持つ。

## 2. 🛠 技術要素

- **バックエンド:** Python（FastAPI）
  - 認証: JWT（OAuth2）
  - データベース: PostgreSQL
  - WebSocket（リアルタイム更新が必要になったら）
  - API ドキュメント: OpenAPI（Swagger UI）
- **フロントエンド:** React（React Router v7）
  - UI ライブラリ: TailwindCSS / Material-UI
- **デプロイ:**（仮）
  - フロントエンド: Vercel / Netlify
  - バックエンド: Railway / Fly.io
  - データベース: Supabase / Firebase（代替案）

## 3. 🚀 機能

### 3.1 🔐 ユーザー認証・管理

- ユーザー登録（メール・パスワード認証）
- ログイン / ログアウト（JWT）
- ユーザープロフィール編集
- 権限管理（master / admin / guest）
  - Master: 全権限
  - Admin: プロジェクト作成・編集・タスク管理可
  - Guest: 閲覧のみ

### 3.2 📂 プロジェクト管理

- プロジェクト作成・編集・削除（admin 以上）
- プロジェクト一覧・詳細表示
- プロジェクトごとのメンバー管理（master が管理）
- プロジェクトに関連するタスク管理

### 3.3 ✅ タスク管理

- タスク作成・編集・削除（admin 以上）
- タスクのステータス管理（ToDo / 進行中 / 完了）
- タスクの担当者設定
- 締め切り設定
- コメント機能（メンバーのみ）

### 3.4 🔔 通知機能

- タスクの締切リマインド
- コメント通知
- メンション機能（@ユーザー）

### 3.5 📊 ダッシュボード

- ユーザーごとのプロジェクト・タスクの一覧
- 進捗状況の可視化
- 最近の活動履歴

### 3.6 🔒 アクセス制御

- Master がユーザーの権限を設定
- 各ユーザーの操作制限を適用
- Guest はプロジェクトの閲覧のみ可

## 4. 🔗 API エンドポイント例（FastAPI）

| メソッド | エンドポイント | 説明 | 認証 |
|----------|---------------|------|------|
| POST | /auth/register | ユーザー登録 | なし |
| POST | /auth/login | ログイン | なし |
| GET | /projects | プロジェクト一覧取得 | 必要 |
| POST | /projects | プロジェクト作成 | 必要（Admin 以上） |
| PUT | /projects/{id} | プロジェクト更新 | 必要（Admin 以上） |
| DELETE | /projects/{id} | プロジェクト削除 | 必要（Master） |
| GET | /tasks | タスク一覧取得 | 必要 |
| POST | /tasks | タスク作成 | 必要（Admin 以上） |
| PUT | /tasks/{id} | タスク更新 | 必要（Admin 以上） |
| DELETE | /tasks/{id} | タスク削除 | 必要（Admin 以上） |

## 5. 🗄 データベース設計（概要）

### 5.1 👤 ユーザーテーブル
| カラム | 型 | 説明 |
|--------|------|------|
| id | UUID | ユーザーID |
| name | String | ユーザー名 |
| email | String | メールアドレス |
| password_hash | String | ハッシュ化されたパスワード |
| role | Enum | master / admin / guest |

### 5.2 📁 プロジェクトテーブル

| カラム | 型 | 説明 |
|--------|------|------|
| id | UUID | プロジェクトID |
| name | String | プロジェクト名 |
| description | Text | 説明 |
| owner_id | UUID | 作成者（マスター） |

### 5.3 📝 タスクテーブル

| カラム | 型 | 説明 |
|--------|------|------|
| id | UUID | タスクID |
| project_id | UUID | どのプロジェクトに属するか |
| name | String | タスク名 |
| status | Enum | ToDo / 進行中 / 完了 |
| assigned_to | UUID | 担当者 |
| due_date | DateTime | 締切日 |

## 6. 🔮 将来的な拡張（オプション）

- 外部カレンダー連携（Google Calendar）
- ファイル添付機能
- ガントチャートによる進捗管理
- モバイル対応（PWA）

## 7. コミットガイドライン

```bash
# ==== Emoji Prefix ====
# :hatching_chick: 🐣 初回コミット
# :tada:           🎉 大規模な新機能追加
# :sparkles:       ✨ 新機能の追加・拡張（部分的な機能追加）
# :+1:             👍 既存機能の改善
# :art:            🎨 UI/UX の更新やデザイン調整
# :ambulance:      🚑 バグ修正
# :memo:           📝 ドキュメントの追加・修正
# :shirt:          👕 コードスタイルの修正や Lint 対応
# :recycle:        ♻️  リファクタリング（機能変更なし）
# :rocket:         🚀 パフォーマンス最適化
# :green_heart:    💚 テストや CI の更新
# :up:             🆙 依存パッケージやライブラリの更新
# :wrench:         🔧 設定ファイルや環境構成の変更
# :construction:   🚧 作業中（WIP）
```

## 8. 💼 まとめ

本仕様に基づき、FastAPI を用いたバックエンドと React を用いたフロントエンドを開発し、ロールベースのアクセス管理を導入したプロジェクト管理アプリを実装する。

