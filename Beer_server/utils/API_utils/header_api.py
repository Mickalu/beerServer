def get_api_authentification_token_header(token):
    authentification_value = "Token {}".format(token)
    header_api = {
        "Authentification": authentification_value,
    }

    return header_api
