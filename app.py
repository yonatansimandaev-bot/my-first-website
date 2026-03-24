from flask import Flask, render_template, request, redirect
from storage import load_tasks, save_tasks
from scheduler import generate_schedule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()

    if request.method == "POST":
        task = {
            "name": request.form["name"],
            "color": request.form["color"],
            "duration": request.form.get("duration", "30"),
            "days": request.form.get("days", "Mon,Tue,Wed,Thu,Fri"),
            "range_start": request.form.get("range_start", "15:00"),
            "range_end": request.form.get("range_end", "20:00"),
            "start": request.form.get("start", ""),
            "end": request.form.get("end", "")
        }
        tasks.append(task)
        save_tasks(tasks)
        return redirect("/")

    schedule = generate_schedule(tasks)

    return render_template("index.html", tasks=tasks, schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)
