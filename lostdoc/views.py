from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .forms import ContactForm, DocUploadForm, NewDocUploadForm, DocRequestForm, NotFoundForm, ServiceRequestForm, DocumentForm
from .models import DocUpload, DocRequest, Document, ServiceRequest
from .filters import DocSearchFilter
from django.db.models import Q
import datetime

# Create your views here.
def index(request):
    passport = Document.objects.get(docname__exact = "Passport")
    nin = Document.objects.get(docname__exact = "National ID")
    driving_licence = Document.objects.get(docname__exact = "Driving Licence")
    academic_doc = Document.objects.get(docname__exact = "Academic Document")
    

    context = {
        'passport':passport,
        'nin':nin,
        'driving_licence':driving_licence,
        'academic_doc':academic_doc,
        
    }
    
    return render(request, 'lostdoc/index.html', context)

def aboutUs(request):
    return render(request, 'lostdoc/aboutus.html')

def services(request):
    doctypeServices = Document.objects.all

    return render(request, 'lostdoc/services.html', {'doctypeServices':doctypeServices})

@login_required
def newDocumentType(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoctype = form.save(commit=False)
            newdoctype.docname = form.cleaned_data['docname']
            newdoctype.docimage = form.cleaned_data['docimage']
            newdoctype.desc = form.cleaned_data['desc']
            newdoctype.save()

            return redirect('aboutus')
            
    else:
        form = DocumentForm()
        return render(request, 'lostdoc/adddoctype.html', {'form':form})
def newDocTest(request):
       
    
   
        docname = request.POST.get('docname')
        docimage = request.POST.get('docimage')
        desc = request.POST.get('desc')
        

        
        image = docimage
        return render(request, 'lostdoc/addtest.html',{'image':image})

@login_required
def newUpload(request):
    if request.method == "POST":
        doctype_list = Document.objects.all()
       
        form = NewDocUploadForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.doctype = form.cleaned_data['doctype']
            upload.doc_surname = form.cleaned_data['doc_surname']
            upload.doc_givenname = form.cleaned_data['doc_givenname']
            upload.docfile = form.cleaned_data['docfile']
            upload.docfile_two = form.cleaned_data['docfile_two']

            upload.uploaded_by = request.user
            
            upload.location = form.cleaned_data['location']
            upload.save()

            return render(request, 'lostdoc/successful_upload.html', {'doctype_list':doctype_list})
    else:
        form = NewDocUploadForm()
        num_nin = DocUpload.objects.all().filter(doctype__exact = 1).count()
        num_Passport = DocUpload.objects.all().filter(doctype__exact = 2).count()
        num_DrivingLicence = DocUpload.objects.all().filter(doctype__exact = 3).count()
        num_AcademicDocument = DocUpload.objects.all().filter(doctype__exact = 4).count()
        num_OtherDocument = DocUpload.objects.all().filter(doctype__exact = 5).count()

        context = {
            'form':form,
            'num_nin':num_nin,
            'num_Passport':num_Passport,
            'num_DrivingLicence':num_DrivingLicence,
            'num_AcademicDocument':num_AcademicDocument,
            'num_OtherDocument':num_OtherDocument,
        }
    return render(request, 'lostdoc/docupload2.html', context)

@login_required
def notFoundDoc(request):
    if request.method == "POST":
        doctype_list = Document.objects.all()
        form = NotFoundForm(request.POST)

        if form.is_valid():
            notfound = form.save(commit=False)
            notfound.doctype = form.cleaned_data.get('doctype')
            notfound.doc_lost_location = form.cleaned_data.get('doc_lost_location')
            notfound.urgency = form.cleaned_data.get('urgency')
            notfound.current_address = form.cleaned_data.get('current_address')
            
            notfound.doc_requester  = request.user
            notfound.requested_date = datetime.datetime.now()

            notfound.save()

            return render(request,'lostdoc/notfound_submit_done.html',{'doctype_list':doctype_list})
    else:
        form = NotFoundForm()
    return render(request, 'lostdoc/notfound.html', {'form':form})

'''Django Filter Search'''
@login_required
def docSearch(request):
    doc_list = DocUpload.objects.all()
    doc_filter = DocSearchFilter(request.GET, queryset= doc_list)

    return render(request, 'lostdoc/docsearch.html', {'filter': doc_filter})

'''Custom Search'''
@login_required
def userSearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(doc_surname__icontains = query) | Q(doc_givenname__icontains = query)
            results = DocUpload.objects.filter(lookups).distinct()

            context = {
                'results':results,
                'submitbutton':submitbutton,
            }

            return render(request, 'lostdoc/usersearch.html', context)
        else:
            return render(request, 'lostdoc/usersearch.html')
    else:
        return render(request, 'lostdoc/usersearch.html')

@login_required
def doc_detail_view(request, pk):
    form = DocRequestForm
    try:
        doc = DocUpload.objects.get(pk=pk)
    except DocUpload.DoesNotExist:
        raise Http404('Document does not exist')
    
    return render(request, 'lostdoc/doc_detail.html', context={'doc': doc, 'form': form})

@login_required
def docRequest(request, doc_id):
    #Requesting a given document by the user
    doc = get_object_or_404(DocUpload, pk = doc_id)
    doctype_list = Document.objects.all()
    form = DocRequestForm(request.POST)

    if form.is_valid():
        doc_requester = request.user
        doc_status = form.cleaned_data.get('doc_request_status')

        doc_request = DocRequest()

        doc_request.requested_doc = doc
        doc_request.doc_requester = doc_requester
        doc_request.doc_request_status = doc_status
        doc_request.requested_date = datetime.datetime.now()

        doc_request.save()

        '''return HttpResponseRedirect(reverse('docdetail', args=(doc.id,)))'''
        return render(request, 'lostdoc/request_complete.html', context={'doc': doc, 'doctype_list':doctype_list})
    
    return render(request, 'lostdoc/doc_detail.html', context={'doc': doc, 'form': form})
     
@login_required
def document_type_detail(request, pk):
    form = ServiceRequestForm
    try:
        doctype = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        raise Http404('Document does not exist')
    
    return render(request, 'lostdoc/doctype_detail.html', context={'doctype': doctype, 'form': form})

@login_required
def serviceRequest(request, doctype_id):
    #Requesting a given service by the user
    doctype = get_object_or_404(Document, pk = doctype_id)
    doctypeServices = Document.objects.all
    form = ServiceRequestForm(request.POST)

    if form.is_valid():
        service_requester = request.user
        
        service_type = form.cleaned_data.get('service_type')
        description = form.cleaned_data.get('description')
        urgency = form.cleaned_data.get('urgency')
        current_address = form.cleaned_data.get('current_address')

        service_request = ServiceRequest()

        service_request.doctype  = doctype 
        service_request.service_type = service_type
        service_request.description = description
        service_request.service_requester = service_requester
        service_request.requested_date = datetime.datetime.now()
        service_request.urgency = urgency
        service_request.current_address = current_address

        service_request.save()

        '''return HttpResponseRedirect(reverse('docdetail', args=(doc.id,)))'''
        return render(request, 'lostdoc/service_request_sent.html', context={'doctype': doctype, 'doctypeServices':doctypeServices})
    
    return render(request, 'lostdoc/doctype_detail.html', context={'doctype': doctype, 'form': form})

def navigation(request):
    docs = Document.objects.all().count()
    nin = Document.objects.filter(docname__exact = 'National ID')

    num_nin = DocUpload.objects.all().filter(doctype__exact = 1).count()
    num_Passport = DocUpload.objects.all().filter(doctype__exact = 2).count()
    num_DrivingLicence = DocUpload.objects.all().filter(doctype__exact = 3).count()
    num_AcademicDocument = DocUpload.objects.all().filter(doctype__exact = 4).count()
    num_OtherDocument = DocUpload.objects.all().filter(doctype__exact = 5).count()

    context = {
            'docs':docs,
            'nin':nin,
            'num_nin':num_nin,
            'num_Passport':num_Passport,
            'num_DrivingLicence':num_DrivingLicence,
            'num_AcademicDocument':num_AcademicDocument,
            'num_OtherDocument':num_OtherDocument,
        }
    return render(request, 'main/basegeneric.html', context)

def contact(request):
    form = ContactForm()

    return render(request, 'lostdoc/contactus.html', {'form':form})

def privacy(request):
    return render(request, 'lostdoc/privacy.html')

def tos(request):
    return render(request, 'lostdoc/tos.html')




    
  