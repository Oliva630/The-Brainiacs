from django.urls import path
from APG import views
urlpatterns = [
	path('',views.search,name='search'),
	path('teammates',views.teammates,name='teammates'),
	path('filter',views.filter,name='filter'),
    path('getcontig/<str:c_name>',views.getcontig,name='getcontig'),
	path('background',views.background,name='background'),
	path('visualization',views.visualization,name='visualization'),
]