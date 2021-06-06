from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=45,null=False)
    second_name = models.CharField(max_length=45, null = False)
    phone = models.IntegerField(null =False)
    mail = models.CharField(max_length=45, null = False)


