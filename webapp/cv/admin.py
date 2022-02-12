from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AboutMe)
admin.site.register(PrimaryInfo)
admin.site.register(EdicationalDetail)
admin.site.register(WorkHistoryDetail)
admin.site.register(Languages)
admin.site.register(Software)
admin.site.register(Skills)
admin.site.register(CoWorksers)
admin.site.register(Courses)
admin.site.register(Projects)
admin.site.register(BooksandArticles)
admin.site.register(Contact)
admin.site.register(pic)


admin.site.register(CV)