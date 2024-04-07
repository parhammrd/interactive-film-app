# Interactive Film API

## Prerequisites

Before running, ensure that you have the following:

- Python dependencies installed by running the following command:
  ```shell
  pip install -r requirements.txt
  ```

## Running uvicorn:

- implement host:port

```shell
uvicorn main:app --port=8000 --host=0.0.0.0
```

- reload flag

```shell
uvicorn main:app --reload
```

## Adding pre-commit hooks:

```shell
pre-commit install
```