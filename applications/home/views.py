from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home/panel.html'
    login_url = ('users_app:login')


class DateMixin(object):

    def get_context_data(self, **kwargs):
        context = super(DateMixin, self).get_context_data(**kwargs)
        context['date'] = datetime.now()
        return context


class TestPage(DateMixin, TemplateView):
    template_name = 'home/test.html'
