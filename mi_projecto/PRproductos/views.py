from django.shortcuts import render, get_object_or_404, redirect 
from .models import Producto 
from django.views import View 
from django.views.generic import ListView

from .models import Categoria
from django.views import View
from django.views.generic import ListView


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'


class ProductoCreateView(View):
    def get(self, request):
        return render(request, 'crear_producto.html')

    def post(self, request):
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        Producto.objects.create(nombre=nombre, fecha=fecha, descripcion=descripcion)
        return redirect('lista_productos')


class ProductoUpdateView(View):
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        return render(request, 'editar_producto.html', {'producto': producto})

    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.nombre = request.POST.get('nombre')
        producto.fecha = request.POST.get('fecha')
        producto.descripcion = request.POST.get('descripcion')
        producto.save()
        return redirect('lista_productos')


class ProductoDetailView(View):
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        return render(request, 'eliminar_productos.html', {'producto': producto})


class ProductoDeleteView(View):
    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return redirect('lista_productos')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'


class CategoriaCreateView(View):
    def get(self, request):
        return render(request, 'crear_categoria.html')

    def post(self, request):
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('lista_categorias')


class CategoriaUpdateView(View):
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        return render(request, 'editar_categoria.html', {'categoria': categoria})

    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.save()
        return redirect('lista_categorias')


class CategoriaDetailView(View):
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        return render(request, 'eliminar_categoria.html', {'categoria': categoria})


class CategoriaDeleteView(View):
    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect('lista_categorias')



    
    

# Create your views here.
