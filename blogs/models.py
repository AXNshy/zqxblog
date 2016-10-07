

# Create your models here.

from django.db import models

class Topic(models.Model):
    topic = models.CharField(u'主题', max_length=30)






class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(u'作者', max_length=30)
    topic = models.ForeignKey(Topic)
    createTime = models.DateTimeField(u'发布时间', auto_now_add=True, editable=True)
    updateTime = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = models.TextField(u'内容', max_length=256)
    title = models.TextField(u'标题',)
    def __str__(self):
        return self.title




class Person(models.Model):
    firstName = models.CharField(u'姓',max_length=30)
    lastName = models.CharField(u'名', max_length=30)

    def myProperty(self):
        return self.firstName+' '+self.lastName
    myProperty.shortDescription="full name of the person"

    fullName = property(myProperty)