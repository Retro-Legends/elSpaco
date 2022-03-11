from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),  # root url
    # path('', views.cladiri, name="cladiri"),  # root url
    path('cladiri/', views.cladiri, name="cladiri"),  # root url
    path('cladire/<str:pk>', views.cladire, name="cladire"),
    path('create-cladire/', views.createCladire, name="create-cladire"),
    path('update-cladire/<str:pk>', views.updateCladire, name="update-cladire"),
    path('delete-cladire/<str:pk>', views.deleteCladire, name="delete-cladire"),
    #
    path('birouri/', views.birouri, name="birouri"),  # root url
    path('birou/<str:pk>', views.birou, name="birou"),
    path('create-birou/', views.createBirou, name="create-birou"),
    path('update-birou/<str:pk>', views.updateBirou, name="update-birou"),
    path('delete-birou/<str:pk>', views.deleteBirou, name="delete-birou"),
    #
    path('desks/', views.desks, name="desks"),  # root url
    path('desk/<str:pk>', views.desk, name="desk"),
    path('create-desk/', views.createDesk, name="create-desk"),
    path('update-desk/<str:pk>', views.updateDesk, name="update-desk"),
    path('delete-desk/<str:pk>', views.deleteDesk, name="delete-desk"),
    #
    path('employees/', views.employees, name="employees"),  # root url
    path('employee/<str:pk>', views.employee, name="employee"),
    path('create-employee/', views.createEmployee, name="create-employee"),
    path('update-employee/<str:pk>', views.updateEmployee, name="update-employee"),
    path('delete-employee/<str:pk>', views.deleteEmployee, name="delete-employee"),
    #
    path('remotes/', views.remotes, name="remotes"),  # root url
    path('remote/<str:pk>', views.remote, name="remote"),
    path('create-remote/', views.createRemote, name="create-remote"),
    path('update-remote/<str:pk>', views.updateRemote, name="update-remote"),
    path('delete-remote/<str:pk>', views.deleteRemote, name="delete-remote"),
    #
    path('api_cladiri/', views.apiCladiri, name="api_cladiri"),  # root url
    path('api_offices/', views.apiOffices, name="api_offices"),  # root url
    path('api_desks/', views.apiDesks, name="api_desks"),  # root url
    path('api_employees/', views.apiEmployees,
         name="api_employees"),  # root url
    path('api_remotes/', views.apiRemotes, name="api_remotes"),  # root url
    #
    path('api_cladire/<str:pk>', views.apiCladire,
         name="api_cladire"),  # root url
    path('api_office/<str:pk>', views.apiOffice, name="api_office"),  # root url
    path('api_desk/<str:pk>', views.apiDesk, name="api_desk"),  # root url
    path('api_employee/<str:pk>', views.apiEmployee,
         name="api_employee"),  # root url
    path('api_remote/<str:pk>', views.apiRemote, name="api_remote"),  # root url

]
