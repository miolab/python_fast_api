# FastAPI framework usage

テーマ：非同期処理を前提としたAPIを、PythonのWebフレームワーク [__FastAPI__](https://github.com/tiangolo/fastapi) で実装します。


## 開発メモ

- install

    ```
    pip install fastapi uvicorn
    ```

- 実装（ソースコード）

    `main.py`

- サーバー起動

    ```
    uvicorn main:app --reload
    ```
    - `reload`: 開発時ライブリロード有効にするオプション

    [http://127.0.0.1:8000](http://127.0.0.1:8000)

    ![fastapi1](https://user-images.githubusercontent.com/33124627/75401005-3597a400-5944-11ea-8767-510e1ec04d54.png)

- API仕様書（Swagger UI）

    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)で確認可。

    ![fastapi1docs](https://user-images.githubusercontent.com/33124627/75412158-f6c61600-5964-11ea-9f78-011d78ae8958.png)

