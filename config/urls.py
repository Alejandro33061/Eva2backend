from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventariojuegoApp.urls')),
    path('consolas/', include('consolasApp.urls')),
    path('accesorios/', include('accesoriosApp.urls')), 
]