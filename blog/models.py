from django.db import models
from martor.models import MartorField
from datetime import date


class Post(models.Model):
    DESIGN = 'DE'
    LIFE = 'LF'
    OFFTOPIC = 'OT'
    CATEGORY_CHOICES = (
        (DESIGN, 'Design'),
        (LIFE, 'Life'),
        (OFFTOPIC, 'Off Topic')
    )

    text_category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=DESIGN)
    text_title = models.CharField(max_length=70)
    text_desc = models.CharField(max_length=200)
    text_body = MartorField()
    pub_date = models.DateField('date published', default=date.today)

    def __str__(self):
        return self.text_title
