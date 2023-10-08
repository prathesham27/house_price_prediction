from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
@app.route('/')
def welcome():
     return render_template('index.html')


@app.route('/predict', methods=('GET', 'POST'))
def predict():
     title = request.form['title']
     content = request.form['content']

     return title


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
