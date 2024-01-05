from datetime import datetime, timedelta
from typing import Dict
import jwt

JWT_SECRET = "9b7799e4e69e8419ea54596df9bd214948b3b0c5c1ebdf3510d6b67a4145f3cc"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080

def sign_jwt(username: str) -> Dict[str, str]:
    payload = {
        "sub": username,
        "expires": (datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).isoformat()
    }

    token = jwt.encode(payload, JWT_SECRET)

    return token

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET)
        expires = datetime.fromisoformat(decoded_token["expires"])
        return decoded_token if expires >= datetime.utcnow() else None
    except:
        return {}
