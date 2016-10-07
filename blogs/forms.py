# 表单

from django import forms

from blogs.models import Blog


class BlogEntity(forms.ModelForm):
    # Meta类是告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
    class Meta:
        model = Blog
        fields = ['title', 'content']

        # labels = {'title': '标题', 'content': '内容'}

        widgets = {'title': forms.TextInput(attrs={'type': 'text'}), 'content': forms.Textarea(attrs={'cols': 40})}
