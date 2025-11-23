from django.db import models


# Create your models here.
class userlogin(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    img=models.ImageField(upload_to='images/',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(userlogin, on_delete=models.CASCADE, null=True)

class Like(models.Model):
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(userlogin, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(userlogin, on_delete=models.CASCADE, related_name="followers")
