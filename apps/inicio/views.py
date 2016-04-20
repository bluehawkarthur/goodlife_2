from django.shortcuts import render
from django.views.generic import TemplateView, FormView, RedirectView
from .forms import LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Inicio(TemplateView):
  template_name = 'inicio/index.html'


class Main(TemplateView):
  template_name = 'inicio/main.html'

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
      return super(Main, self).dispatch(*args, **kwargs)



class LoginView(FormView):
    form_class = LoginForm
    template_name = "inicio/login.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'index'
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)