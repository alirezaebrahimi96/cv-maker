from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import AboutMe, PrimaryInfo, Projects, Skills, Software, Languages, Courses, Contact, CoWorksers, WorkHistoryDetail, EdicationalDetail, Show
from .forms import AboutMeForm, PictureForm, PrimaryInfoForm, ProjectsForm, SkillsForm, SoftwareForm, LanguagesForm, CoursesForm, ContactForm, CoWorksersForm, WorkHistoryDetailForm, EdicationalDetailForm, ShowForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
    
class pic(LoginRequiredMixin, FormView):
    template_name = 'pic.html'
    form_class = PictureForm
    success_url = '/aboutme/'
    fields = '__all__' 
    def form_valid(self, form):
        form.save()
        return super(pic, self).form_valid(form)
class aboutme(LoginRequiredMixin, FormView):
    template_name = 'aboutme.html'
    form_class = AboutMeForm
    success_url = '/'
    fields = '__all__' 
    def form_valid(self, form):
        form.save()
        return super(aboutme, self).form_valid(form)