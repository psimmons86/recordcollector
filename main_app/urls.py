

from django.urls import path
from . import views

urlpatterns = [

    path('labels/', views.LabelList.as_view(), name='label-index'),
    path('labels/<int:pk>/', views.LabelDetail.as_view(), name='label-detail'),
    path('labels/create/', views.LabelCreate.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', views.LabelUpdate.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', views.LabelDelete.as_view(), name='label-delete'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.record_index, name='record-index'),
    path('records/<int:record_id>/', views.record_detail, name='record-detail'),
    path('records/create/', views.RecordCreate.as_view(), name='record-create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='record-update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='record-delete'),
    path('records/<int:record_id>/add_listening/', views.add_listening, name='add-listening'),

    path('records/<int:record_id>/associate_label/<int:label_id>/', views.associate_label, name='associate-label'),
    path('records/<int:record_id>/remove_label/<int:label_id>/', views.remove_label, name='remove-label'),
]
