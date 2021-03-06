# Generated by Django 4.0.2 on 2022-02-12 18:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0003_alter_aboutme_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='owner',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='archivos')),
                ('owner', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.picture'),
        ),
    ]
