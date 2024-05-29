from django.urls import path,include
from . import views


urlpatterns = [

    path('cvvhome/',views.TaskListview.as_view(),name='cvvhome'),
    path('cvvdetail/<int:id>/', views.TaskDetailview.as_view(), name='cvvdetail')
]
