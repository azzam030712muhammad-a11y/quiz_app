from db.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabel 1:Quiz(Kumpulan nama Quiz)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    # Tabel 2:Question(bank soal)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL,
            type TEXT NOT NULL
        )
    """)

    # Tabel 3:Relasi antara Quiz dan Question (many-to-many)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quiz(id),
            FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    """)

    conn.commit()
    conn.close()
            
