from django.urls import path
from . import views


urlpatterns = [
    path('announcement/',views.AnnoucementList),
    path('announcement/<int:pk>',views.AnnouncementDetail)
    
]
