import jwt
from jwt import InvalidTokenError
from app.core.config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)
    
    to_encode.update({
      "exp": expire
    })
    
    return jwt.encode(
      to_encode,
      SECRET_KEY,
      algorithm=ALGORITHM
      )

def verify_access_token(token : str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )
        return payload
    except InvalidTokenError:
        return None