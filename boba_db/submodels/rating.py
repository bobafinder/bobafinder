from django.db import models
from django.contrib.auth.models import User
from boba_db.submodels.review import Review


class Rating(models.Model):
    score = models.IntegerField()
    name = models.CharField(max_length=200)
    caption = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    review = models.ForeignKey(Review, blank=True, null=True)

    def __str__(self):
        return '{}: {} - {}'.format(self.__class__.__name__, self.name, self.score)
