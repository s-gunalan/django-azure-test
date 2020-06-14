from django.db import models

# Create your models here.
class Rules(models.Model):
    rule_name = models.CharField(max_length=200)
    rule_type = models.CharField(max_length=200)
    def __str__(self):
        return self.rule_name
class Bugs(models.Model):
    criticality = models.CharField(default='code smell',max_length=20)
    rule = models.ForeignKey(Rules,on_delete = models.CASCADE)
    def __str__(self):
        return self.criticality