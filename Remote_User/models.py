from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)



class productdetails_model(models.Model):

    names = models.CharField(max_length=300)
    p_desc= models.CharField(max_length=500)
    p_uses = models.CharField(max_length=200)
    c_name = models.CharField(max_length=300)
    p_price = models.CharField(max_length=300)
    topics = models.CharField(max_length=300)
    pcat = models.CharField(max_length=300)
    senderstatus = models.CharField(default="process", max_length=300 )
    ratings = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    sanalysis= models.CharField(max_length=300)
    DT = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)




