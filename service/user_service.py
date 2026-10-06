import datetime

from model.user import User
from data_access.user_data_managment import UserDataManager


class UserService:
    def __init__(self):
        self.__user_data_management = UserDataManager()

    def save_User(self, user: User):
        # checking user saving Business logic
        print("==== BUSINESS RULE =====")
        age = int((datetime.date.today() - user.birth_date).days / 365)

        if user.role == "clerk" and (40 < age or age < 20):
            raise ValueError("unfortunately you cant be clerk : age must be 20 to 40")

        users = self.__user_data_management.get_all_users()
        is_user_exist = list(filter(lambda saved_user: saved_user.national_code == user.national_code, users))
        if is_user_exist:
            raise ValueError("user with national_code already exist")

        self.__user_data_management.save_user(user)

    def get_all_users(self):
        # checking user saving Business logic
        print("==== BUSINESS RULE =====")

        users = self.__user_data_management.get_all_users()
        return users

    def edite_user(self, user: User):
        print("==== BUSINESS RULE =====")
        # self.__user_data_management.find_by_name_update(user , user.name)

        age = int((datetime.date.today() - user.birth_date).days / 365)
        
        if user.role == "clerk" and (40 < age or age < 20):
            raise ValueError("unfortunately you cant be clerk : age must be 20 to 40")

        users = self.__user_data_management.get_all_users()
        users = list(filter(lambda saved_user: saved_user.national_code != user.national_code, users))
        users.append(user)
        self.__user_data_management.save_users(users)

    def delete_user(self, national_code):
        print("==== BUSINESS RULE =====")
        users = self.__user_data_management.get_all_users()
        users = list(filter(lambda saved_user: saved_user.national_code != national_code, users))
        self.__user_data_management.save_users(users)
