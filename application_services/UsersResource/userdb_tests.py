from application_services.UsersResource.user_service import UserResource


def t1():
    res = UserResource.get_users_and_addresses()

    print(res)

t1()