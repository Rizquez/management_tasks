from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from tasks import views

# api versioning
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API'))
]

# Estas lineas de codigo se encargan de generar de manera automatica
# las peticiones de tipo GET, POST, PUT y DELETE para no tener que 
# realizarlas manualmente