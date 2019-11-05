from django.urls import path
from .import views

app_name = 'sento'

urlpatterns=[ 
    path('add/', views.AddData, name='add'),
    path('list/', views.ListData, name='list'),
    path('rank/', views.Rank, name='rank'),
    path('update/<int:pk>/', views.Update, name='update'),
]