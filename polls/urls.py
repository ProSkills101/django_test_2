from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('mypolls/', views.mypolls, name='mypolls'),
    path('mypolls/create/', views.mypolls_create, name='mypolls-create'),
    path('mypolls/update/<int:question_id>/', views.mypolls_update, name='mypolls-update'),
    path('mypolls/delete/<int:question_id>/', views.mypolls_delete, name='mypolls-delete'),
    path('mypolls/delete/<int:question_id>/choice/<int:choice_id>/', views.mypolls_delete_choice, name='mypolls-delete-choice'),
]