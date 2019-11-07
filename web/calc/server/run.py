from flask import Flask, render_template, request, render_template_string
import os

__FLAG__ = 'HCTF{fl4sk_temp1ate_injecti0n_wi7hout_'_'_:p}'

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
	return render_template('index.html')

allow_char = "{}abcdefghijklmnopqrstuvwxyz0123456789+-/*.[]()"

@app.route('/api/calc', methods=['POST'])
def calc():
	b64 = request.form['b64'].decode('base64').strip()
	for strstr in b64:
		if strstr not in allow_char:
			return "Not Allowed Character!"
	return render_template_string("{{" + b64 + "}}")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)