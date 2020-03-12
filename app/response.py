from flask import jsonify, make_response


def ok(data, msg):
    res = {
        'data': data,
        'message': msg
    }

    return make_response(jsonify(res)), 200


def badRequest(data, msg):
    res = {
        'data': data,
        'message': msg
    }

    return make_response(jsonify(res)), 400
