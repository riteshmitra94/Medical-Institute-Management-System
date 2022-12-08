from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),

    path('institutions/', views.showInstitutions, name="institutions"),
    path('addInstitute/', views.addInstitution, name="addInstitute"),

    path('register/', views.Register, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('institute/<str:inst_Id>/',views.showInstituteInfo, name="institute"),
    path('update_institute/<str:inst_Id>/',views.updateInstituteInfo, name="updateInstitute"),
    #path('user/', views.showUserInfo, name="user")
]