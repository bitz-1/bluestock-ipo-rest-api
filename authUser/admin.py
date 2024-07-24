from django.contrib import admin
from authUser.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserModelAdmin(BaseUserAdmin):
   
    list_display = ["email", "name", "tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
   
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name" , "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
