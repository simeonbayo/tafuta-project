from django import forms

from .models import DocUpload, DocRequest, NotFound, ServiceRequest,Document

#Create your forms here
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docname','docimage','desc']

class DocUploadForm(forms.ModelForm):
    docfile = forms.ImageField()
    class Meta:
        model = DocUpload
        fields = ['doctype','doc_surname','doc_givenname','docfile','docfile_two','uploaded_by','district','location']

class DocRequestForm(forms.ModelForm):
    
    class Meta:
        model = DocRequest
        fields = ['urgency','current_address']

class NotFoundForm(forms.ModelForm):
    class Meta:
        model = NotFound
        fields = ['doctype','doc_lost_location','urgency','current_address']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type','description','urgency','current_address']

class NewDocUploadForm(forms.ModelForm):
    
    class Meta:
        model = DocUpload
        fields = ['doctype','doc_surname','doc_givenname','docfile','docfile_two','district','location']

class ContactForm(forms.Form):
    fullnames = forms.CharField(max_length="100")
    email = forms.EmailField()
    subject = forms.CharField(max_length="100")
    message = forms.CharField(widget=forms.Textarea, required=True)