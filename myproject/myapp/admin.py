from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myapp.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'is_active', 'is_admin')

# Register the User model with the custom UserModelAdmin
# admin.site.register(User, UserModelAdmin)