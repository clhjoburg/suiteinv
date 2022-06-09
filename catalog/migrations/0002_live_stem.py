# Generated by Django 3.1.7 on 2021-08-14 21:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_1', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_1_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_2', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_2_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_3', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_3_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_4', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_4_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_5', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_5_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_6', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_6_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_7', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_7_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_8', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_8_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_9', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_9_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_10', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_10_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_11', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_11_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_12', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_12_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_13', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_13_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_14', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_14_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_15', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_15_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('track_16', models.FileField(default='silence.mp3', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_16_pan', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('mixed_render', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('comments', models.TextField(default='No comment', max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_project_zip', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])])),
                ('live_render', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('plug_in_1', models.URLField(blank=True)),
                ('plug_in_2', models.URLField(blank=True)),
                ('plug_in_3', models.URLField(blank=True)),
                ('plug_in_4', models.URLField(blank=True)),
                ('plug_in_5', models.URLField(blank=True)),
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