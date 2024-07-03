from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model
from myapp.models import Fruit
from myapp.models import Meal




User = get_user_model()
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'is_active', 'is_admin')

# Register the User model with the custom UserModelAdmin
# admin.site.register(User, UserModelAdmin)
admin.site.register(Fruit)
admin.site.register(Meal)
