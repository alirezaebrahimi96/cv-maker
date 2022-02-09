from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import AboutMe, PrimaryInfo, Projects, Skills, Software, Languages, Courses, Contact, CoWorksers, WorkHistoryDetail, EdicationalDetail, Show
from .forms import AboutMeForm, PrimaryInfoForm, ProjectsForm, SkillsForm, SoftwareForm, LanguagesForm, CoursesForm, ContactForm, CoWorksersForm, WorkHistoryDetailForm, EdicationalDetailForm, ShowForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, 'index.html')

