from rest_framework.authtoken.models import Token

def get_token_value_from_headers(token_headers):
    return token_headers.split(" ")[1]

def get_user_by_token_headers(request):
    token_headers = request.headers.get("Authorization")
    token = get_token_value_from_headers(token_headers)
    token_object = Token.objects.get(key=token)
    return token_object.user
