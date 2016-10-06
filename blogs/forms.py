#表单

from django import forms

from blogs.models import Blog


class BlogEntity(forms.Form):
    title = forms.CharField(label= u'标题', max_length=30)

    content = forms.CharField(label= u'内容', max_length=30)

    # Meta类是告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
    # class Meta:
    #     model = Blog
    #     fields = ['text']
    #     labels = {'text': ''}