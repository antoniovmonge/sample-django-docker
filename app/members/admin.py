# app/members/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Member


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "position",
        "fun_fact",
        "created_date",
        "updated_date",
    )

    list_display = (
        "name",
        "position",
        "fun_fact",
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )
