from django.db import models

# Create your models here.

gender = (

    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Nothing', 'Nothing'),
)

martial_status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
)

military_service_status = (
    ('Educational Exemption', 'Educational Exemption'),
    ('Exempted', 'Exempted'),
    ('Completed', 'Completed'),
    ('Ongoing', 'Ongoing'),
    ('Not served yet', 'Not served yet')
)

job_category = (
    ('Administration, business and management', 'Administration, business and management'),
    ('Alternative therapies', 'Alternative therapies'),
    ('Animals, land and environment', 'Animals, land and environment'),
    ('Computing and ICT', 'Computing and ICT'),
    ('Construction and building', 'Construction and building'),
    ('Design, arts and crafts', 'Design, arts and crafts'),
    ('Education and training', 'Education and training'),
    ('Engineering', 'Engineerin'),
    ('Facilities and property services', 'Facilities and property services'),
    ('Financial services', 'Financial services'),
    ('Garage services', 'Garage services'),
    ('Hairdressing and beauty', 'Hairdressing and beauty'),
    ('Healthcare', 'Healthcare'),
    ('Heritage, culture and libraries', 'Heritage, culture and libraries'),
    ('Hospitality, catering and tourism', 'Hospitality, catering and tourism'),
    ('Languages', 'Languages'),
    ('Legal and court services', 'Legal and court services'),
    ('Manufacturing and production', 'Manufacturing and production'),
    ('Performing arts and media', 'Performing arts and media'),
    ('Print and publishing, marketing and advertising', 'Print and publishing, marketing and advertising'),
    ('Retail and customer services', 'Retail and customer services'),
    ('Science, mathematics and statistics', 'Science, mathematics and statistics'),
    ('Security, uniformed and protective services', 'Security, uniformed and protective services'),
    ('Social sciences and religion', 'Social sciences and religion'),
    ('Social work and caring services', 'Social work and caring services'),
    ('Sport and leisure', 'Sport and leisure'),
    ('Transport, distribution and logistics', 'Transport, distribution and logistics')
)

degree = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('Doctorate', 'Doctorate')
)

degree_status = (
    ('Studing', 'Studing'),
    ('Finished', 'Finished')
)

work_status = (
    ('Working', 'Working'),
    ('Finished', 'Finished')
)

software_level = (
    ( 'Trainee developer ', ' Trainee developer '),
    ( 'Junior developer ', ' Junior developer '),
    ( 'Mid-level developer ', ' Mid-level developer '),
    ( 'Senior developer ', ' Senior developer '),
    ( 'Leader ', ' Leader ')

)

class AboutMe(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    about = models.CharField(max_length=500)
    picture = models.ImageField()

    def __str__(self):
        return self.first_name + self.last_name + " " + self.job_title

class PrimaryInfo(models.Model):
    first_name = models.ForeignKey(AboutMe, related_name='f_name', on_delete=models.CASCADE)
    last_name = models.ForeignKey(AboutMe, related_name='l_name', on_delete=models.CASCADE)
    gender = models.CharField(choices=gender, max_length=150)
    marital_status = models.CharField(choices=martial_status, max_length=150)
    military_service_status = models.CharField(choices=military_service_status, max_length=150)
    country = models.CharField(max_length=150)
    convince = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    date_of_birth = models.DateTimeField()
    expected_salary = models.IntegerField()
    job_category = models.CharField(choices=job_category, max_length=150)

    def __str__(self):
        return self.first_name.first_name + ' ' + self.last_name.last_name

class EdicationalDetail(models.Model):
    degree = models.CharField(choices=degree, max_length=150)
    field = models.CharField(max_length=200)
    status = models.CharField(choices=degree_status, max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.degree
    

class WorkHistoryDetail(models.Model):
    job_category = models.CharField(choices=job_category, max_length=150)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=work_status, max_length=150)

    def _str__(self):
        return self.title

class Languages(models.Model):
    language = models.CharField(max_length=150)
    level = models.IntegerField()

    def __Str__(self):
        return self.language

class Software(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(choices=software_level, max_length=150)

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class CoWorksers(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Courses(models.Model):
    title = models.CharField(max_length=150)
    length = models.IntegerField()
    date = models.DateField()
    ink = models.CharField(max_length=150)

    def __Str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=200)
    data = models.DateTimeField()
    length = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class BooksandArticles(models.Model):
    title = models.CharField(max_length=200)
    data = models.DateTimeField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(max_length=64)
    number = models.IntegerField() 

    def __Str__(self):
        return self.email + ' ' + self.number



class CV(models.Model):
    title = models.CharField(max_length=150)
    about = models.OneToOneField(AboutMe, on_delete=models.CASCADE)
    info = models.OneToOneField(PrimaryInfo, on_delete=models.CASCADE)
    education = models.ManyToManyField(EdicationalDetail)
    works = models.ManyToManyField(WorkHistoryDetail)
    languages = models.ManyToManyField(Languages)
    softwares = models.ManyToManyField(Software)
    skills = models.ManyToManyField(Skills)
    cowork = models.ManyToManyField(CoWorksers)
    cources = models.ManyToManyField(Courses)
    projects = models.ManyToManyField(Projects)
    articles = models.ManyToManyField(BooksandArticles)
    contacs = models.ManyToManyField(Contact)

    def __str__(self):
        return self.title