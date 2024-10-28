import os
import requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("Unauthorized, Missing Credentials", 401)

    basicAuth = (auth.username, auth.password)

    response = requests.post(
        url=f"http://{os.environ.get('AUTH_SVC_ADDRESS')}",
        auth=basicAuth
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
