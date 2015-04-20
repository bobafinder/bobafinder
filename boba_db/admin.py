from django.contrib import admin
from . import models


class RatingInline(admin.StackedInline):
    model = models.Rating


class ReviewAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Review', {'fields': ['headline', 'body']}),
    #     ('Overall Rating', {'fields': ['overall_rating']}),
    # ]
    inlines = [RatingInline]


# Register your models here.
admin.site.register(models.Review, ReviewAdmin)
# admin.site.register(models.Rating)
admin.site.register(models.Store)
