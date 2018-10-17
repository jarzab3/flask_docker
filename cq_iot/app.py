from flask import Flask, render_template, Response, jsonify, request
import settings
from flask import abort

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

log = settings.logging


@app.route('/')
def index():
    return render_template('index.html')


options = [
    {
        'id': 1,
        'title': u'Add new device',
        'description': u'More description for add device option',
        'status': True
    },
    {
        'id': 2,
        'title': u'View device',
        'description': u'More description for view device option',
        'status': False
    }
]


@app.route('/options/api/v1.0/options', methods=['GET'])
def get_options():
    return jsonify({'options': options})


@app.route('/options/api/v1.0/options/<int:option_id>', methods=['GET'])
def get_task(option_id):
    option = [option for option in options if option['id'] == option_id]
    if len(option) == 0:
        abort(404)
    return jsonify({'task': option[0]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
    # app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=(
    #     '/etc/letsencrypt/live/cq.jarzebak.eu/cert.pem', '/etc/letsencrypt/live/cq.jarzebak.eu/privkey.pem'))
    log.debug("Started up cq app")
