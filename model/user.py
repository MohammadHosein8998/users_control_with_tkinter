import jdatetime
from persian_tools import national_id, phone_number as phone_num
from datetime import date


class User:
    def __init__(self, name: str, family: str, national_code: str, birth_date: date, phone_number: str, user_name: str,
                 password: str, role: str, locked: bool = False):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.user_name = user_name
        self.password = password
        self.locked = locked
        self.role = role

    # Name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("name cant be empty")
        self.__name = name

    name = property(get_name, set_name)

    # Family
    def get_family(self):
        return self.__family

    def set_family(self, family):
        if not family:
            raise ValueError("family cant be empty")
        self.__family = family

    family = property(get_family, set_family)

    # National code
    def get_national_code(self):
        return self.__national_code

    def set_national_code(self, national_code):
        if not national_id.validate(national_code):
            raise ValueError(f"national_id {national_code} is not valid")
        self.__national_code = national_code

    national_code = property(get_national_code, set_national_code)

    # Birth date
    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        if not isinstance(birth_date, date):
            raise ValueError(f"birth_date must be an date object !!!")
        elif birth_date > date.today():
            raise ValueError("your birth day cant be future")
        elif (date.today() - birth_date).days / 365 < 18:
            raise ValueError(
                f"you must be at least be 18 year old , you are {int((date.today() - birth_date).days / 365)}")
        self.__birth_date = birth_date

    birth_date = property(get_birth_date, set_birth_date)

    # Phone number
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        if not phone_num.validate(phone_number):
            raise ValueError(f"phone number is not valid !!!")
        self.__phone_number = phone_num.normalize(phone_number)

    phone_number = property(get_phone_number, set_phone_number)

    # UserName
    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    user_name = property(get_user_name, set_user_name)

    # Password
    def set_password(self, password):
        self.__password = password

    password = property(None, set_password)

    # Locked

    def get_locked(self):
        return self.__locked

    def set_locked(self, locked=True):
        if not isinstance(locked, bool):
            raise ValueError("locked must be True or False")
        self.__locked = locked

    locked = property(get_locked, set_locked)

    # Role
    def get_role(self):
        return self.__role

    def set_role(self, role):
        if not role in ["client", "clerk"]:
            raise ValueError("role must be client or clerk")
        self.__role = role

    role = property(get_role, set_role)

    # casting to tuple
    def to_tuple(self):
        # casting time from milady to shamsi
        persian_date = jdatetime.datetime.fromgregorian(
            date=self.birth_date
        )
        string_persian = jdatetime.datetime.strftime(persian_date, '%Y-%m-%d')
        return self.name , self.family , self.national_code, string_persian, self.phone_number, self.user_name, self.role , self.locked

    def __repr__(self) -> str:
        return f"User(name : {self.name} , family:{self.family},  national code:{self.national_code}, birth date:{self.birth_date}, phone number:{self.phone_number}, user name:{self.user_name}, locked:{self.locked})"
