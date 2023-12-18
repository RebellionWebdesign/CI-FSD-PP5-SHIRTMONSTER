from django import forms
from .models import CustomShirt


class CustomShirtForm(forms.ModelForm):
    class Meta:
        model = CustomShirt
        fields = (
            'full_name',
            'email',
            'phone',
            'image',
            'inquiry',
        )

    def __init__(self, *args, **kwargs):
        """ Add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name*',
            'email': 'Email Address*',
            'phone': 'Phone Number',
            'image': 'Custom print image here',
            'inquiry': 'Please provide a description*'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            placeholder = f'{placeholders[field]}'
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False