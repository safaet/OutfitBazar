from django.contrib import admin
from django.urls import path, include
from store import views
from django.http import HttpResponse


def accounts(request):
    return HttpResponse("This is the accounts page.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password change/reset
    path('accounts/', include('store.urls')),  # Your custom signup URL
    # path('accounts/', accounts, name='accounts'),  # Custom accounts view
]

