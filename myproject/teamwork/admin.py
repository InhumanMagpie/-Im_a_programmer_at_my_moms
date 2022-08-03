from django.contrib import admin
from .models import User, Team, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {"fields": ("username", "password")}),
    #     (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    #     (
    #         _("Permissions"),
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #             ),
    #         },
    #     ),
    # )
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass