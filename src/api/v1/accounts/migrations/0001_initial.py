# Generated by Django 4.2.11 on 2024-03-22 14:42

import api.v1.accounts.managers
import api.v1.accounts.services
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')),
                ('email', models.EmailField(error_messages={'unique': 'Пользователь с таким email уже существует'}, max_length=150, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания аккаунта')),
                ('sex', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], default=None, null=True, verbose_name='Пол пользователя')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('avatar', models.ImageField(default='avatars/default.png', upload_to=api.v1.accounts.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])], verbose_name='Фото профиля')),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True, verbose_name='О себе')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', api.v1.accounts.managers.CustomUserManager()),
            ],
        ),
    ]