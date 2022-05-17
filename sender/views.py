from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.core.mail import send_mail
from .models import EmailContact


class IndexView(TemplateView):

    template_name =  'sender/homepage.html'
    


def SendPage(request):
        if request.method == 'POST':
            name = request.POST.get('full-name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            entry = EmailContact(name=name, email=email, subject=subject, message=message)
            entry.save()
            
            context = {   
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
                }

            send_mail(context['subject'], str(context['message']), '', ['django.developer.tester@gmail.com'])

        return render(request, 'sender/emailprovision.html', {})