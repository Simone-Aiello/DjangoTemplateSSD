from django.db import models


# Create your models here.
class SuperHero(models.Model):
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    epic_name = models.CharField(max_length=50)
    secret_identity = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.epic_name}"
