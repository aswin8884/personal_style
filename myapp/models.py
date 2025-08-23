from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class User_registration(models.Model):

    name=models.CharField(max_length=25,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    profile_picture=models.ImageField(null=True)
    approvel=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Stylist_registration(models.Model):

    name=models.CharField(max_length=25,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    admin_approval=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Tailor_registration(models.Model):

    name=models.CharField(max_length=25,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    admin_approval=models.BooleanField(default=False)
    work_status=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Add_outfit_designs(models.Model):

    name=models.CharField(max_length=25,null=True)
    description=models.CharField(max_length=25,null=True)
    image=models.ImageField(null=True)
    stylist_id=models.ForeignKey(Stylist_registration,on_delete=models.CASCADE,null=True)

class Work_request(models.Model):

    name=models.CharField(max_length=25,null=True)
    shipping_address=models.CharField(max_length=50,null=True)
    details=models.CharField(max_length=500,null=True)
    quantity=models.CharField(max_length=50,null=True)
    contact=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    payment_status=models.BooleanField(default=False)
    delivery_date=models.DateField(null=True)
    request_on=models.DateTimeField(null=True)
    accept_status=models.BooleanField(default=False)
    accepted_on=models.DateTimeField(null=True)
    outfit_id=models.ForeignKey(Add_outfit_designs,on_delete=models.CASCADE,null=True)
    tailor_id=models.ForeignKey(Tailor_registration,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)


class User_message_to_stylist(models.Model):

    stylist_id=models.ForeignKey(Stylist_registration,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=100,null=True)
    message_on=models.DateTimeField(null=True)
    reply=models.CharField(max_length=100,null=True)
    reply_on=models.DateTimeField(null=True)

class User_message_to_tailor(models.Model):

    tailor_id=models.ForeignKey(Tailor_registration,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=100,null=True)
    message_on=models.DateTimeField(null=True)
    reply=models.CharField(max_length=100,null=True)
    reply_on=models.DateTimeField(null=True)
    
class Feedback(models.Model):

    feedback=models.CharField(max_length=500,null=True)
    rating=models.IntegerField(null=True)
    feedback_on=models.DateTimeField(null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)