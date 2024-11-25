from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer 
from models.user import User, EmailAndPassword
from config.database import user_collection
from schemas.user_schema import individual_serial
from handlers.hashing import hash_password, verify_password
from handlers.jwt_handler import create_access_token,verify_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
def say_hi(token: str =Depends(oauth2_scheme)):
    valid = verify_access_token(token)
    if not valid:
        return HTTPException( detail="Invalid token")
    return "Hi fast api users!"

# Register user
@router.post("/register")
async def register(data: User):
    # Check user already registered
    existing_user =  user_collection.find_one({"email_id": data.email_id})

    # Already exist return exception
    if existing_user:
       return HTTPException(
           status_code= 400,           
          detail="Email already registered"
       )
    
    # Hash the password
    hashed_pw = hash_password(data.password)
    data.password = hashed_pw

    # Convert model into dict
    user = dict(data)

    # Add the user to collection
    user_collection.insert_one(user)

    # return success res
    res = {
        "status":"ok",
        "data": "User created successfully! "
    }
    return res


# User login
@router.post("/login")
async def login_with_email_password(data: EmailAndPassword):
    existing_user = user_collection.find_one({"email_id": data.email})
    if not existing_user or not verify_password(data.password,existing_user["password"]):
        return HTTPException(
           status_code= 401,           
          detail="Invalid credentials"
       )
    token=  create_access_token({"sub":data.email})
    res ={
        "status":"ok",
        "token": token
    }

    return res
    
