# connect to posgres database
import psycopg2

conn = psycopg2.connect(
    host="localhost", port=5432, database="pydb", user="postgres", password=""
)

db = conn.cursor()


db.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    age INT
)
""")
conn.commit()
