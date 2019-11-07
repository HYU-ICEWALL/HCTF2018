from flask import Flask, render_template, request, render_template_string, send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/h1dden')
def flag():
	return render_template('flag.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)