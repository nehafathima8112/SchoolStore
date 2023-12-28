from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
