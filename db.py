import psycopg2

conn = psycopg2.connect(
    host="db.supabase.co",
    database="postgres",
    user="postgres",
    password="yourpassword"
)

cursor = conn.cursor()

import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

print("Database connected")