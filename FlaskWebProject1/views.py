from flask import Flask, request, render_template, send_file

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/HCI')
def hci():
    return render_template('HCI.html')

@app.route('/download/')
def return_files_tut():
	try:
		return send_file('/home/site/wwwroot/download/[HCI-under]hw1_2017320229.hwp')
	except Exception as e:
		return str(e)

if __name__ == '__main__':
    app.run()

