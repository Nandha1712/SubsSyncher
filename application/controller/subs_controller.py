from flask import request, Blueprint, jsonify, render_template, make_response
from datetime import datetime

from application.utils.validator import login_required

subs_sync = Blueprint('subs_syncher', __name__)


@subs_sync.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        __user = request.form['user_name']
        print(__user)

        response = make_response(render_template('welcome.html'))
        response.set_cookie('authToken', value="xyz")
        return response

    return jsonify({'code': 400})


@subs_sync.route('/home', methods=['GET'])
@login_required(request)
def hello_ping():
    current = datetime.utcnow()
    detail = {"code": 200, "time": current}
    return jsonify(detail)
