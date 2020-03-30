import uuid
from django.db import models

from  django.db  import  models, IntegrityError
from  django.contrib.auth.models  import  AbstractBaseUser, PermissionsMixin
from  django.contrib.auth.models  import  UserManager  as  _UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from  django.contrib.auth.models  import  Group
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female')
]

DOCUMENT_TYPE_CHOICES = [
    ('RG','Registro civil / NUIP'),
    ('TI','Tarjeta de identidad'),
    ('CC','Cedula de ciudadania'),
    ('CE','Cedula de extranjeria'),
    ('PA','Passport'),

]

# This model covers data about patients in health-related 
# activities. It doesn't contain PII (Personal 
# Identifiable Information):
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()


# This model covers PII information for a patient
class PatientData(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE_CHOICES)
    document_id = models.CharField(max_length=16)

# Receive data for cognito and save in user model
class CogUserManager( _UserManager ):
    def get_or_create_for_cognito ( self ,  payload ):
        cognito_id = payload[ 'sub' ]
        group =  payload[ 'cognito:groups' ] if 'cognito:groups' in payload else None
        try :
            user = self.get( cognito_id =cognito_id)   
            if group:
                new_group, created = Group.objects.get_or_create( name =group[ 0 ])
                user.groups.set([new_group])
            return  user
        except  self.model.DoesNotExist:
            pass

        try :
            user = self.create(
                    cognito_id = cognito_id,
                    email = payload[ 'email' ],
                    first_name = payload[ 'name' ] if 'name' in payload else '',
                    last_name = payload[ 'given_name' ] if 'given_name' in payload else '',
                    username = payload['cognito:username'],
                    is_active = True )
            if group:
                new_group, created = Group.objects.get_or_create( name =group[ 0 ])
                user.groups.set([new_group])
            return  user
        except  IntegrityError:
            user = self.get( cognito_id =cognito_id)
            if group:
                new_group, created = Group.objects.get_or_create( name =group[ 0 ])
                user.groups.set([new_group])
            return  user
        return  user

    # Custom command createsuperuser
    def create_superuser(self, password, username, email, **extra_fields): 
        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# custom User model for Cognito
class CogUser( AbstractBaseUser, PermissionsMixin ):
    #cognito_id = models.UUIDField(primary_key = True , default =uuid.uuid4,  editable = False )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('is superuser'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    cognito_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #USERNAME_FIELD  =  'cognito_id'
    objects = CogUserManager()