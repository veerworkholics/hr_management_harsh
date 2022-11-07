from django.db import models

# Create your models here.
class Customuser(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  mobile=models.CharField(max_length=20)
  email=models.EmailField(max_length=50)
  image=models.ImageField(null=True)
  role_id=models.IntegerField()
  password=models.CharField(max_length=20)
  address=models.TextField()
  status=models.IntegerField()
  created_at=models.DateField()
  updated_at=models.DateField()

class Role(models.Model):
  role_name=models.CharField(max_length=100)
  status=models.IntegerField()
  created_at=models.DateTimeField()
  updated_at=models.DateTimeField()


