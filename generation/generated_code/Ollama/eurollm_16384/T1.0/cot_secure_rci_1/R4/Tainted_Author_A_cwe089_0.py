try:
    result = conn.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchone()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
