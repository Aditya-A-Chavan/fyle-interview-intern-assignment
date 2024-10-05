from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))

    @classmethod
    def error(cls, status_code, message="An error occurred", error_type="FyleError"):
        error_response = {
            "error": error_type,
            "message": message
        }
        return make_response(jsonify(error_response), status_code)