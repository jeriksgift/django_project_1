from django.contrib import admin
from .models import Members
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "phone")

admin.site.register(Members, MemberAdmin)