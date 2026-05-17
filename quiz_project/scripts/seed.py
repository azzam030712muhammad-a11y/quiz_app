from db.connection import get_connection

# 
def seed_questions():
    conn = get_connection()
    cursor = conn.cursor()

    questions = [
        #Format: (question, answer, wrong1, wrong2, wrong3, type)

        #("2+2=?", "4", "3", "5", "6", "easy"),
        ("Sebuah persegi memiliki sisi 8 cm. Berapa luas persegi tersebut?",
        "64 cm²",
        "16 cm²",
        "32 cm²",
        "128 cm²",
        "Matematika"),
        ("Hasil dari 3x+5=20, berapakah nilai x?",
        "5",
        "3",
        "4",
        "6",
        "Matematika"),
        ("Sebuah toko memberi diskon 20 persen dari harga Rp50.000. Berapa harga setelah diskon?",
        "40.000",
        "50.000",
        "30.000",
        "20.000",
        "Matematika"),
        ("Apa fungsi utama dari akar pada tumbuhan?",
        "Menyerap air dan nutrisi dari tanah",
        "Menyerap cahaya matahari",
        "Menyerap udara",
        "Menyerap karbon dioksida",
        "IPA"),
        ("Sebutkan perubahan wujud dari air menjadi uap!",
        "Evaporasi",
        "Kondensasi",
        "Sublimasi",
        "Presipitasi",
        "IPA"),
        ("Gaya yang menyebabkan benda jatuh ke bawah disebut apa?",
        "Gravitasi",
        "Magnetisme",
        "Listrik",
        "Gesekan",
        "IPA"),
        ("Siapa presiden pertama Indonesia?",
        "Soekarno",
        "Soeharto",
        "Bacharuddin Jusuf Habibie",
        "Megawati Soekarnoputri",
        "IPS"),
        ("Apa nama benua tempat negara Indonesia berada?",
        "Asia",
        "Afrika",
        "America",
        "Australia",
        "IPS"),
        ("Sebutkan salah satu contoh kegiatan ekonomi di bidang pertanian!",
        "Menanam padi",
        "Membuat kerajinan tangan",
        "Membuka toko",
        "Mengolah hasil pertanian",
        "IPS"),
    ]

    cursor.executemany("""
    INSERT INTO questions (question, answer, wrong1, wrong2, wrong3, type)
    VALUES (?, ?, ?, ?, ?, ?)
    """, questions)

    conn.commit()
    conn.close()

#
def seed_quiz():
    conn = get_connection()
    cursor = conn.cursor()

    quizzes = [
        ("Matematika",),
        ("IPA",),
        ("IPS",)
    ]

    cursor.executemany("""
    INSERT INTO quiz (name) VALUES (?)
    """, quizzes)

    conn.commit()
    conn.close()    

#Fungsi 3: Relasi antara Quiz dan Question (many-to-many)
def seed_quiz_content():
    conn = get_connection()
    cursor = conn.cursor()

    quiz_content = [
        #Format: (quiz_id, question_id)
        (1, 1), (1, 2), (1, 3), # Quiz Matematika
        (2, 4), (2, 5), (2, 6), # Quiz IPA
        (3, 7), (3, 8), (3, 9)  # Quiz IPS
    ]

    cursor.executemany("""
    INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)
    """, quiz_content)

    conn.commit()
    conn.close()