from random import randint

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('construction.html')
    # return render_template('base.html', rand=randint(1,1000))

@app.route('/test')
def test():
    return render_template('base.html', rand=randint(1,1000))

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
