from datetime import date

from model.user import User

person1 = User("mohammd hsoein", "ghasemi", "0022613013", date(2000, 1, 20), "09026464308", "moh8998",
               "Mo123456", "clerk", False)

print(person1)
person1.set_password("Mo654321")
print(person1)