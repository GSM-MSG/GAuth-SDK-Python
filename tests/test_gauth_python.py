from gauth_python import requests

def test_function():
    assert requests.code_issuance("exampleString", "exampleString")
    assert requests.token_issuance("exampleString","exampleString","exampleString","exampleString")
    assert requests.token_reissuance()
    assert requests.user_info()

