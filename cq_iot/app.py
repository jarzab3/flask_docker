from flask import Flask, render_template, Response, jsonify, request
import settings


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

log = settings.logging

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/_apiQuery')
def api_query_task():
    query = request.args.get('apiQ0', "", type=str).strip()
    global color

    reply = ""

    if query == "color":
        color = True
        reply = "Changed to color"
    elif query == "gray":
        color = False
        reply = "Changed to gray"

    return jsonify(result=reply)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
    # app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=(
    #     '/etc/letsencrypt/live/cq.jarzebak.eu/cert.pem', '/etc/letsencrypt/live/cq.jarzebak.eu/privkey.pem'))
    log.debug("Started up cq app")
