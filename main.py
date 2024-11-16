from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart-data')
def chart_data():
    data ={
        "categories": ['January', "February", "March", "April", "May"],
        "series":[
            {"name": "Dataset 1", "data":[random.randint(0,100) for _ in range(5)]},
            {"name": "Dataset 2", "data":[random.randint(0,100) for _ in range(5)]},
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)