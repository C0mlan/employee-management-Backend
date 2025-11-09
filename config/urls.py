
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/employee/", include("employee.urls")),
    path("api/v1/time/", include("stafftime.urls"))

]