# import the User object
from django.contrib.auth.models import check_password
from django.contrib.auth.models import User

from home.models import *



class StaffBackend:
    # Create an authentication method
    # This is called by the standard Django login procedure
    def authenticate(self, username=None, password=None):

        try:
            # Try to find a user matching your username
            user = Staff.objects.get(username=username)
            #  Check the password is the reverse of the username
            if check_password(password,user.password):
                # Yes? return the Django user object
               if user.is_active:
                    return user
            else:
                # No? return None - triggers default login failed
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None

