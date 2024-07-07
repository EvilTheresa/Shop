from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm, CategoryForm
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "products.html", context={"products": products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

def detail_product(request, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def update_product(request, *args, pk, **kwargs):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(initial={
            "name": product.name,
            "price": product.price,
            "image": product.image,
        })
        return render(
            request, "update_product.html",
            context={"form": form}
        )
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, pk=pk)
            product.name = request.POST.get("name")
            product.image = request.POST.get("image")
            product.price = request.POST.get("price")
            product.save()
            return redirect("detail_product.html", pk=product.pk)
        else:
            return render(
                request,
                "update_product.html",
                {"form": form}
            )


def delete_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", context={"product": product})
    else:
        product.delete()
        return redirect("products")