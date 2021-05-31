from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'webapp/index.html'
    # @method_decorator(ensure_csrf_cookie)
    # def get(self, request, *args, **kwargs):
    #     return render(request, 'webapp/index.html')
