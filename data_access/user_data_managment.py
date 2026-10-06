import os.path
import pickle
from typing import List
from model.user import User
from os import path


class UserDataManager:
    def __init__(self):
        self.file_name = "user.date"
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__user_list = pickle.load(file)
            file.close()
        else:
            file = open(self.file_name, "wb")
            pickle.dump([], file)
            self.__user_list = []

    def save_user(self, user: User):

        self.__user_list.append(user)
        file = open(self.file_name, "wb")
        pickle.dump(self.__user_list, file)
        file.close()
        print("user save successfully")

    def save_users(self , users: List[User]):
        self.__user_list = users
        file = open(self.file_name, "wb")
        pickle.dump(self.__user_list, file)
        file.close()
        print("user save successfully")

    def get_all_users(self):
        file = open(self.file_name, "rb")
        self.__user_list = pickle.load(file)
        file.close()
        return self.__user_list


