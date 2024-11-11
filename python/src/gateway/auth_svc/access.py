import os
import requests

def login(request):
    auth = request.authorization
    if not auth:
        return None, ('Unauthorized, Missing Credentials', 401)
    else:
        basic_auth = (auth.username, auth.password)

    try:
        response = requests.post(
            url=f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
            auth=basic_auth
        )
    except Exception as err:
        return None, (f'\nInternal Server Error: {err}\n', 500)

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)