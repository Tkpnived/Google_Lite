from django.urls import path
from adminapp import views


urlpatterns = [
    path('web/',views.web,name="web"),
    path('table/', views.table, name="table"),
    path('cats/', views.cats, name="cats"),
    path('deletecat/<int:dataid>', views.deletecat, name="deletecat"),

]