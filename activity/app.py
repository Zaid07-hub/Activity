from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Zaid_Home.html')

@app.route('/Family')
def city():
    return render_template('Family.html')

@app.route('/city')
def family():
    return render_template('zaid_city.html')

if __name__ == "__main__":
    app.run(debug=True)