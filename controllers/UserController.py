import json
from flask import jsonify

from models import UserModel

class UserController:

    def alreadyExist(userEmail):
        resp = UserModel.UserModel.readOne(userEmail)

        if(len(resp) > 0):
            return True
        
        return False

    def create(request):
        userName = (json.loads(request.data)).get('name')
        userEmail = (json.loads(request.data)).get('email')
        userAge = (json.loads(request.data)).get('age')
        userGender = (json.loads(request.data)).get('gender')

        if (userName) is None: 
            return { "message": "Campo nome de usuário é obrigatório" }, 400
        
        if (userEmail) is None: 
            return { "message": "Campo e-mail de usuário é obrigatório" }, 400

        if (userAge) is None: 
            return { "message": "Campo idade de usuário é obrigatório" }, 400

        if (userGender) is None: 
            return { "message": "Campo sexo de usuário é obrigatório" }, 400

        if type(userName) is not str: 
            return { "message": "Parâmetro userName deve ser do tipo string" }, 400

        if type(userEmail) is not str: 
            return { "message": "Parâmetro userEmail deve ser do tipo string" }, 400

        if type(userAge) is not int: 
            return { "message": "Parâmetro userAge deve ser do tipo integer" }, 400

        if type(userGender) is not str: 
            return { "message": "Parâmetro userGender deve ser do tipo string" }, 400

        userName = " ".join(userName.split())
        userEmail = " ".join(userEmail.split())
        userAge = userAge.strip()
        userGender = " ".join(userGender.split())

        resp = UserController.alreadyExist(userEmail)

        if(resp):
            return { "message": "Usuário já cadastrado na base de dados!" }

        UserModel.UserModel.create(userName, userEmail, userAge, userGender)

        return { "message": "Usuário criado com sucesso!" }

    def readAll(request): 
        user = UserModel.UserModel.readAll()

        if (len(user) == 0):
            return { "message": "Não há usuários cadastrados na base de dados!" }

        return jsonify(user)

    def readOne(request, userEmail):
        user = UserModel.UserModel.readOne(userEmail)

        if (len(user) == 0):
            return { "message": "Usuário não encontrado na base de dados!" }, 404

        return jsonify(user[0])

    def update(request):
        userName = (json.loads(request.data)).get('name')
        userEmail = (json.loads(request.data)).get('email')
        userAge = (json.loads(request.data)).get('age')
        userGender = (json.loads(request.data)).get('gender')
        oldUserEmail = (json.loads(request.data)).get('oldUserEmail')

        if (userName) is None: 
            return { "message": "Campo nome de usuário é obrigatório!" }, 400
        
        if (userEmail) is None: 
            return { "message": "Campo e-mail de usuário é obrigatório!" }, 400

        if (userAge) is None: 
            return { "message": "Campo idade de usuário é obrigatório!" }, 400

        if (userGender) is None: 
            return { "message": "Campo sexo de usuário é obrigatório!" }, 400

        if (oldUserEmail) is None: 
            return { "message": "Campo antigo email de usuário é obrigatório!" }, 400

        if type(userName) is not str: 
            return { "message": "Parâmetro userName deve ser do tipo string!" }, 400

        if type(userEmail) is not str: 
            return { "message": "Parâmetro userEmail deve ser do tipo string!" }, 400

        if type(userAge) is not int: 
            return { "message": "Parâmetro userAge deve ser do tipo integer!" }, 400

        if type(userGender) is not str: 
            return { "message": "Parâmetro userGender deve ser do tipo string!" }, 400

        if type(oldUserEmail) is not str: 
            return { "message": "Parâmetro oldUserEmail deve ser do tipo string!" }, 400

        userName = " ".join(userName.split())
        userEmail = " ".join(userEmail.split())
        userAge = userAge.strip()
        userGender = " ".join(userGender.split())

        resp = UserController.alreadyExist(oldUserEmail)

        if (resp == False): 
            return { "message": "Usuário não encontrado na base de dados!" }, 404

        resp = UserController.alreadyExist(userEmail)

        if (resp == True):
            return { "message": "Novo e-mail já foi cadastrado na base de dados!" }, 406

        wasUpdated = UserModel.UserModel.update(userName, userEmail, userAge, userGender, oldUserEmail)

        if (wasUpdated == False):
            return { "message": "Erro ao tentar fazer update. Contate o suporte!" }

        return { "message": "Usuário atualizado com sucesso!" }

    def delete(request):
        userEmail = (json.loads(request.data)).get('email')

        if (userEmail) is None: 
            return { "message": "Campo e-mail de usuário é obrigatório" }, 400

        if type(userEmail) is not str: 
            return { "message": "Parâmetro userEmail deve ser do tipo string" }, 400

        userEmail = " ".join(userEmail.split())

        resp = UserController.alreadyExist(userEmail)

        if (resp == False): 
            return { "message": "Usuário não encontrado na base de dados!" }, 404

        wasDeleted = UserModel.UserModel.delete(userEmail)

        if (wasDeleted == False):
            return { "message": "Erro ao deletar o usuário. Contate o suporte!" }

        return { "message": "Usuário deletado com sucesso!" }
