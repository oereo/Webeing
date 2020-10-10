# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, nickname, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            nickname=nickname,
            phone_number=phone_number,
            # phoneNumber = phoneNumber,
        )
        user.is_seller = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_seller(self, email, business_number, seller_address, seller_name, phone_number, nickname, date_of_birth,
                      password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            nickname=nickname,
            phone_number=phone_number,
            seller_address=seller_address,
            business_number=business_number,
            seller_name=seller_name,
            # is_seller = is_seller,
            # phoneNumber = phoneNumber,
        )
        user.is_seller = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, nickname, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            nickname=nickname,
            phone_number=phone_number,
            # phoneNumber = phoneNumber,

        )
        user.is_seller = False
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    phone_number = models.CharField(max_length=14, null=False, unique=True)
    date_of_birth = models.DateField()
    business_number = models.CharField(max_length=30, null=True, unique=True)
    seller_address = models.CharField(max_length=30, null=True, unique=True)
    seller_name = models.CharField(max_length=30, null=True, unique=True)

    # phoneNumber = PhoneNumberField(_("phoneNumber"),null=False, blank = False, unique = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(null=True, default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'nickname', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# class normalUser
