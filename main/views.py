from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PaperSubmissionForm, ContactForm
from .forms import ContactForm
from django.shortcuts import render
from smtplib import SMTPException
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

            try:
         
                subject_admin = f'New Paper Submission By - {author_name}'  
                message_admin = f"""
                Title: {title}
                Author: {author_name}
                Mobile: {mobile}
                Email: {email}
                Institution: {institution}
                Category: {category}
                """

                email_msg_admin = EmailMessage(
                    subject_admin,
                    message_admin,
                    settings.EMAIL_HOST_USER,
                    ['bit@gmail.com']
                )

                if paper_file:
                    email_msg_admin.attach(paper_file.name, paper_file.read(), paper_file.content_type)

                email_msg_admin.send()


                subject_user = 'Thank You for Your Paper Submission'
                message_user = f"""
                Dear {author_name},

                Thank you for submitting your paper titled "{title}". We have received your submission and will review it shortly.

                Best regards,
                Your Organization
                """

                email_msg_user = EmailMessage(
                    subject_user,
                    message_user,
                    settings.EMAIL_HOST_USER,
                    [email]
                )

                email_msg_user.send()

                return redirect('paper_success')  

            except SMTPException as e:
         
                print(f"SMTP Error: {e}")
                return render(request, 'paper.html', {'form': form, 'error_message': 'Something went wrong. Please try again later.'})

    else:
        form = PaperSubmissionForm()
    
    return render(request, 'paper.html', {'form': form})





def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name'] 
        email = form.cleaned_data['email']
        
        try:

            subject_admin = f'Contact Inquiry - {name}'
            message_admin = f"""
            Name: {name}
            Email: {email}
            Phone: {form.cleaned_data['phone']}
            Subject: {form.cleaned_data['subject']}
            Message: {form.cleaned_data['message']}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bit@gmail.com']

            send_mail(subject_admin, message_admin, from_email, recipient_list, fail_silently=False)

            subject_user = 'Thank You for Contacting Us'
            message_user = f"""
            Dear {name},

            Thank you for contacting us. We have received your message and will get back to you shortly.

            Best regards,
            Your Organization
            """

            email_msg_user = EmailMessage(
                subject_user,
                message_user,
                settings.EMAIL_HOST_USER,
                [email]
            )

            email_msg_user.send()

            return redirect('contact_success') 

        except SMTPException as e:

            print(f"SMTP Error: {e}")
            return render(request, "contact.html", {"form": form, "error_message": "Something went wrong. Please try again later."})

    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, 'contact_success.html')

def paper_success(request):
    return render(request, 'paper_success.html')