from web.app import create_app

app = create_app()



from db.connection import get_connection
from db.schema import create_tables
from scripts.seed import seed_questions, seed_quiz, seed_quiz_content
# from db.query import get_questions_by_quiz_and_type
# from db.query import get_next_question

def main():
    # current_id = 0
    # soal_ke = 0

    # while True:
    #     q = get_next_question(last_id=current_id, quiz_id=1) # quiz_id=1 → Math Quiz

    #     if not q:
    #         print("\n===Quiz Selesai! ===")
    #         break
    #     soal_ke += 1
    #     current_id = q["id"] #WAJIB update, atau loop infinite!

    #     print(f"\nSoal {soal_ke}: {q['question']} [{q['type']}]")
    #     print(f" A. {q['answer']}")
    #     print(f" B. {q['wrong1']}")
    #     print(f" C. {q['wrong2']}")
    #     print(f" D. {q['wrong3']}")

    #     input("Tekan Enter untuk soal berikutnya...")
        
    # Test 1:semua soal dari Math Quiz (id=1)
    # question = get_questions_by_quiz_and_type(1)
    # print(f"Semua soal dari Math Quiz: {len(quesntion)} soal")
    # for q in question:
    #     print(" -", dict(q)['question'], f"[{dict(q)['type']}]")

    # print()

    # # Test 2:hanya soal 'essay' dari Math Quiz
    # easy = get_questions_by_quiz_and_type(1, 'easy')
    # print(f"Soal 'EASY' dari Math Quiz: {len(easy)} soal")

    # for q in easy:
    #     print(" -", dict(q)['question'])


    # create_tables()
    # print("Tables created!")
    seed_questions()
    seed_quiz()
    seed_quiz_content()
    print("Data seeded!")
    # conn = get_connection()
    # print("Database Connected:", conn)
    # conn.close()

if __name__ == "__main__":
    app.run(debug=True)
    # main()


