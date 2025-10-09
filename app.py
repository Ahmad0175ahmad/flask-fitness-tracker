from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (you can replace with SQLite later)
workouts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        exercise = request.form.get("exercise")
        duration = request.form.get("duration")
        calories = request.form.get("calories")

        if exercise and duration and calories:
            workouts.append({
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            })
        return redirect(url_for("index"))

    total_calories = sum(int(w["calories"]) for w in workouts) if workouts else 0
    total_time = sum(int(w["duration"]) for w in workouts) if workouts else 0

    return render_template("index.html", workouts=workouts, total_calories=total_calories, total_time=total_time)


@app.route("/clear", methods=["POST"])
def clear():
    workouts.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
