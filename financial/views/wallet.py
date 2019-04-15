from flask import Blueprint, jsonify, render_template

wallet = Blueprint('wallet', __name__, url_prefix='')


@wallet.route("/wallet", methods=['GET'])
def get_wallet():
    return render_template('index.html')
