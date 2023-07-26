import requests

global server_url
global open_url

server_url = "https://server.gauth.co.kr"
open_url = "https://open.gauth.co.kr/user"
    
def code_issuance(email: str, password:str) -> str :
    URL = server_url + "/oauth/code"
    response = requests.post(URL, json={"email":email, "password" : password})
    return response.content

def token_issuance(code : str, clientId: str, clientSecret: str, redirectUri: str) -> str :
    URL = server_url + "/oauth/token"
    response = requests.post(URL, json={"code" : code,
                                    "clientId": clientId,
                                        "clientSecret": clientSecret,
                                        "redirectUri" : redirectUri})
    return response.content

def token_reissuance(refreshToken : str) -> str:
    URL = server_url + "/oauth/token"
    response = requests.patch(URL, headers={"refreshToken" : "Bearer " + refreshToken})
    return response.content