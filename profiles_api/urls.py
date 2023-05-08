from django.urls import path

from profiles_api import views

# hello-view -> name of url
#Mapped to  views.HelloApiView.as_view() class

#When enter addres../api/hello-view -> it will call views.HelloApiView.as_view()
# HelloApiView class will be rendered by url
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]