# payments/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Food(models.Model):
    foodid = models.AutoField(db_column='foodID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    foodname = models.CharField(max_length=255, blank=True, null=True)
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    expireddate = models.DateField(db_column='expiredDate', blank=True, null=True)  # Field name made lowercase.
    categories = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Interests(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    foodid = models.ForeignKey(Food, models.DO_NOTHING, db_column='FoodID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interests'


class Order(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='Food_ID', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    order_type = models.IntegerField(db_column='Order_Type', blank=True, null=True)  # Field name made lowercase.
    order_quantity = models.IntegerField(db_column='Order_quantity', blank=True, null=True)  # Field name made lowercase.
    order_amount = models.DecimalField(db_column='Order_Amount', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel_number = models.IntegerField(db_column='Tel_Number', blank=True, null=True)  # Field name made lowercase.
    password = models.IntegerField(db_column='PassWord', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

class Profile(AbstractUser):
    id = models.BigAutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)
    nickname = models.CharField(verbose_name="nickname", max_length=256, default="", blank=True)
    tel_number = models.CharField(verbose_name="tel_number", max_length=256, default="", blank=True)
    gender = models.CharField(verbose_name="gender", max_length=255, default="", blank=True)
    type = models.CharField(verbose_name="type", max_length=255, default="", blank=True)
    balance = models.DecimalField(verbose_name="balance", max_digits=10, decimal_places=2, blank=True, default=0)
    first_name = models.CharField(verbose_name="first_name", max_length=255, default="", blank=True)
    last_name = models.CharField(verbose_name="last_name", max_length=255, default="", blank=True)
    status = models.IntegerField(verbose_name="status", default=0, blank=True)
    version = models.IntegerField(verbose_name="version", default=0, blank=True)
    create_time = models.DateTimeField(verbose_name="create_time", auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(verbose_name="modify_time", auto_now=True, blank=True)

    class Meta:
        db_table = "profile"
        verbose_name = "profile"
        app_label = "payments"

class Apply(models.Model):
    releaseDate = models.DateField(max_length=32, verbose_name="releaseDate")
    expiredDate = models.DateField(max_length=32, verbose_name="expiredDate")
    categories = models.CharField(max_length=15, verbose_name="categories")
    price = models.EmailField(max_length=32, verbose_name="price")
    description = models.CharField(max_length=100, verbose_name="description")
    quantity = models.EmailField(max_length=32, verbose_name="quantity")
    postcode = models.CharField(max_length=32, verbose_name="postcode")
    location = models.CharField(max_length=32,verbose_name="location")