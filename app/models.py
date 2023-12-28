from django.db import models

# Create your models here.
class Tblone(models.Model):
    id=models.AutoField
    uname=models.CharField(max_length=50,default='')
    fname=models.CharField(max_length=50,default='')
    lname=models.CharField(max_length=50,default='')
    mail=models.CharField(max_length=20,default='')
    pwd=models.CharField(max_length=10,default='')

    objects = models.Manager()



    def __str__(self):
        return f'{self.uname} {self.fname} {self.lname} {self.mail} {self.pwd}'

    class Meta:
       db_table='res_tblone_master'


class Tbltwo(models.Model):
    id=models.AutoField
    url=models.CharField(max_length=50,default='')
    pname=models.CharField(max_length=50,default='')
    status=models.CharField(max_length=50,default='')
    wsiteverified=models.CharField(max_length=50,default='')
    projprog=models.CharField(max_length=100,default='')

    objects = models.Manager()

    def __str__(self):
        return f'{self.url} {self.pname} {self.status} {self.wsiteverified} {self.projprog}'

    class Meta:
        db_table='res_tbltwo_master'

class Tblthree(models.Model):
    id=models.AutoField
    start=models.CharField(max_length=50,default='')
    end=models.CharField(max_length=50,default='')
    dwnldpages=models.IntegerField()
    checkpages=models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return f'{self.start} {self.end} {self.dwnldpages} {self.checkpages} '

    class Meta:
        db_table = 'res_tblthree_master'

