#encoding=utf-8
from django.db import models

# Create your models here.
class article(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField("标题",max_length=100)
    text=models.TextField("内容",max_length=4000)
    cdate=models.DateTimeField()
    tag=models.CharField("标签",max_length=200,blank=True)
    def __str__(self):
        return self.title
    
class imgpic(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField("标题",max_length=100)
    url=models.CharField("链接地址",max_length=200)
    cdate=models.DateTimeField()
    x=models.IntegerField(blank=True,null=True)
    y=models.IntegerField(blank=True,null=True)
    tag=models.CharField("标签",max_length=200,blank=True)