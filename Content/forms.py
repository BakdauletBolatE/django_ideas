from django import forms
from .models import Ideas,Photo

class PhotoToIdeas(forms.ModelForm):
    photo = forms.ImageField(label="photo",widget=forms.FileInput(
                                    attrs={'class':'form-control',
                                    }))

    class Meta:
        model = Photo
        fields = ('photo',)

class IdeasForm(forms.ModelForm):
    title = forms.CharField(label="title",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
    description = forms.CharField(label="description",
                                widget=forms.Textarea(
                                    attrs={'class':'form-control',
                                    }))

    class Meta(object):
        model = Ideas
        fields = ('id','title','description')