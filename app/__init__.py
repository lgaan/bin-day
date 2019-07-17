from datetime import datetime, timedelta
from flask import Flask, render_template

DAYS = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
app = Flask(__name__)

@app.route("/")
def index_():
    date = datetime.now()
    day = DAYS[date.strftime("%A").lower()]

    if day != 3:
        if day > 3:
            next_bin_day = (date.day)+(day-3)+6
            if (next_bin_day%2) != 0:
                return render_template("main.html", day="Recycling", date=str(date).split(".")[0], week="Next")
            else:
                return render_template("main.html", day="General Waste", date=str(date).split(".")[0], week="Next")
        else:
            bin_day = (date.day)+(3-day-1)
            if (bin_day%2) != 0:
                return render_template("main.html", day="Recycling", date=str(date).split(".")[0], week="This")
            else:
                return render_template("main.html", day="General Waste", date=str(date).split(".")[0], week="This")
    else:
        if (date.day%2) != 0:
           return render_template("main.html", day="Recycling", date=str(date).split(".")[0], week="This")
        else:
            return render_template("main.html", day="General Waste", date=str(date).split(".")[0], week="This")

@app.route("/next")
def next_week():
    date = datetime.now()
    day = DAYS[date.strftime("%A").lower()]

    next_bin_day = (date.day+1)+(day-3)+6

    if (next_bin_day%2) != 0:
        return render_template("main.html", day="Recycling", date=str(datetime.strptime("2019-07-24", r"%Y-%m-%d")).split(".")[0], week="Next")
    else:
        return render_template("main.html", day="General Waste", date=str(datetime.strptime("2019-07-24", r"%Y-%m-%d")).split(".")[0], week="Next")
