from django.db import models

# Create your models here.

class Questions(models.Model):
    quest = models.TextField(max_length=150, db_index=True)


class Answ(models.Model):
    answer = models.TextField(max_length=150, db_index=True)
    quest = models.ForeignKey(Questions, on_delete=models.CASCADE)
    nq = models.OneToOneField(Questions, on_delete=models.CASCADE, related_name='+')