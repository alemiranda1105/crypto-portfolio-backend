

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def LoginResponseModel(data, token):
    return {
        "data": [data],
        "code": 200,
        "token": token
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }