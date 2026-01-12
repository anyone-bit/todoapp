from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # list to store tasks

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        if task:
            tasks.append(task)   # INSERT
    return render_template("index.html", tasks=tasks)

@app.route("/remove/<int:i>")
def remove(i):
    tasks.pop(i)   # REMOVE
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
