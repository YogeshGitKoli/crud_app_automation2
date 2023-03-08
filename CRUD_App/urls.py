from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('AllData/',views.AllData.as_view(),name='AllData'),
    path('AddData/',views.AddData.as_view(),name='AddData'),
    path('UpdateData/<pk>',views.UpdateData.as_view(),name='UpdateData'),
    path('DeleteData/<pk>',views.DeleteData.as_view(),name='DeleteData'),
    
    #SECURITY URLS
    path('SignUp/',views.SignUpUser.as_view(),name='signup'),
    path('SignIn/',views.SignInUser.as_view(),name='signin'),
    path('PasswordChange/',views.PasswordChangeUser.as_view(),name='passchange'),
    path('PassChangeDone/',views.PassChangeDoneUser.as_view()),
    path('SignOut/',views.SignOutUser.as_view(),name='logout'),
    
]
