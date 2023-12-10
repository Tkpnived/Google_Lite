from django.urls import path
from jobapp import views


urlpatterns = [
    path('home',views.home,name="home"),
    path("",views.login,name="login"),
    path('cal', views.cal, name="cal"),
    path('search/', views.search, name='search'),
    path('retur/<item_id>', views.retur, name='retur'),
    path('Image/<dataid>', views.Image, name='Image'),
    path('Image2/<dataid>', views.Image2, name='Image2'),
    path('catr/<item_id>', views.catr, name='catr'),
    path('ret/<dataid>', views.ret, name='ret'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logins', views.logins, name='logins'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('retcat/<dataid>', views.retcat, name='retcat'),


]