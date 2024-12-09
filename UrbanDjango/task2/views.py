from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class ClassTemplateView(TemplateView):
    template_name = 'class_template.html'

def func_template(request):
    return render(request, 'func_template.html')