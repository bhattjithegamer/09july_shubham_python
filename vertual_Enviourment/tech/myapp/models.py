from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class user(AbstractBaseUser):
    admin = 'admin'
    user = 'user'
    role_choice = [
        ('admin','admin'),
        ('user','user'),
    ]
    role = models.CharField(max_length=10 ,choices = role_choice,default=user)
    email = models.EmailField(unique = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    

class task(models.Model):
    status_choices = [
        ('pending','pending'),
        ('inprogress','inprogress'),
        ('completed','completed'),
    ]
    title = models.CharField(max_length=200)
    des = models.TextField(max_length=20)
    status = models.CharField(max_length=30,choices=status_choices,default = 'pending')

    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(user,on_delete=models.CASCADE,related_name='tasks')
    attchment = models.FileField(upload_to='task_files/',null=True , blank=True)
    def __str__(self):
        return self.title