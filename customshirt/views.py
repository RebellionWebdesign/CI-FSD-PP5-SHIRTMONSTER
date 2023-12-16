from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import CustomShirt
from .forms import CustomShirtForm

class CustomShirtView(View):
    """ This view displays a contact form for custom shirt inquiries """
    def get(self, request):
        inquiry_form = CustomShirtForm(request.POST)
        template = 'customshirt/customshirt.html'
        context = {
            'inquiry_form': inquiry_form,
        }
        return render(request, template, context)
    
    def post(self, request):
        template = 'home'
        if request.method == 'POST':
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone': request.POST['phone'],
                'inquiry': request.POST['inquiry'],
            }
            inquiry_form = CustomShirtForm(form_data)

            if inquiry_form.is_valid():
                inquiry_form.save()
                messages.success(request, 'Inquiry saved, we will contact you within 25 hours!')
            return redirect(reverse(template))
