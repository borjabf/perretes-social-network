# Django's native ModelForm allows to generate forms
# with validation based on the model (database) created

from django import forms
from .models import Bark

class BarkForm(forms.ModelForm):
    # Refers the Bark model
    class Meta:
        model = Bark
        # Only takes "content" field
        fields = ['content']

        # Widget handles the rendering of the HTML form input elements
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'bark-input',
                'placeholder': 'Type your bark here',
                'rows': 3,
                'maxlength': '140' # Char constrain
            })
        }

        # Removes text content from tag label from the Bark form
        labels = {
            'content': '',
        }

