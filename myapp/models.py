from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 20, null = False)#建立字串長度最大為20，且欄位不可空白。
    sex = models.CharField(max_length = 2, default = 'M', null = False)
    birthday = models.DateField(null = False)
    phone = models.CharField(max_length = 20, null = False)

    class Meta:
        db_table = "student"