from django.db import models
from django.contrib.auth.models import User

class CaffeineItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    serving_size_in_ml = models.FloatField()
    caffeine_amount_in_mg = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# uv run manage.py makemigrations caffeinecalculatorapp
# uv run manage.py migrate

class ConsumedItem(models.Model):
    user = models.ForeignKey(User, related_name='consumed_items', on_delete=models.CASCADE)
    caffeine_item = models.ForeignKey(
        CaffeineItem,
        related_name="consumed_items",
        on_delete=models.SET_NULL,
        null=True,
    )
    consumed_number = models.PositiveIntegerField()
    consumption_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# uv run manage.py makemigrations caffeinecalculatorapp to create new migration file
# uv run manage.py migrate to apply the migration and update the database schema
