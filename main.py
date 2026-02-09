from fastapi import FastAPI, status

import infra.database as db

app = FastAPI()


@app.post("/", status_code=status.HTTP_204_NO_CONTENT)
def post_root():
    return
