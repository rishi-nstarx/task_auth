from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # Add or modify forms if you have custom forms, otherwise you can use the default
    # form = CustomUserChangeForm
    # add_form = CustomUserCreationForm

    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()  # Empty tuple since we don't have 'groups' or 'user_permissions'

# Unregister the Group model if you don't use it with CustomUser
admin.site.unregister(Group)

admin.site.register(CustomUser, CustomUserAdmin)
