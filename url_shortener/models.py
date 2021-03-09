from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from random import choice
import string

# from urllib3 import PoolManager

User = get_user_model()


def generate_short_url():
    chars = string.digits + string.ascii_letters
    return ''.join(choice(chars) for _ in range(7))


class ShortLink(models.Model):
    user = models.ForeignKey(User, related_name='Short_Links', null=True, blank=True, on_delete=models.SET_NULL)
    long_url = models.CharField(verbose_name='Long URL', max_length=200,unique=True)
    short_url = models.CharField(default=generate_short_url, verbose_name='Short URL', unique=True, max_length=200)
    last_validation = models.DateTimeField(default=timezone.now, verbose_name='Last Validation')
    is_broken = models.BooleanField(default=False, verbose_name='Status of link', blank=True)

    def __str__(self):
        return f'{self.user} {self.long_url}'
