# FastAPI framework Usage

### 概要

- 非同期処理を前提としたAPIを、PythonのWebフレームワーク [__FastAPI__](https://github.com/tiangolo/fastapi) で実装します。

- 公式リファレンス
  - [Docs](https://fastapi.tiangolo.com/)
  - [GitHub](https://github.com/tiangolo/fastapi)

- 環境 / ツール
    | | バージョン | 備考 |
    |:--|:--|:--|
    | Python | 3.7 | |
    | pipenv | | |
    | Insomnia | | REST Client |

---

## 開発メモ

### 準備（インストール）

```
$ pip install fastapi uvicorn
```

#### 実装（ソースコード）

- [`main.py`](https://github.com/miolab/python_fast_api/blob/master/main.py)


### サーバー起動（localhost）

```
$ uvicorn main:app --reload
```
- `--reload`: 開発時ライブリロード有効にするオプション

### REST Clientで結果確認

#### 通常バージョン

- [http://127.0.0.1:8000](http://127.0.0.1:8000)

  <img width="640" alt="fast1" src="https://user-images.githubusercontent.com/33124627/77629099-53c8e200-6f8c-11ea-97f1-a427cde26043.png">

- __API仕様書（Swagger UI）__ を、[http://127.0.0.1:8000/__docs__](http://127.0.0.1:8000/docs)で確認可能。

  <img width="640" alt="fast1" src="https://user-images.githubusercontent.com/33124627/75412158-f6c61600-5964-11ea-9f78-011d78ae8958.png">

---

#### API用ディレクトリを指定したバージョン（`lang/`ディレクトリ作成）

- [http://127.0.0.1:8000/lang](http://127.0.0.1:8000/lang)

  <img width="640" alt="fast2" src="https://user-images.githubusercontent.com/33124627/77629645-35afb180-6f8d-11ea-8db4-be4bad531a29.png">

---

#### GETリクエスト想定パターン

- [http://127.0.0.1:8000/items/3?query=some_query](http://127.0.0.1:8000/items/3?query=some_query)

  <img width="640" alt="fast3" src="https://user-images.githubusercontent.com/33124627/77642503-1b7fce80-6fa1-11ea-8c05-44e21c46e9ab.png">


