from django.urls import path

from .views import MemberList, MemberDetail

urlpatterns = [
    path("api/members/", MemberList.as_view()),
    path("api/members/<int:pk>/", MemberDetail.as_view()),
]
