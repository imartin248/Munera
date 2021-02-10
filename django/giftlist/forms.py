from django import forms
from . import models

class AddGift(forms.ModelForm):
    class Meta:
        model = models.Gift
        fields = ['name', 'price', 'link', 'user']

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.TextInput(attrs={'class': 'form-control'}),
                'link': forms.TextInput(attrs={'class': 'form-control'}),
            }
        

class AddGroupMember(forms.ModelForm):
    class Meta:
        model = models.GroupMember
        fields = ['member','group']

class CreateGroup(forms.ModelForm):
    class Meta:
        model  = models.UserGroup
        fields = ['admin','group_name']

        widgets = {
                'group_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Group'}),
            }
