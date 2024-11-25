from models.user import User

def individual_serial(user: User)->dict:
    convertedUser = {
        "user_id":user["_id"],
        "name": user["name"],
    "email_id": user["email_id"],
    "password": user["password"] 
    }
    return convertedUser