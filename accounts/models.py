from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create(self, email, is_active=True, is_staff=False, is_admin=False, password=None):
        if not email:
            raise ValueError("email address is required")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, password=None):
        user_obj = self.create(
            email,
            password=password,
            is_staff=True
        )
        return user_obj
    
    def create_superuser(self, email, password=None):
        user_obj = self.create(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user_obj
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    @property
    def get_email(self):
        return self.email
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        return super().has_module_perms(app_label)
    


# Create your models here.
