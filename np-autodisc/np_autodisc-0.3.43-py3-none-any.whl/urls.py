# urls.py

from django.urls import path

from extras.views import ObjectChangeLogView

from np_autodisc import views
from np_autodisc.models import DiscoveryRequest

app_name = 'np_autodisc'
urlpatterns = [

    path('discovery-requests/', views.DiscoveryRequestListView.as_view(), name = 'discoveryrequest_list'),
    path('discovery-requests/<int:pk>/', views.DiscoveryRequestView.as_view(), name = 'discoveryrequest'),
    path('discovery-requests/<int:pk>/delete/', views.DiscoveryRequestDeleteView.as_view(), name = 'discoveryrequest_delete'),
    path('discovery-requests/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name = 'discoveryrequest_changelog', kwargs = {'model': DiscoveryRequest}),
    path('discovery-requests/add/', views.DiscoveryRequestCreateView.as_view(), name = 'discoveryrequest_add'),

]
