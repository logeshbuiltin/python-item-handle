import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

dataBaseFile = "DataFile.db"

class userRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type=str,
        required=True,
        help="Username field can not be empty"
    )
    parser.add_argument("password",
        type=str,
        required=True,
        help="Username field can not be empty"
    )

    def post(self):
        data = userRegister.parser.parse_args()

        nameUser = data["username"]

        user = UserModel.find_by_username(nameUser)

        if user:
            return ("message", f"{nameUser} already exists in the database"), 205
        else:
            user = UserModel(**data)
            user.save_to_db()
            return {'message': f"{nameUser} has been created successfully"}, 201
            
            
        
            