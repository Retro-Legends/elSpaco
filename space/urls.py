from django.urls import path
from . import views


urlpatterns = [

    path('', views.cladiri, name="cladiri"),  # root url
    path('cladire/<str:pk>', views.cladire, name="cladire"),
    path('create-cladire/', views.createCladire, name="create-cladire"),
    path('update-cladire/<str:pk>', views.updateCladire, name="update-cladire"),
    path('delete-cladire/<str:pk>', views.deleteCladire, name="delete-cladire"),


]
