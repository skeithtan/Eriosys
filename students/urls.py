from django.conf.urls import url
from .views import *


student_urls = [
    url(r'students/$', StudentListCreateView.as_view()),
    url(r'students/(?P<pk>(\d+))/$', StudentUpdateDestroyRetrieveView.as_view()),
]

residency_urls = [
    url(r'students/(?P<student_id>(\d+))/residency/$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/residency/(?P<residencyaddresshistory_id>(\d+))/$', ResidencyAddressHistoryUpdateDestroyRetrieveView.as_view()),
]

student_program_urls = [
    url(r'students/(?P<student_id>(\d+))/programs/$', StudentProgramListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/programs/(?P<program_offering_id>(\d+))$', StudentProgramUpdateDestroyRetrieveView.as_view()),

]
