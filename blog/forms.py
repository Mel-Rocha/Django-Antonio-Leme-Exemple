from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    """
    Form for forms that are independent of models and
    generally represent relationship attributes
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """
    ModelForm for forms associated with models
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
