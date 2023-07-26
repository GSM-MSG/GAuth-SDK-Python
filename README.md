# GAuth-Python

>> 단 하나의 계정으로 모든 GSM의 서비스를 이용할 수 있게.

```
      ___           ___           ___                       ___     
     /  /\         /  /\         /__/\          ___        /__/\    
    /  /:/_       /  /::\        \  \:\        /  /\       \  \:\   
   /  /:/ /\     /  /:/\:\        \  \:\      /  /:/        \__\:\  
  /  /:/_/::\   /  /:/ /::\   ___  \  \:\    /  /:/     ___ /  /::\ 
 /__/:/__\/\:\ /__/:/ /:/\:\ /__/\  \__\:\  /  /::\    /__/\  /:/\:\
 \  \:\    /:/ \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\   \  \:\/:/__\/
  \  \:\  /:/   \  \::/       \  \:\  /:/  \__\/  \:\   \  \::/     
   \  \:\/:/     \  \:\        \  \:\/:/        \  \:\   \  \:\     
    \  \::/       \  \:\        \  \::/          \__\/    \  \:\    
     \__\/         \__\/         \__\/                     \__\/
```

**GAuth는 여러 프로젝트에서 편하게 로그인을 구현할 수 있고 사용자들이 새로 계정을 만들 필요가 없어 접근성을 더욱 쉽게 만들어줄 수 있는 서비스 입니다.**

## Installation

```
// pip3 install gauth-python
// pip install gauth-python
```

## How to use
### Code 발급
```python
from gauth_python.requests import code_issuance

code_issuance(
    email=YOUR_EMAIL,
    password=YOUR_PASSWORD
)
```

### token 발급
```python
from gauth_python.requests import token_issuance

token_issuance(
    code = YOUR_CODE,
    clientId = YOUR_CLIENT_ID,
    clientSecret = YOUR_CLIENT_SECRET,
    redirectUri = YOUR_REDIRECT_URL
)
```

### token 재발급
```python
from gauth_python.requests import token_reissuance

token_reissuance(
    Authorization = YOUR_REFRESH_TOKEN
)

```


### 유저 정보 가져오기
```python
from gauth_python.requests import user_info

user_info(
   Authorization = YOUR_ACCESS_TOKEN
)
```