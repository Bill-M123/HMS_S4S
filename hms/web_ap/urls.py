from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('all_participants/', views.All_Participants_ListView.as_view(), name='all_participants'),
path('new_participant/', views.new_participant , name='new_participant'),

]
# Use include() to add paths from the catalog application
# Use include() to add paths from the catalog application
