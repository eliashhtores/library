from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    passport = models.CharField(max_length=50)
    age = models.IntegerField()
    appellative = models.CharField(max_length=10)

    class Meta:
        db_table = ('person')
        unique_together = ('country', 'appellative')
        constraints = [
            models.CheckConstraint(check=models.Q(
                age__gte=18), name='age_gte_18'),
        ]

    def __str__(self):
        return self.full_name
