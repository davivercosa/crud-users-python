from connection.database import engine
from sqlalchemy.orm import Session
from queries import UserQuery

class UserModel:

    def create(userName, userEmail, userAge, userGender):
        with Session(bind = engine) as session:
            
            newUserQuery = UserQuery.User(name = userName, email = userEmail, age = userAge, gender = userGender)
            
            session.add_all([newUserQuery])
            session.commit()
        
    def readAll():
        with Session(bind = engine) as session:
            user = session.query(UserQuery.User).all()

            userList = []

            for user_obj in user:
                user_obj = user_obj.__dict__
                user_obj.pop("_sa_instance_state")
                userList.append(user_obj)

            return userList

    def readOne(userEmail):
        with Session(bind = engine) as session:

            user = session.query(UserQuery.User).filter(UserQuery.User.email == userEmail)

            userList = []

            for user_obj in user:
                user_obj = user_obj.__dict__
                user_obj.pop("_sa_instance_state")
                userList.append(user_obj)

            return userList

    def update(userName, userEmail, userAge, userGender, oldUserEmail):
        with Session(bind = engine) as session:
            wasUpdated = session.query(UserQuery.User).filter(UserQuery.User.email == oldUserEmail).update({"name": userName, "email": userEmail, "age": userAge, "gender": userGender})

            session.commit()

            if (wasUpdated == 0):
                return False

            return True 

    def delete(userEmail):
        with Session(bind = engine) as session:
            wasDeleted = session.query(UserQuery.User).filter(UserQuery.User.email == userEmail).delete(synchronize_session = 'evaluate')
            session.commit()

            if (wasDeleted == 0):
                return False

            return True 
