from flask import Flask, request
app = Flask(__name__)

from controllers import HomeController, UserController

# Index
@app.route("/")
def index():
    return HomeController.HomeController.index(request)

#  User 
@app.route("/user", methods = ['POST'])
def userCreate():
    return UserController.UserController.create(request)

@app.route("/users")
def userReadAll():
    return UserController.UserController.readAll(request)    

@app.route("/user/<string:userEmail>")
def userReadOne(userEmail):
    return UserController.UserController.readOne(request, userEmail)

@app.route("/user", methods = ['PUT'])
def userUpdate():
    return UserController.UserController.update(request)

@app.route("/user", methods = ['DELETE'])
def userDelete():
    return UserController.UserController.delete(request)

if __name__ == "__main__":
    print('Server is up!')
    app.run(debug = True)
