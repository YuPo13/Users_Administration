from users.models import UserProfile
from django.contrib.auth.models import User


def run():

    new_admin_username = input("Please provide email for new admin: ")
    new_admin_password = input("Please provide password for new admin: ")
    new_admin_password_repeated = input("Please repeat the same password again: ")

    if not User.objects.filter(username=new_admin_username):

        if new_admin_password == new_admin_password_repeated:
            new_admin = User()
            new_admin.is_superuser = True
            new_admin.is_staff = True
            new_admin.username = new_admin_username
            new_admin.set_password(new_admin_password)
            new_admin.save()
            UserProfile.user_manager.create(user=new_admin)
            print("New admin has been created")

            return new_admin

        else:
            print("The passwords entered do not match. Start over again.")

    else:
        print("The username provided is already in use. Start over again.")

    return None
