from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class AdvUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50)
    last_name = models.CharField(max_length=12, verbose_name="Фамилия", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Фамилия введена не правильно',
                       code='invalid_last_name'), ])
    first_name = models.CharField(max_length=12, verbose_name="Имя", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Имя введено не правильно',
                       code='invalid_first_name'), ])
    middle_name = models.CharField(max_length=12, verbose_name="Отчество", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Отвество введено не правильно',
                       code='invalid_middle_name'), ])
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь'), ('author', 'Автор')),
                            default='user')
    username = models.CharField(max_length=20, verbose_name="Имя пользователя", unique=True, validators=[
        RegexValidator(regex=r'^[a-z]+$', message='Имя пользователя введено не правильно',
                       code='invalid_username'), ])

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    def is_author(self, bb):
        if self.pk == bb.author.pk:
            return True
        return False

    class Meta(AbstractUser.Meta):
        pass