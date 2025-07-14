from flask import Flask, render_template, request
import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form.get('todo')
        feeling = request.form.get('feeling')
        note = request.form.get('note')
        date = datetime.date.today().isoformat()

        entry = {
            'date': date,
            'todo': todo,
            'feeling': feeling,
            'note': note
        }

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(entry)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
