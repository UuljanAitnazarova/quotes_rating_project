from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Quote(models.Model):
    text = models.TextField(max_length=300, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    is_moderated = models.BooleanField(blank=False, null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(get_user_model(), through='api.Rating')
    sum_rating = models.IntegerField(default=0)

    class Meta:
        permissions = [
            ('can_view_non_moderated_quotes', 'Can_view_non_moderated_quotes')
        ]



    def __str__(self):
        return f'{self.author}:{self.text}'


class Rating(models.Model):
    quote = models.ForeignKey('api.Quote', related_name='quote_rating', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), blank=False, null=False, related_name='user_rating', on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(-1), MaxValueValidator(1)])

    def __str__(self):
        return f'{self.user}-{self.quote}-{self.rating}'