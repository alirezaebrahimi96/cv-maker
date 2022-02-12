from django import forms

from .models import AboutMe, pic, PrimaryInfo, Projects, Skills, Software, Languages, Courses, Contact, CoWorksers, WorkHistoryDetail, EdicationalDetail, Show


class PictureForm(forms.ModelForm):
    class Meta:
        model = pic
        fields =['picture']
class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields =['first_name', 'last_name', 'job_title', 'about']
        widgets = {'about': forms.Textarea(attrs={'cols':80})}


class PrimaryInfoForm(forms.ModelForm):
    class Meta:
        model = PrimaryInfo
        fields = '__all__'


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {'explation': forms.Textarea(attrs={'cols':80})}

class PromaryInfoForm(forms.ModelForm):
    class Meta:
        model = PrimaryInfo
        fields = '__all__'

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'


class CoWorksersForm(forms.ModelForm):
    class Meta:
        model = CoWorksers
        fields = '__all__'


class WorkHistoryDetailForm(forms.ModelForm):
    class Meta:
        model = WorkHistoryDetail
        fields = '__all__'


class EdicationalDetailForm(forms.ModelForm):
    class Meta:
        model = EdicationalDetail
        fields = '__all__'

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

