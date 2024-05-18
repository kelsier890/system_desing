import os, requests

def login(request):
    auth = requests.authorization
    if not auth:
        return None, ("missing credentials",401)
    
    bassicAuth = (auth.username, auth.password)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
        auth=bassicAuth
    )

    if response.status_code == 200:
        return response.txt, None
    else:
        return None, (response.txt, response.status_code)

    
    

