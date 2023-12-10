from django.db import models

# Create your models here.
class logindb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Phone = models.IntegerField(null=True)
    Mobile = models.IntegerField(null=True)
    Address=models.TextField(max_length=100,null=True)

    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)


from django.db import models

class WikipediaEntry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
