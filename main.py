from fastapi import FastAPI, Response


app = FastAPI()


@app.get('/')
def root():
    return Response('<h1>Interactive film API.</h1>')
