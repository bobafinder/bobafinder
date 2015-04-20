from django.db import models
from django.contrib.auth.models import User
from boba_db.submodels.store import Store


class Review(models.Model):
    overall_rating = models.IntegerField()
    reviewer = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    headline = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return '{}: {} - {}'.format(self.__class__.__name__, self.headline, self.body)
