import requests

global server_url
global open_url

server_url = "https://port-0-gauth-backend-85phb42bluutn9a7.sel5.cloudtype.app"
open_url = "https://port-0-gauth-resource-server-71t02clq411q18.sel4.cloudtype.app/user"
    
def code_issuance(email: str, password:str) -> str :
    URL = server_url + "/oauth/code"
    response = requests.post(URL, json={"email":email, "password" : password})
    response_json = response.content.decode("utf-8")
    return response_json

def token_issuance(code : str, clientId: str, clientSecret: str, redirectUri: str) -> str :
    URL = server_url + "/oauth/token"
    response = requests.post(URL, json={"code" : code,
                                        "clientId": clientId,
                                        "clientSecret": clientSecret,
                                        "redirectUri" : redirectUri})
    response_json = response.content.decode("utf-8")
    return response_json

def token_reissuance(refreshToken : str) -> str:
    URL = server_url + "/oauth/token"
    response = requests.patch(URL, headers={"refreshToken" : "Bearer " + refreshToken})
    response_json = response.content.decode("utf-8")
    return response_json

def user_info(accessToken : str) -> str:
    URL = open_url + "/user"
    response = requests.get(URL, headers={"Authorization": "Bearer " + accessToken})
    response_json = response.content.decode("utf-8")
    return response_json