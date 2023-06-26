from. import views
from django.urls import path

urlpatterns = [

    path('',views.function,name='function'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')

]
