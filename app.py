from flask import Flask, render_template, redirect, request, session
from tempfile import mkdtemp
import os
from data import QUESTIONS, RISK_LEVELS, SAFETY_PLAN

DATABASE = 'results.db'
SECRET_KEY = os.urandom(24).hex()

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    """Count the answers and manage the home"""
    session.clear()

    if request.method == "POST":
        return redirect("/question/1")

    return render_template("index.html")


@app.route("/question/<int:num>", methods=["GET", "POST"])
def question(num):
    """Ask questions and save the answers."""

    if 'scores' not in session:
        session['scores'] = {}

    total_questions = len(QUESTIONS)

    if request.method == "POST":
        q_to_save_num = num - 1

        selected_option_index = request.form.get("option")

        if selected_option_index is None:
            return render_template("question.html",
                                   question=QUESTIONS[q_to_save_num],
                                   q_num=q_to_save_num,
                                   total_questions=total_questions,
                                   is_last_question=(q_to_save_num == total_questions),
                                   error="Debes seleccionar una opción para continuar.")

        try:
            option_index = int(selected_option_index)

            prev_question_data = QUESTIONS[q_to_save_num]
            score = prev_question_data["options"][option_index]["score"]

            # Save points
            session['scores'][f"q{q_to_save_num}"] = int(score)

            session.modified = True

            if num > total_questions:
                return redirect("/results")
            else:
                return redirect(f"/question/{num}")

        except (ValueError, IndexError):
            # If error, go to home
            return redirect("/")

    else:

        if num > 1:
            for i in range(1, num):
                prev_score_key = f"q{i}"
                if prev_score_key not in session.get('scores', {}):
                    return redirect(f"/question/{i}")

        current_question = QUESTIONS.get(num)

        if not current_question:
            if num > total_questions:
                return redirect("/results")
            return redirect("/")

        return render_template("question.html",
                               q_num=num,
                               question=current_question,
                               total_questions=total_questions,
                               is_last_question=(num == total_questions))


@app.route("/results")
def results():
    """Gives final score and indicates risk level."""

    total_questions = len(QUESTIONS)

    if 'scores' not in session or len(session.get('scores', {})) < total_questions:
        if 'scores' not in session or not session['scores']:
            return redirect("/")

        for i in range(1, total_questions + 1):
            prev_score_key = f"q{i}"

            if prev_score_key not in session['scores']:
                return redirect(f"/question/{i}")

        return redirect(f"/question/{total_questions}")

    total_score = 0
    for score_value in session['scores'].values():
        try:
            # Just in case convert to integer
            total_score += int(score_value)
        except (ValueError, TypeError):
            continue

    result_data = None
    for level in RISK_LEVELS:
        if level["min_score"] <= total_score <= level["max_score"]:
            result_data = level
            break

    if not result_data:
        result_data = RISK_LEVELS[0]

    session.clear()

    return render_template("results.html",
                           total_score=total_score,
                           # Max score is 2*8 = 16
                           max_score=len(QUESTIONS) * 2,
                           result=result_data,
                           safety_plan=SAFETY_PLAN
                           )
