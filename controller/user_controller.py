from datetime import datetime
import jdatetime
from model.user import User
from service.user_service import UserService


class UserControl:
    def __init__(self):
        self.__user_service = UserService()
    def make_new_user(self , user):
        (name, family, national_code, birth_date, phone_number, user_name, password, role, locked) = user.values()
        birth_date = jdatetime.datetime.strptime(birth_date, '%Y-%m-%d').date().togregorian()
        new_user = User(name, family, str(national_code), birth_date, str(phone_number), user_name, password, role,
                        bool(locked))
        return new_user
    def save_user(self, user):
        try:
            new_user = self.make_new_user(user)
            self.__user_service.save_User(new_user)
            return True, f"user {new_user.name} {new_user.family} saved successfully"
        except Exception as e:
            return False, e

    def get_all_user(self):
        try:
            users = self.__user_service.get_all_users()
            return True, users
        except Exception as e:
            print(f"error in get_all_user : {e}")
            return False, e

    def edite_user(self, user):
        try:
            print("========== controller ==========")
            new_user = self.make_new_user(user)

            self.__user_service.edite_user(new_user)
            return True, f"user {new_user.name} {new_user.family} edited successfully"
        except Exception as e:
            print(f"error in editing user : {e}")
            return False, e

    def delete_user(self , national_code : str):
        try:
            print("========== controller ==========")
            self.__user_service.delete_user(national_code)
            return True , f"user with national code : {national_code} deleted successfully"
        except Exception as e:
            return False, e

