import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv("db.env")

def execute(query, *params, fetch=False):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params if params else None)

            if fetch:
                result = cur.fetchall()
            else:
                result = None

            if not query.strip().lower().startswith("select"):
                conn.commit()

            return result

    finally:
        conn.close()