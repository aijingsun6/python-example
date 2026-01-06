class User:
    pass
class BasicUser(User):
    pass
class ProUser(User):
    pass
class TeamUser(User):
    pass

def new_user[U: User](user_class: type[U]) -> U:
    return user_class()

a = new_user(BasicUser)
print(a)