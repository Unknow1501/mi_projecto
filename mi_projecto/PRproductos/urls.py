# PRproductos/urls.py
from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDetailView, ProductoDeleteView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:pk>/borrar/', ProductoDeleteView.as_view(), name='borrar_producto'),
]
# PRproductos/urls.py
from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDetailView, CategoriaDeleteView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalle_categoria'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:pk>/borrar/', CategoriaDeleteView.as_view(), name='borrar_categoria'),
]
