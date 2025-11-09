"""
Portfolio Website Backend Of Website Using Flask Micro Framwork
Authtor : Zen
"""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Zen Portfolio')


@app.route('/ru')
def indexru():
    return render_template('indexru.html')
if __name__ == '__main__':
    app.run(debug=True)