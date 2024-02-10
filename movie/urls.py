from django.urls import path
from . import views

app_name ='moviesapp'

urlpatterns = [
    path('',views.homeview,name='homeview'),
    path('detail/<int:m_id>/',views.details,name='detail'),
    path('update/<int:mv_id>/',views.update,name='update'),
    path('delete/<int:d_id>/',views.delete,name='delete'),
]
