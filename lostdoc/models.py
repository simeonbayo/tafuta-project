from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
#Extend user model to create a custom user model with more fields
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .ugdistricts import DISTRICTS

#Image Compression function
def Compress(image):
    im = Image.open(image)
    #Create a ByteISO object
    im_io = BytesIO()
    #Save image to ByteISO object
    im.save(im_io, 'JPEG', quality = 10)
    #Create a django-friendly files object
    new_image = File(im_io, name=image.name)

    return new_image

# Create your models here.
#Custom user model from the abstract user model
class User(AbstractUser):
    telephone_no = models.IntegerField(verbose_name="Telephone Number", null=True)
    address = models.CharField(max_length=500)
    district = models.CharField(max_length=50, choices=DISTRICTS, default="Kampala")


class Document(models.Model):
    DOCTYPE = (
        ("National ID","National ID"),
        ("Passport","Passport"),
        ("Driving Licence","Driving Licence"),
        ("Academic Document","Academic Document"),
        ("Other Document","Other Document")
    )
    docname = models.CharField(max_length=20, verbose_name="Type of Document", choices=DOCTYPE)
    docimage = models.ImageField(upload_to = 'documents/', null = True)
    desc = models.TextField(verbose_name="Description", default="")

    def __str__(self):
        return self.docname

class DocUpload(models.Model):
    doctype = models.ForeignKey(Document, on_delete = models.CASCADE,verbose_name="Document Type")
    doc_surname = models.CharField(max_length=200, default = "",verbose_name= "Document Surname")
    doc_givenname = models.CharField(max_length=200, default = "", verbose_name="Document Givenname")
    docfile = models.ImageField(upload_to = 'documents/', default = "", verbose_name="Front Image")
    docfile_two = models.ImageField(upload_to = 'documents/', default = "", verbose_name="Back Image")
    uploaded_at = models.DateTimeField(auto_now_add= True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    district = models.CharField(max_length=50, choices=DISTRICTS, default="Kampala")
    location = models.CharField(max_length= 200)

    def __str__(self):
        return self.docfile.name

    def save(self, *args, **kwargs):
        #call the compress function
        new_image = Compress(self.docfile)
        new_image2 = Compress(self.docfile_two)
        #Set the uploaded images to the compressed images
        self.docfile = new_image
        self.docfile_two = new_image2
        #Save
        super().save(*args, **kwargs)

URGENCY = (
        ('Days','Days'),
        ('Weeks','Weeks'),
        ('Months','Months'),
    )

class DocRequest(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Complete','Complete')
    )
    requested_doc = models.ForeignKey(DocUpload, on_delete = models.CASCADE, verbose_name= "Requested Document")
    doc_requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    requested_date = models.DateTimeField(auto_now_add= True, verbose_name= "Requested Date")
    urgency = models.CharField(max_length=10, choices=URGENCY, default="" , verbose_name="How urgent do you need the document ?")
    current_address = models.CharField(max_length=100, default="Kampala,Bwaise", verbose_name="Where is your current location (e.g.Kampala,Bwaise) ?")
    doc_request_status = models.CharField(max_length=10,null=True, choices = STATUS, verbose_name= "Status")
    doc_clearance_date = models.DateTimeField(auto_now_add= True, verbose_name="Clearance Date")
    
    def __str__(self):
        return self.requested_doc.docfile.name
    
class NotFound(models.Model):
    
    doctype = models.ForeignKey(Document, on_delete = models.CASCADE, verbose_name="Document Type")
    doc_requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    requested_date = models.DateTimeField(auto_now_add= True, verbose_name= "Requested Date")
    doc_lost_location = models.CharField(max_length=300, default="Kampala,Bwaise-Shell", verbose_name="Specify (e.g.Kampala,Bwaise) where you think, you lost the document ?")
    urgency = models.CharField(max_length=10,choices=URGENCY, default="", verbose_name="How urgent do you need the document ?")
    current_address = models.CharField(max_length=100, default="Kampala,Bwaise-Shell", verbose_name="Where is your current location (e.g.Kampala,Bwaise) ?")

    def __str__(self):
        return self.doc_requester.first_name

class ServiceRequest(models.Model):
    SERVICE_TYPE = (
        ('New Document','New Document'),
        ('Renew Document','Renew Document'),
        ('Others','Others')
    )
    doctype = models.ForeignKey(Document, on_delete = models.CASCADE, verbose_name="Document Type")
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE, verbose_name="Type of Service")
    description = models.TextField(verbose_name="Summarize your request here")
    service_requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    requested_date = models.DateTimeField(auto_now_add= True, verbose_name= "Requested Date")
    
    urgency = models.CharField(max_length=10,choices=URGENCY,default="", verbose_name="How urgent do you need the document ?")
    current_address = models.CharField(max_length=100, default="Kampala,Bwaise-Shell", verbose_name="Where is your current location (e.g.Kampala,Bwaise) ?")

    def __str__(self):
        return self.service_requester.first_name