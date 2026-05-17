from db.connection import get_connection

def get_questions_by_quiz(quiz_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN questions q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
    ORDER BY qc.id
    """, (quiz_id,))

    results = cursor.fetchall()
    conn.close()
    return results

def get_all_quizzes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM quiz")
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_questions_by_quiz_and_type(quiz_id, q_type=None):
    conn = get_connection()
    cursor = conn.cursor()

    # Query dasar (selalu dipakai)
    query = """
    SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN questions q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
    """
    params = [quiz_id,]

    # Tambahkan filter berdasarkan tipe soal jika diberikan
    if q_type:
        query += " AND q.type = ?"
        params.append(q_type)

    query += " ORDER BY qc.id"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def get_next_question(last_id=0, quiz_id=1, q_type=None):
    """
    Ambil 1 soal berikutnya setelah posisi last_id.
    last_id = 0 → ambil soal pertama
    last_id = 3 → ambil soal setelah quiz_content.id = 3
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT qc.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN questions q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
        AND qc.id > ?
    """
    params = [quiz_id, last_id]

    if q_type:
        query += " AND q.type = ?"
        params.append(q_type)

    query += " ORDER BY qc.id LIMIT 1"

    cursor.execute(query, params)
    result = cursor.fetchone() #Hanya 1 baris
    conn.close()
    return result

#     Iterasi 1: last_id = 0 → ambil baris pertama (qc.id=1) → soal '2+2=?'
# current_id = 1 (simpan ID ini)
# Iterasi 2: last_id = 1 → ambil baris setelah ID=1 (qc.id=2) → soal '3+5=?'

# current_id = 2
# Iterasi 3: last_id = 2 → ambil baris setelah ID=2 (qc.id=4) → soal '12x12=?'
# current_id = 4
# Iterasi 4: last_id = 4 → tidak ada lagi → return None → quiz selesai!

