from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee

class EmployeeAdmin(UserAdmin):
    model = Employee
    list_display = ['id', 'username', 'email', 'phone', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'phone']

admin.site.register(Employee, EmployeeAdmin)
