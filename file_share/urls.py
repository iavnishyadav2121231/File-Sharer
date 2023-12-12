from . import views
from django.urls import path,include

urlpatterns = [
    #home
    path("",views.home_page,name='home_page'),
    
    #login_signup
    path("login/",views.login_page,name='login_page'),
    path("login",views.login_x,name='login_x'),
    path("logout/",views.logout_x,name='logout_x'),
    path("signup/",views.signup_page,name='signup_page'),
    path("register",views.register,name='register'),

    #file functions
    path("viewfiles/",views.view_files,name='view_files'),
    path("uploadfile/",views.upload_file,name='upload_file'),
    path("uploadfile/uploadfile_submit",views.upload_file_submit,name='upload_file_submit'),
    path("share/",views.share,name='share'),
    path('profile/<email>/', views.profile),
    path('delete/files/<file>/', views.delete_x)
    
]
