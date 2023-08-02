from django.db import models

class Account_Type(models.Model):
    type = models.CharField(max_length=20)

class City(models.Model):
    city = models.CharField(max_length=50)

class Province(models.Model):
    province = models.CharField(max_length=50)


class Container_Length(models.Model):
    length = models.IntegerField()


class Container_Height(models.Model):
    height = models.IntegerField()


class Container_Year(models.Model):
    year = models.IntegerField()


class Container_Type(models.Model):
    type = models.CharField(max_length=20)
    inspection_cost = models.IntegerField()

class Repair_Type(models.Model):
    type = models.CharField(max_length=30)


class Repair_Area(models.Model):
    area = models.CharField(max_length=30)


class Damage_Area(models.Model):
    area = models.CharField(max_length=30)

class Quantity(models.Model):
    quantity = models.IntegerField()

class Yard(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,)
    phone = models.CharField(max_length=10, unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    pincode = models.IntegerField()

class Comp(models.Model):
    comp = models.CharField(max_length=30)
class Rep(models.Model):
    rep = models.CharField(max_length=30)
class Component(models.Model):
    component = models.CharField(max_length=30)
class Event(models.Model):
    event = models.CharField(max_length=30)
class Dam(models.Model):
    dam = models.CharField(max_length=30)