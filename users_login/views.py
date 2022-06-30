from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout  
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth import get_user_model

from .forms import FormularioLogin
from .forms import CustomUpdateForm


User = get_user_model()


class Login(FormView):
    template_name = 'login_logout/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)



#_________________________________________________________________________________________________________________________

class UserEditView(generic.UpdateView):
    form_class = CustomUpdateForm
    template_name = 'login_logout/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


#________________________________________________________________________________________________________________________________
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_login:login'))
