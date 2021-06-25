from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="This field can not be left blank")
    parser.add_argument('password',type=str,required=True,help="This field can not be left blank")

    def post(self):
        print('in post')
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : "A user with this username is already exists"}, 400

        user = UserModel(**data)    # UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message" : "User created Successfully"}, 201
