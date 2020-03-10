from flask import jsonify, make_response


def ok(values, msg):
    res = {
        'values': values,
        'message': msg
    }

    return make_response(jsonify(res)), 200


def badRequest(values, msg):
    res = {
        'values': values,
        'message': msg
    }

    return make_response(jsonify(res)), 400
