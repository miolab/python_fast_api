# FastAPI framework Sandbox

Python の Web フレームワーク [**FastAPI**](https://github.com/tiangolo/fastapi) での API 実装メモ

https://fastapi.tiangolo.com

|        | バージョン | 備考           |
| :----- | :--------- | :------------- |
| Python | 3.10       |                |
| Poetry |            |                |
| Docker |            | docker compose |

---

## Dev Note

### Preparation

```
docker compose build
```

```
docker compose run --entrypoint "poetry init \
  --name sample_app \
  --dependency fastapi \
  --dependency uvicorn[standard]" \
  sample-app
```

```
docker compose run --entrypoint "poetry install" sample-app
```

### Execution

Start local API server;

```
docker compose up
```

- `--reload`: 開発時ライブリロード有効にするオプション

### Result

#### 通常バージョン

- [http://127.0.0.1:8000](http://127.0.0.1:8000)

  <img width="640" alt="fast1" src="https://user-images.githubusercontent.com/33124627/77629099-53c8e200-6f8c-11ea-97f1-a427cde26043.png">

- **API 仕様書（Swagger UI）** を、[http://127.0.0.1:8000/**docs**](http://127.0.0.1:8000/docs)で確認可能。

  <img width="640" alt="fast1" src="https://user-images.githubusercontent.com/33124627/75412158-f6c61600-5964-11ea-9f78-011d78ae8958.png">

---

#### API 用ディレクトリを指定したバージョン（`lang/`ディレクトリ作成）

- [http://127.0.0.1:8000/lang](http://127.0.0.1:8000/lang)

  <img width="640" alt="fast2" src="https://user-images.githubusercontent.com/33124627/77629645-35afb180-6f8d-11ea-8db4-be4bad531a29.png">

---

#### GET リクエスト想定パターン

- [http://127.0.0.1:8000/items/3?query=some_query](http://127.0.0.1:8000/items/3?query=some_query)

  <img width="640" alt="fast3" src="https://user-images.githubusercontent.com/33124627/77642503-1b7fce80-6fa1-11ea-8c05-44e21c46e9ab.png">
