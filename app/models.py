from django.db import models
class Topic(models.Model):
    Topic_Name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Topic_Name
class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    Email=models.EmailField(max_length=254,default='vaishu@gmail.com')
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.author


