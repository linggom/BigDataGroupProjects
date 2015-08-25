from flask import Flask, render_template, send_from_directory


app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return render_template("index.html", title = 'Home')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/home')
def home():
    return render_template("index.html", title = 'Home')

if __name__ == '__main__':
    app.run()
