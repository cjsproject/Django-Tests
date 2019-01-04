from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username',]
admin.site.register(CustomUser, CustomUserAdmin) 
"""	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
		)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
			}),
		)
	list_display = ('email', 'first_name', 'last_name', 'is_staff')
	searh_fields = ('email', 'first_name', 'last_name')
	ordering = ('email',)
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
"""