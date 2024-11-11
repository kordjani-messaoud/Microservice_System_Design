import requests
import os

def token(request):
    if not 'Authorization' in request.headers:
        return None, ('Unauthorized, Missing Credentials', 401)
    
    token = request.headers['Authorization']
    if not token:
        return None, ('Unauthorized, Missing Credentials', 401)

    response = requests.post(
        url=f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={'Authorization': token}
    )
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)