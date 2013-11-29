from .models import Account
from django.contrib.auth.models import User

class MyCustomBackend:

    def authenticate(self, username=None, password=None):
        try:
            user = Account.objects.get(userid=username)
        except Account.DoesNotExist:
            pass
        else:
            if user.check_password(password=password):
                try:
                    django_user = User.objects.get(username=user.username)
                except User.DoesNotExist:
                    django_user = User(username=user.userid,password=user.MasPass)
                    django_user.is_staff = True
                    django_user.save()
                return django_user
            else:
                return None
 
    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None