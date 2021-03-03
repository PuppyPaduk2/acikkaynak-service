# Generated by Django 3.1.7 on 2021-03-03 22:41

import app.common.types
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('iso_code', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator()])),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator()])),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('iso_code', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator()])),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator()])),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator()])),
                ('country', models.ForeignKey(db_column='country_uuid', on_delete=django.db.models.deletion.RESTRICT, related_name='cities', to='common.country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=255, null=True, unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.MinLengthValidator(2)], verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('gender', models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')], default=app.common.types.Genders['OTHER'], max_length=255, verbose_name='gender')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.EmailValidator()], verbose_name='e-mail')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='phone')),
                ('profile_picture_uri', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()], verbose_name='profile picture uri')),
                ('locale', models.CharField(default='tr-tr', max_length=255, verbose_name='locale')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
