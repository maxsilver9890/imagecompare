import sqlite3
import os
from PIL import Image
import imagehash

DB_NAME = "image_db.sqlite"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_path TEXT NOT NULL,
            phash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def compute_phash(image_path):
    img = Image.open(image_path)
    return str(imagehash.phash(img))


def register_image(name, image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file not found")

    phash = compute_phash(image_path)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO images (name, image_path, phash) VALUES (?, ?, ?)",
        (name, image_path, phash)
    )
    conn.commit()
    conn.close()


def search_image(image_path, threshold=10):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file not found")

    query_hash = imagehash.phash(Image.open(image_path))

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT name, phash FROM images")
    records = cur.fetchall()
    conn.close()

    best_match = None
    min_distance = float("inf")

    for name, stored_hash in records:
        distance = query_hash - imagehash.hex_to_hash(stored_hash)
        if distance < min_distance:
            min_distance = distance
            best_match = name
    if min_distance<= threshold:
        return best_match, min_distance
    return None , min_distance


def deregister_image(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM images WHERE name = ?", (name,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    return deleted

def deregister_image_by_id(image_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM images WHERE id = ?", (image_id,))
    conn.commit()

    deleted = cur.rowcount
    conn.close()
    return deleted
