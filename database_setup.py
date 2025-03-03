import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("messages.db")
cursor = conn.cursor()

# Create table for messages
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database setup complete!")