from django import forms

from .models import AboutMe, PrimaryInfo, Projects, Skills, Software, Languages, Courses, Contact, CoWorksers, WorkHistoryDetail, EdicationalDetail, Show

class AboutMeForm(forms.Form):
    class Meta:
        model = AboutMe
        fields =['first_name', 'last_name', 'job_title', 'picture', 'about']
        widgets = {'about': forms.Textarea(attrs={'cols':80})}


class PrimaryInfoForm(forms.Form):
    class Meta:
        model = PrimaryInfo
        fields = '__all__'


class ProjectsForm(forms.Form):
    class Meta:
        model = Projects
        fields = '__all__'


class SkillsForm(forms.Form):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {'explation': forms.Textarea(attrs={'cols':80})}

class PromaryInfoForm(forms.Form):
    class Meta:
        model = PrimaryInfo
        fields = '__all__'

class SoftwareForm(forms.Form):
    class Meta:
        model = Software
        fields = '__all__'


class LanguagesForm(forms.Form):
    class Meta:
        model = Languages
        fields = '__all__'


class CoursesForm(forms.Form):
    class Meta:
        model = Courses
        fields = '__all__'


class CoWorksersForm(forms.Form):
    class Meta:
        model = CoWorksers
        fields = '__all__'


class WorkHistoryDetailForm(forms.Form):
    class Meta:
        model = WorkHistoryDetail
        fields = '__all__'


class EdicationalDetailForm(forms.Form):
    class Meta:
        model = EdicationalDetail
        fields = '__all__'

class ShowForm(forms.Form):
    class Meta:
        model = Show
        fields = '__all__'


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = '__all__'

