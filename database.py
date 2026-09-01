import sqlite3

def create_database():
    connection = sqlite3.connect("sih26036.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        applicant_name TEXT NOT NULL,
        instrument_type TEXT NOT NULL,
        instrument_id TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

def add_application(applicant_name, instrument_type, instrument_id):
    connection = sqlite3.connect("sih26036.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO applications
    (applicant_name, instrument_type, instrument_id, status)
    VALUES (?, ?, ?, ?)
    """, (applicant_name, instrument_type, instrument_id, "Pending"))

    connection.commit()
    connection.close()

def get_applications():
    connection = sqlite3.connect("sih26036.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    connection.close()
    return applications

def approve_application(application_id):
    connection = sqlite3.connect("sih26036.db")
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?
    """, ("Approved", application_id))
    connection.commit()
    connection.close()
    

