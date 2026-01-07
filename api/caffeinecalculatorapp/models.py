from django.db import models

class CaffeineItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    serving_size_in_ml = models.FloatField()
    caffeine_amount_in_mg = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# python3 manage.py makemigrations caffeinecalculatorapp
# python3 manage.py migrate

#   ...
# TODO-1-1 Créer une nouvelle migration et l'appliquer

# TODO-6-0 Créer un nouveau model nommé ConsumedItem et ajouter
# les champs : user, caffeine_item, consumed_number, consumption_date, created, updated
# TODO-6-1 Créer une nouvelle migration et l'appliquer
