from django import views
from django.contrib import admin
from django.urls import path, include
from crudapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(), name='index'),
    path('add/',views.AddView.as_view(), name='add'),
    path('<slug:slug>/',views.SingleView.as_view(), name='single'),
    path('edit/<int:pk>',views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>',views.DeleteView.as_view(), name='delete'),

]
