from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.covid19api.com/summary"
    url_data = requests.get(url)
    json_data = url_data.json()
    global_stats = json_data["Global"]

    india_stats = json_data["Countries"][76]
    
    return render_template("home.html", global_stats=global_stats, india_stats=india_stats)

@app.route('/world', methods=["GET", "POST"])
def world_cases():
    url = "https://api.covid19api.com/summary"
    url_data = requests.get(url)
    json_data = url_data.json()

    countries = json_data["Countries"]
    # "countries" this var has 0 to 189 index
    # print(countries[189])

    return render_template("world_cases.html", countries=countries)

@app.route('/india')
def india_cases():
    url = "https://api.covid19india.org/data.json"
    url_data = requests.get(url)
    json_data = url_data.json()

    state_wise_data = json_data["statewise"]
    # Sate Wise Data Has 0 to 37 index
    
    

    return render_template("india_cases.html", state_wise_data=state_wise_data)


app.run(debug=True)