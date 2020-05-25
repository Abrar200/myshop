from django.urls import path
from . import views
from .views import  homeview, ItemDetailView

urlpatterns = [
	path('', homeview.as_view(), name='myshop-home'),
	# path('', views.FilterView, name='myshop-home'),
	path('product/<slug>', ItemDetailView.as_view(), name='product'),
	path('s/', views.search, name='search'),
	path('about/', views.about, name='myshop-about'),
	path('contact/', views.contact, name='myshop-contact'),
	# path('', views.home, name='myshop-home'),
]