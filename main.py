from flask import Flask, request, render_template, send_file

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hci')
def hci():
    return render_template('hci.html')

if __name__ == '__main__':
    app.run()

