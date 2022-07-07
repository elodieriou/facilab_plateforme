"""facilab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import authentication.views
from django.contrib import admin
from django.urls import path
from plateform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPage.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('user-type/', authentication.views.user_type, name='user-type'),
    path('user-type/applicant', authentication.views.SignupApplicant.as_view(), name='user-applicant'),
    path('user-type/fablab', authentication.views.SignupFablab.as_view(), name='user-fablab'),
    path('profile/<id>/', authentication.views.detail_profile, name='profile-applicant'),
    path('profile/<id>/update/', authentication.views.update_profile, name='update-profile'),
    path('home/', views.home_page, name='home-page'),
    path('my-requests/', views.list_requests, name='list-request'),
    path('all-requests/applicant/', views.table_request, name='table-request'),
    path('all-requests/fablab/', views.table_request_fablab, name='table-request-fablab'),
    path('requests/create/', views.create_request, name='create-request'),
    path('detail-request-from-mylist-applicant/<id>/', views.detail_request_list_applicant,
         name='detail-request-list-applicant'),
    path('detail-request-from-table-applicant/<id>/', views.detail_request_table_applicant,
         name='detail-request-table-applicant'),
    path('requests-fablab/<id>/', views.detail_request_fablab, name='detail-request-fablab'),
    path('requests/<pk>/update/', views.UpdateRequest.as_view(), name='update-request'),
    path('requests/<pk>/delete/', views.DeleteRequest.as_view(), name='delete-request'),
]
