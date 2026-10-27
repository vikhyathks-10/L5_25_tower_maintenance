
"""Manage tower maintenance, service records, and fault risk."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE towers (
        id INTEGER PRIMARY KEY,
        site TEXT,
        last_service INTEGER,
        faults INTEGER
    )
    """
)


def add_tower(site, last_service, faults=0):
    """Add a tower to the maintenance database."""
    conn.execute(
        """
        INSERT INTO towers (site, last_service, faults)
        VALUES (?, ?, ?)
        """,
        (site, last_service, faults),
    )
    conn.commit()


def service_tower(tower_id, year):
    """Service a tower and reset its fault count."""
    try:
        cursor = conn.execute(
            """
            UPDATE towers
            SET last_service = ?, faults = 0
            WHERE id = ?
            """,
            (year, tower_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        print("Service failed.")
        return False


def overdue(year):
    """Return sites overdue for maintenance by two or more years."""
    rows = conn.execute(
        "SELECT site, last_service FROM towers"
    ).fetchall()

    result = []
    for site, last_service in rows:
        if year - last_service >= 2:
            result.append(site)

    return result


def risk_level(tower_id):
    """Return a tower's risk level, or None if it does not exist."""
    row = conn.execute(
        "SELECT faults FROM towers WHERE id = ?",
        (tower_id,),
    ).fetchone()

    if row is None:
        return None

    if row[0] > 3:
        return "high"
    return "normal"


def snapshot():
    """Return a snapshot of all tower records."""
    return conn.execute("SELECT * FROM towers").fetchall()


def main():
    """Run the sample tower maintenance scenario."""
    add_tower("Ridge-A", 2021, 5)
    add_tower("Coast-B", 2024)

    service_count = int(service_tower(2, 2025))
    total = len(snapshot())

    print(
        overdue(2025),
        risk_level(1),
        total,
        service_count,
    )


if __name__ == "__main__":
    main()
