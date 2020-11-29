import django_filters
from .models import DocUpload

#Create your filters here
class DocSearchFilter(django_filters.FilterSet):
    class Meta:
        model = DocUpload
        fields = ['doc_surname','doc_givenname']