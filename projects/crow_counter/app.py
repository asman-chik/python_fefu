from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

crows_count = 0

@app.route('/')
def index():
    return render_template('index.html', count=crows_count)

@app.route('/add_crow', methods=['POST'])
def add_crow():
    global crows_count
    crows_count += 1  
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)