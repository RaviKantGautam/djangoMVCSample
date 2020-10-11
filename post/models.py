from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse
from django.core.validators import EmailValidator

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES_CHOICE = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLES_CHOICE = sorted([(item,item) for item in get_all_styles()])


# Create your models here.
class Snippet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100,blank=True,default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(max_length=250,choices=LANGUAGES_CHOICE,default='python')
	style = models.CharField(max_length=250,choices=STYLES_CHOICE,default='friendly')

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.language

	def get_absolute_url(self):
		return reverse('post:demo',kwargs={'pk':self.pk})


class UserManager(BaseUserManager):
	def create_user(self,email,password=None):
		if not email:
			return ValueError('Emial is must')
		user = self.models(email=self.normalize_email(email))
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_staff(self,email,password):
		user = self.create_user(email,password)
		user.is_staff = True
		user.save(using=self._db)
		return user
	def create_superuser(self,email,password):
		user = self.create_user(email,password)
		user.is_superuser = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(validators=[EmailValidator])
	name = models.CharField(max_length=100)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		return self.name

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True

	@property
	def is_client(self):
		return self.client

	@property
	def is_staff(self):
		return self.staff
