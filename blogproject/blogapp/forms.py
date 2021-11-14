from django import forms

class PostForm(forms.Form):
    post_title = forms.CharField(label='Post Title', max_length=200, min_length=5)
    post_content =forms.CharField(widget=forms.Textarea, label='Post Content', max_length=10000, min_length=50)
