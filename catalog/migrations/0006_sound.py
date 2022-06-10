# Generated by Django 3.1.7 on 2022-06-10 06:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_auto_20220609_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound_file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('comments', models.TextField(default='No comment', max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
