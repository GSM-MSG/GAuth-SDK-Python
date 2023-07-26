from gauth_python_package.gauth_python import GAuthPython
import gauth_python_package

def test_function():
    assert GAuthPython.code_issuance("exampleString", "exampleString")
    assert GAuthPython.token_issuance("exampleString","exampleString","exampleString","exampleString")
    assert GAuthPython.token_reissuance()
    assert GAuthPython.user_info()

