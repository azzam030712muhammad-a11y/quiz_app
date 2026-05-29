from db.query import get_all_quizzes, get_next_question
from flask import redirect, url_for, session, request, render_template



def register_routes(app):

    @app.route("/")
    def home():
        quizzes = get_all_quizzes()
        return render_template("index.html", quizzes=quizzes)

        # html = "<h1>Quiz list</h1><ul>"

        # for q in quizzes:
        #     html += f"<li><a href='/start/{q['id']}'>{q['name']}</a></li>"

        # html += "</ul>"
        # return html
    

    @app.route("/start/<int:quiz_id>")
    def start_quiz(quiz_id):
        session['quiz_id'] = quiz_id
        session['last_id'] = 0
        session['score']  = 0

        return redirect(url_for("question"))
    
    @app.route("/question", methods=["GET", "POST"])
    def question():
        quiz_id = session.get('quiz_id')
        last_id = session.get('last_id', 0)

        if not quiz_id:
            return "<h2>Belum pulih quiz. <a href='/'>Kembali</a></h2>"
        #--Handle Post---------------------------------
        if request.method == "POST":
            user_answer = request.form.get("answer")
            correct_answer = session.get("correct_answer")

            if user_answer == correct_answer:
                session['score'] += 1
                session['feedback'] = "Correct!"
            else:
                session["feedback"] = f"Wrong! Jawaban: {correct_answer}"

            return redirect(url_for("question"))
        #--Handle Get---------------------------------
        q = get_next_question(last_id, quiz_id)

        if not q:
            return redirect(url_for("result"))
        
        session['last_id'] = q['id']
        session['correct_answer'] = q['answer']

        feedback = session.pop("feedback", None)
        
        # html = ""

        # if feedback:
        #     html += f"<p><b>{feedback}</b></p><hr>"
            
        # html += f"""
        # <h2>{q['question']}</h2>
        # <p>Skor sekarang: {session.get('score', 0)}</p>

        
        # <form method='POST'>
        #     <input type='radio' name='answer' value='{q['answer']}' > {q['answer']}<br>
        #     <input type='radio' name='answer' value='{q['wrong1']}' > {q['wrong1']}<br>
        #     <input type='radio' name='answer' value='{q['wrong2']}' > {q['wrong2']}<br>
        #     <input type='radio' name='answer' value='{q['wrong3']}' > {q['wrong3']}<br><br>
        #     <button type='submit'>Submit</button>
        # </form>
        # """
        return render_template("question.html", question=q, feedback=feedback)

    @app.route("/result")
    def result():
        score = session.get('score', 0)
        return render_template("result.html", score=score)

        # html = f"""
        # <h1>Quiz Selesai!</h1>
        # <h2>Skor Anda: {score}</h2>
        # <a href='/'>Main lagi</a>
        # """
        # return html

