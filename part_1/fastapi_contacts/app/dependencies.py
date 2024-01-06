# app/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi.throttling import ThrottlingRateLimit, ThrottlingMiddleware
from .security import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

# Rate limiting configuration
throttle_contact_routes = ThrottlingRateLimit(
    requests=5,  # Number of requests allowed
    seconds=60,  # Time window for rate limiting in seconds
)

# Apply rate limiting to the contact routes
throttle_middleware_contact_routes = ThrottlingMiddleware(
    throttle=[throttle_contact_routes],
    backend="memory"  # You can use "redis" for a distributed setup
)

def get_current_user_rate_limited(token: str = Depends(oauth2_scheme)):
    return get_current_user(token=token)

def get_current_user_rate_limited_throttle(token: str = Depends(oauth2_scheme)):
    return get_current_user(token=token)
