from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import CustomShirt
from .forms import CustomShirtForm
import boto3
import os

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
            inquiry_form = CustomShirtForm(request.POST, request.FILES)

        if inquiry_form.is_valid():
            custom_shirt_instance = inquiry_form.save(commit=False)
            client = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'), aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))
            image = request.FILES['image']
            image_location = f'custom_shirts/{image.name}'

            try:
                client.upload_fileobj(image, os.environ.get('AWS_BUCKET'), image_location)
                custom_shirt_instance.image = image_location
                custom_shirt_instance.save()
                messages.success(request, 'Inquiry saved, we will contact you within 25 hours!')
                return redirect(reverse(template))
            except Exception as e:
                messages.error(request, 'Error while uploading image, please contact us via eMail.')
    
            inquiry_form = CustomShirtForm(request.POST, request.FILES)
            context =  {
                'inquiry_form': inquiry_form
            }

            return render(request, 'customshirt/customshirt.html', context)
