from django.urls import path, include
from . import views
from .views import contact,services, privacy,tos, newUpload, docSearch, docRequest,serviceRequest, doc_detail_view,document_type_detail, notFoundDoc, userSearch, newDocumentType, aboutUs, navigation,newDocTest

#Create your url patterns here
urlpatterns = [
    path('', views.index, name = 'home'),
    path('aboutus/', views.aboutUs, name = 'aboutus'),
    path('contactus/', views.contact, name = 'contactus'),
    path('services/', views.services, name = 'services'),
    path('privacy/', views.privacy, name = 'privacy'),
    path('tos/', views.tos, name = 'tos'),
    path('navigation', views.navigation, name = 'nav'),
    path('upload/', views.newUpload, name= 'upload'),
    path('type/add/', views.newDocumentType, name= 'adddoctype'),
    path('type/addme/', views.newDocTest, name= 'addtest'),
    path('search/', views.docSearch, name = 'docsearch'),
    path('usersearch/', views.userSearch, name = 'usersearch'),
    path('docdetail/<int:pk>/', views.doc_detail_view, name = 'docdetail'),
    path('request/<int:doc_id>/make_request/', views.docRequest, name = 'docrequest'),
    path('doctypedetail/<int:pk>/', views.document_type_detail, name = 'doctypedetail'),
    path('service/<int:doctype_id>/request/', views.serviceRequest, name = 'servicerequest'),
    path('notfound/', views.notFoundDoc, name = 'notfound' ),
]