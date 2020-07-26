from django.db import models
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=700)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             models.SET_NULL,
                             null=True,
                             blank=True)
    article = models.ForeignKey(Article, models.SET_NULL, null=True, blank=True)
    reply_to = models.ForeignKey('self',
                                 models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name="replytocomment")
    created_date = models.DateTimeField(auto_now_add=True)
