from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disease_detection', methods=['POST', 'GET'])
def disease_detection():
    pred = 'null'
    if request.method == 'POST':
        s1 = request.form['s1']
        s2 = request.form['s2']
        s3 = request.form['s3']
        s4 = request.form['s4']
        s5 = request.form['s5']

        # generate a prediction using the input values
        pred = predict(s1, s2, s3, s4, s5)

        return render_template('Detection.html', data=pred)

    else:
        return render_template('Detection.html', data=pred)

if __name__ == '__main__':
    app.run(debug=True)
