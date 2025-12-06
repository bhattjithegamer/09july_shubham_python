from django.db import models

# Create your models here.

class userdata(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    mobil=models.IntegerField(max_length=10)
    city=models.CharField(max_length=20)
    profile_img = models.ImageField(upload_to="profile_images/", default="default.png")

    

class mynotes(models.Model):
    uploaded_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(userdata,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    desc=models.TextField(max_length=500)
    subject=models.CharField(max_length=50)
    files=models.FileField(upload_to='notesdata')
    status_opt=[
        ('pending','pending'),
        ('approve','approve'),
        ('reject','reject')
    ]
    status=models.CharField(max_length=20,choices=status_opt)
    updated_at=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/') # Image upload karva mate

class contact_us(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField()