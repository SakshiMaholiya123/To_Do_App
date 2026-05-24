from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# to the verify password
def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# to create token
def create_token(data:dict):

    encode=data.copy()

    expire=datetime.utcnow()+timedelta(minutes=30)

    encode.update({
        "exp":expire
    })

    token = jwt.encode(
        encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token