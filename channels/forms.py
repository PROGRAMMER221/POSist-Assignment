from django import forms
from channels.models import Tags, Channel

# FORMS
class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tag_name']

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name','description','tags']

class InviteForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'required' : True,
        'class' : 'form-control'
    }))