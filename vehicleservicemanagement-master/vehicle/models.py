from django.db import models
from django.contrib.auth.models import User 
import datetime
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Mechanic(models.Model):
    #name = models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    skill = models.CharField(max_length=500,null=True)
    salary=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    cat=(('Four wheeler with gear','Four wheeler with gear'),('Four wheeler without gear','Four wheeler without gear'),('Electric Car','Electric Car'))
    category=models.CharField(max_length=50,choices=cat)

    vehicle_no=models.PositiveIntegerField(null=False)
    vehicle_name = models.CharField(max_length=40,null=False)
    vehicle_model = models.CharField(max_length=40,null=False)
    vehicle_brand = models.CharField(max_length=40,null=False)

    problem_description = models.CharField(max_length=500,null=False)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

    stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    def __str__(self):
        return self.problem_description

class Attendance(models.Model):
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    present_status = models.CharField(max_length=10)

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)

#ecom

class Category(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = 'categories'


class Ecustomer(models.Model):  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):  
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=10)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,default=1) 
    description =models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='products/') 

    def __str__(self):
        return self.name 


class Order(models.Model):  
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer =models.ForeignKey(Ecustomer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=20,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
 
#new---
'''class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    # Add other relevant fields'''

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    cost_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other relevant fields

class Service(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service_types = models.ManyToManyField(ServiceType, through='ServiceEntry')
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other relevant fields

class ServiceEntry(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)

class Bill(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other relevant fields 

class Address(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
