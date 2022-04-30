import os
from app.main import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app(os.getenv('OJT') or 'test')
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def hello_world():
    return 'Angular Flask Frame Work'


@app.route('/home')
def home():
    return 'Angular Flask Frame Work'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
