import requests

global server_url
global open_url

server_url = "https://server.gauth.co.kr"
open_url = "https://open.gauth.co.kr/user"
    
def code_issuance(email: str, password:str) -> str :
    URL = server_url + "/oauth/code"
    response = requests.post(URL, json={"email":email, "password" : password})
    return response.content