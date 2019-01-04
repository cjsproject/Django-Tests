from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailAuth(ModelBackend):
	def authenticate(self, email=None, password=None, **kwargs):
		UserModel = get_user_model()
		if email is None:
			email = kwargs.get(CustomUser.USERNAME_FIELD)
		try:
			user = UserModel._default_manager.get_by_natural_key(email)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			UserModel().set_password(password)
"""		UserModel = get_user_model()
		email = kwargs.get(UserModel.USERNAME_FIELD)
		try:
			user = UserModel.objects.get(email)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
				Usermodel().set_password(password)
"""
"""		UserModel = get_user_model()
		if username is None:
	        username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
        	user = UserModel._default_manager.get_by_natural_key(email=username)
        	if user.check_password(password):
        		return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
"""
"""		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(email=username)
		except UserModel.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				return user
		return None
"""