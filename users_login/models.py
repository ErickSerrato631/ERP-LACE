from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None):
        if not email:
            raise ValueError(
                'Usuarios debe de contar con una dirección de correo electrónico')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.signup_confirmation = True

        user.save(using=self._db)
        return user

#------------------MainContactData Model-------------------------


class Department(models.Model):
    department = models.CharField(
        verbose_name='Departamento',
        max_length=50,
    )

    class Meta:
        db_table = 'Departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return str(self.department)



class CustomUser(AbstractBaseUser):
    id_contact = models.AutoField(primary_key=True)

    first_name = models.CharField(
        verbose_name='Nombre',
        max_length=45,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        verbose_name='Apellidos',
        max_length=25,
        blank=True,
        null=True
    )

    email = models.CharField(
        verbose_name='Correo Electrónico',
        unique=True,
        max_length=50,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name='Télefono',
        max_length=20,
        blank=True,
        null=True
    )

    password = models.CharField(
        verbose_name='Contraseña',
        max_length=128,
        blank=True,
        null=True,
    )

    id_department = models.ForeignKey(
        Department,
        on_delete = models.CASCADE,
        verbose_name = "Departamento",
        null=True,
    )

    workstation = models.CharField(
        verbose_name='puesto de trabajo',
        max_length=128,
        blank=True,
        null=True,
    )

    attendance = models.DateTimeField(
        verbose_name='Horario de entrada',
        auto_now=True,
    )

    is_admin = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    signup_confirmation = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name', ]

    class Meta:
        db_table = 'Usuario'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """¿El usuario tiene permisos específicos?"""
        return True

    def has_module_perms(self, app_label):
        """¿El usuario tiene permisos para visitar la app 'app_label'?"""
        return True

    @property
    def isStaff(self):
        """¿El usuario es miembro del staff?"""
        return self.is_admin

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Envía un correo a este usuario"""
        send_mail(subject, message, from_email, [self.email], **kwargs)
