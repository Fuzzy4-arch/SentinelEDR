import sqlite3
from pathlib import Path


DATABASE_PATH = Path("sentineledr.db")


def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            risk INTEGER NOT NULL,
            pid INTEGER,
            process TEXT,
            reason TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_alert(alert):
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute(
        """
        INSERT INTO alerts (
            alert_type,
            severity,
            risk,
            pid,
            process,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            alert["type"],
            alert["severity"],
            alert["risk"],
            alert["pid"],
            alert["process"],
            alert["reason"],
        ),
    )

    connection.commit()
    connection.close()


def get_alerts():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.execute(
        """
        SELECT
            id,
            alert_type,
            severity,
            risk,
            pid,
            process,
            reason
        FROM alerts
        ORDER BY id DESC
        """
    )

    alerts = cursor.fetchall()
    connection.close()

    return alerts


if __name__ == "__main__":
    initialize_database()
    print("SentinelEDR database initialized.")