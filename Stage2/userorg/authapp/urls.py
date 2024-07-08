# authapp/urls.py
from django.urls import path
from django.conf.urls import handler404, handler500
from .views import index,  UserRegView, LoginView, OrganisationListCreateView, OrganisationDetailView, UserDetailView, AddUserToOrganisationView

urlpatterns = [
    path("",index, name="index"),
    path('auth/register/', UserRegView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('api/organisations/', OrganisationListCreateView.as_view(), name='organisation_list'),
    path('api/organisations/<uuid:orgId>/', OrganisationDetailView.as_view(), name='organisation_detail'),
    path('api/users/<uuid:userId>/', UserDetailView.as_view(), name='user_detail'),
    path('api/organisations/<uuid:orgId>/users/', AddUserToOrganisationView.as_view(), name='add_user_to_organisation'),
]

handler404 = 'authapp.views.custom_404_view'
handler500 = 'authapp.views.custom_500_view'