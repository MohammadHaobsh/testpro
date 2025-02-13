from django.urls import path
from .views import login_page, logout_view, register_page, dashboard, add_employee

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-employee/', add_employee, name='add_employee'),
]
