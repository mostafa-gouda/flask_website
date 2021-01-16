from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


def save_to_text(data):
    with open("database.csv", "a") as database:
        database.write(f"{data['email']},{data['subject']},{data['message']}\n")


def save_to_csv(data):
    with open("database.csv",newline="\n", mode="a") as database:
        writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([data['email'], data['subject'], data['message']])


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:file_name>')
def home(file_name):
    return render_template(file_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        save_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Ooops"
