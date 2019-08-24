from django.shortcuts import render
from django.views.generic import(View,TemplateView,
                                ListView,DetailView,
                                UpdateView,CreateView,
                                DeleteView

                                )
from django.http import HttpResponse
# Create your views here.
from django.core.urlresolvers import reverse_lazy
from . import models
class lol(View):
    def get(self,request):
        return HttpResponse('lol')
class index(TemplateView):
    template_name='image.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['insert']='data is inserted using ckass base view'
        return context
class school(ListView):
    model=models.school
    #template_name='myapp/school_list.html'
class student(DetailView):
    context_object_nam='school'
    model=models.school
    template_name='myapp/student_detail.html'
class create(CreateView):
    fields=('name',)
    model=models.school
class update(UpdateView):
    fields=('name',)
    model=models.school
class delete(DeleteView):
    model=models.school
    success_url=reverse_lazy('goto:school')
