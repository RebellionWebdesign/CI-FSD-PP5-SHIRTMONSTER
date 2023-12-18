from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import CustomShirt
from .forms import CustomShirtForm
import boto3
import os
from django.conf import settings

class CustomShirtView(View):
    """ This view displays a contact form for custom shirt inquiries """
    def get(self, request):
        template = 'customshirt/customshirt.html'
        if request.user.is_authenticated:
            profile = request.user.userprofile
            profile_mail = request.user
            initial_data = {
                'full_name': profile.user.first_name + ' ' + profile.user.last_name,
                'email': profile_mail.email,
                'phone': profile.phone,
            }

            inquiry_form = CustomShirtForm(initial=initial_data)

            context = {
            'inquiry_form': inquiry_form,
            }
        else:
            inquiry_form = CustomShirtForm(request.POST)
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
            image_url = f"{settings.AWS_S3_CUSTOM_DOMAIN}/{image_location}"

            try:
                client.upload_fileobj(image, os.environ.get('AWS_BUCKET'), image_location)
                custom_shirt_instance.image = image_location
                custom_shirt_instance.image_url = image_url
                custom_shirt_instance.save()
                messages.success(request, 'Inquiry saved, we will contact you within 24 hours!')
                return redirect(reverse('custom_shirts'))
            except Exception as e:
                messages.error(request, 'Error while uploading image, please contact us via eMail.')
    
            inquiry_form = CustomShirtForm(request.POST, request.FILES)
            context =  {
                'inquiry_form': inquiry_form
            }

            return redirect(reverse('custom_shirts'))
