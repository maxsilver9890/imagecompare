import sqlite3
from database import DB_NAME


def list_images():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT id, name, image_path FROM images")
    rows = cur.fetchall()

    conn.close()
    return rows
