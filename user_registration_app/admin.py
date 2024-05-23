from django.contrib import admin
from .models import Registration
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    admin.site.site_header = "Registration Admin Page"
    model = Registration
    list_display = ("username","email","date_joined","last_login","is_active")
    list_filter = ("is_staff", "is_active","is_superuser")
    fieldsets = (
        ("User Details", {"fields": ("first_name","last_name","email","Mobile","Date_of_birth","gender","Userimg","Address","slug")}),
        ("Authentiction Details", {"fields": ("username","password")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_superuser","groups", "user_permissions")}),
        ("Important Dates", {"fields": ("date_joined","Updated_date","last_login")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1","password2","is_staff","is_active")}
        ),
    )
    readonly_fields = ("Updated_date","date_joined","last_login",)
    search_fields = ("email","mobile",)
    ordering = ("date_joined",)
    prepopulated_fields = {"slug": ("username",)}

admin.site.register(Registration, CustomUserAdmin)

