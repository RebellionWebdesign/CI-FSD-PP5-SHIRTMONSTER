from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    """ This form lets users write a testimonial """
    class Meta:
        model = Testimonial
        fields = (
            'content',
        )

    def set_content(self, order_number):
        try:
            testimonial = Testimonial.objects.get(order_id__order_number=order_number)
            self.fields['content'].initial = testimonial.content
        except Testimonial.DoesNotExist:
            pass

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, sets autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Write your testimonial here.'
        }

        self.fields['content'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'testimonial-form'
            self.fields[field].label = False
    
    def update_testimonial(self, testimonial, user):
        testimonial.content = self.cleaned_data['content']
        testimonial.save()