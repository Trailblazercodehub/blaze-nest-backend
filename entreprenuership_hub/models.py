from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CoWorking(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField('customuser.CustomUser', related_name='coworking', blank=True, null=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coworking/', null=True,
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CoWorkingApplication(models.Model):
    user = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE)
    coworking = models.ForeignKey(CoWorking, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} appied for {self.coworking.name} coworking space"
    

    
class Incubator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField('customuser.CustomUser', related_name='incubator', blank=True, null=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='incubator/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class IncubatorApplication(models.Model):
    user = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} appied for {self.incubator.name} Incubator"
    
