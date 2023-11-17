from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('index.html')