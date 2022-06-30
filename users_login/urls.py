from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings

from .forms import CustomPasswordReset, CustomPasswordSet
from .views import (
    Login,
    logoutUser,
    UserEditView
)

app_name = 'users_login'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUser), name='logout'),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),

    #-----------------------------------------------------------------------------------------------

]
