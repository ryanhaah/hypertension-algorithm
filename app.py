from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/algorithm")
def algorithm():
    return render_template("algorithm0.html")

@app.route("/indications")
def indications():
    return render_template("indications.html")

@app.route("/bloodpressure", methods = ["POST"])
def bloodpressure():
    systolic = request.form.get("systolic")
    diastolic = request.form.get("diastolic")
    if int(systolic) > 180 or int(diastolic) > 120:
        return render_template("algorithm1.5.html")
    elif int(systolic) in range(140, 181) or int(diastolic) in range(90, 121):
        return render_template("algorithm1.4.html")
    elif int(systolic) in range(130, 140) or int(diastolic) in range(80, 90):
        return render_template("algorithm1.3.html")
    elif int(systolic) in range(120, 130) and int(diastolic) in range(60, 80):
        return render_template("algorithm1.2.html")
    elif int(systolic) in range(90, 120) and int(diastolic) in range(60, 80):
        return render_template("algorithm1.1.html")
    elif int(systolic) in range(0, 90) or int(diastolic) in range(0, 60):
        return render_template("algorithm1.6.html")
    else:
        return render_template("invalid.html")

@app.route("/bloodpressure/stage1", methods = ["GET", "POST"])
def stage1():
    if request.method == "POST":
        stage1_key = request.form.getlist("condition")
        if stage1_key == ["3"]:
            return render_template("algorithm2.1.html")
        elif stage1_key == ["1"]:
            return render_template("algorithm2.2.html")
        elif stage1_key == ["2"] or stage1_key == ["1", "2"]:
            return render_template("algorithm3.3.html")
        else:
            return render_template("invalid.html")

@app.route("/bloodpressure/stage2", methods = ["GET", "POST"])
def stage2():
    if request.method == "POST":
        stage2_key = request.form.getlist("condition")
        if stage2_key == ["1"] or stage2_key == ["3"]:
            return render_template("algorithm2.2.html")
        elif stage2_key == ["2"] or stage2_key == ["1", "2"]:
            return render_template("algorithm3.3.html")
        else:
            return render_template("invalid.html")

@app.route("/bloodpressure/notblack")
def notblack():
    return render_template("algorithm3.1.html")

@app.route("/bloodpressure/isblack")
def isblack():
    return render_template("algorithm3.2.html")

@app.route("/bloodpressure/goal/success")
def success():
    return render_template("algorithm7.html")

@app.route("/bloodpressure/goal/1")
def goal1():
    return render_template("algorithm4.html")

@app.route("/bloodpressure/goal/2")
def goal2():
    return render_template("algorithm5.html")

@app.route("/bloodpressure/goal/refer")
def refer():
    return render_template("algorithm6.html")

if __name__ == "__main__":
    app.run(debug = True)