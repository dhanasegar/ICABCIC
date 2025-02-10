from django import forms
import re

# Validator for mobile numbers
def validate_mobile(value):
    if not re.fullmatch(r'^\+?\d{10,15}$', value):
        raise forms.ValidationError("⚠️ Invalid mobile number! Enter 10-15 digits (optional + at the start).")

# Validator for file uploads (only .pdf, .doc, .docx allowed)
def validate_file_extension(value):
    valid_extensions = ('.pdf', '.doc', '.docx')
    if not value.name.lower().endswith(valid_extensions):
        raise forms.ValidationError("⚠️ Invalid file format! Only PDF, DOC, and DOCX files are allowed.")


class PaperSubmissionForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter paper title',
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100  rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    author_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter author name',
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    mobile = forms.CharField(
        max_length=15,
        validators=[validate_mobile],
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter mobile number',
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email address',
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100  rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    institution = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter institution name',
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    category = forms.ChoiceField(
        choices=[
            ('academicians', 'Academicians'),
            ('researchers', 'Researchers'),
            ('students', 'Students'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100 rounded-lg  focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    paper_file = forms.FileField(
        validators=[validate_file_extension],
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-600 bg-gray-100 rounded-lg  focus:ring-2 focus:ring-blue-500 focus:outline-none cursor-pointer'
        })
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-lg  bg-gray-100 text-black border border-gray-600',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 rounded-lg  bg-gray-100 text-black border border-gray-600',
            'placeholder': 'Your Email'
        })
    )
    phone = forms.CharField(
        validators=[validate_mobile],
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-lg  bg-gray-100 text-black border border-gray-600',
            'placeholder': 'Your Phone'
        })
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-lg  bg-gray-100 text-black border border-gray-600',
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 rounded-lg  bg-gray-100 text-black border border-gray-600 h-32',
            'placeholder': 'Your Message'
        })
    )
