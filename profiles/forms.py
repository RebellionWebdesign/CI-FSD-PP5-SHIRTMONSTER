from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone',
            'zip_code',
            'city',
            'adress_line_1',
            'adress_line_2',
            'country',
            'user',
        ]

    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  widget=forms.HiddenInput())

    def set_update_user(self, user):
        self.fields['country'].widget.attrs['autofocus'] = True
        self.fields['user'].initial = user

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone': 'Phone Number',
            'zip_code': 'Postal Code',
            'city': 'Town or City',
            'adress_line_1': 'Street Address 1',
            'adress_line_2': 'Street Address 2',
            'country': 'Country',
            'user': 'Username',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields['phone'].label = "Phone"
