from flask import Flask

app = Flask(__name__)

# add pages by defining page and return the string
# simple routing
@app.route('/')
def index():
    return '<h1>Hello Puppy</h1>'

# more page routing
@app.route('/information')
def info():
    return " <h1>Puppies are cute!</h1>"

# dynamic routing
@app.route('/puppy/<name>')
def puppy(name):
    return "100th letter: {}".format(name[100])


if __name__ =='__main__':
    app.run(debug=True)
