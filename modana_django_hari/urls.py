from django.urls import path
from django.urls import include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/users/", include("users.urls", namespace="users")),
]
