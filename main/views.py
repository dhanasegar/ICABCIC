from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PaperSubmissionForm, ContactForm
from .forms import ContactForm
from django.shortcuts import render

from django.core.mail import EmailMessage


def home(request):
    contact_form = ContactForm()
    paper_form = PaperSubmissionForm()
    return render(request, "index.html", {'contact_form': contact_form, 'paper_form': paper_form})

def paper(request):
    if request.method == 'POST':
        form = PaperSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
           
            title = form.cleaned_data['title']
            author_name = form.cleaned_data['author_name'] 
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            institution = form.cleaned_data['institution']
            category = form.cleaned_data['category']
            paper_file = request.FILES.get('paper_file')

          
            subject = f'New Paper Submission By - {author_name}'  

          
            message = f"""
            Title: {title}
            Author: {author_name}
            Mobile: {mobile}
            Email: {email}
            Institution: {institution}
            Category: {category}
            """

           
            email_msg = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['it@gmail.com']
            )

          
            if paper_file:
                email_msg.attach(paper_file.name, paper_file.read(), paper_file.content_type)

           
            email_msg.send()

            return redirect('paper_success')  

    else:
        form = PaperSubmissionForm()
    
    return render(request, 'paper.html', {'form': form})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name'] 
        
        subject = f'Contact Inquiry - {name}'

        message = f"""
        Name: {name}
        Email: {form.cleaned_data['email']}
        Phone: {form.cleaned_data['phone']}
        Subject: {form.cleaned_data['subject']}
        Message: {form.cleaned_data['message']}
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['it@gmail.com']

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('contact_success') 

    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, 'contact_success.html')

def paper_success(request):
    return render(request, 'paper_success.html')