"""
Generate SQLite database with Streamlit app usage logs.
For mockup screenshot purposes.
"""

import sqlite3
from datetime import datetime, timedelta
import random

DB_PATH = "projects/streamlit-center/streamlit_usage_logs.db"

# Sample data
USERS = ["104582", "287341", "156093", "342718", "098264", "471935"]
PAGES = ["Dashboard", "Analytics", "Reports", "Settings", "Data Explorer"]


def generate_logs():
    """Generate sample usage log entries."""
    logs = []
    base_date = datetime(2024, 11, 15, 9, 0, 0)

    for i in range(12):
        visit_date = base_date + timedelta(
            days=random.randint(0, 10),
            hours=random.randint(0, 8),
            minutes=random.randint(0, 59),
        )
        user_id = random.choice(USERS)
        page = random.choice(PAGES)

        logs.append((visit_date.strftime("%Y-%m-%d %H:%M:%S"), user_id, page))

    # Sort by date
    logs.sort(key=lambda x: x[0])
    return logs


def create_database():
    """Create SQLite database with usage logs table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usage_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visit_date TEXT NOT NULL,
            user_id TEXT NOT NULL,
            page_visited TEXT NOT NULL
        )
    """)

    # Clear existing data
    cursor.execute("DELETE FROM usage_logs")

    # Insert sample logs
    logs = generate_logs()
    cursor.executemany(
        "INSERT INTO usage_logs (visit_date, user_id, page_visited) VALUES (?, ?, ?)",
        logs,
    )

    conn.commit()
    conn.close()

    print(f"Database created at: {DB_PATH}")
    print(f"Inserted {len(logs)} log entries.")


if __name__ == "__main__":
    create_database()
