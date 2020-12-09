from flask import Flask, render_template
from flask_basicauth import BasicAuth
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='./static')
# app.config['BASIC_AUTH_USERNAME'] = 'username'
# app.config['BASIC_AUTH_PASSWORD'] = 'password'
# basic_auth = BasicAuth(app)

@app.route('/')
# @basic_auth.required
def root():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8000')
