from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm, CategoryForm
from .models import Product


def index(request):
    products = Product.objects.order_by("category")
    return render(request, "products.html", context={"products": products})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create_product.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                title=request.POST.get("title"),
                content=request.POST.get("content"),
                author=request.POST.get("author")
            )
            return redirect("product_detail", pk=product.pk)

        return render(
            request,
            "create_product.html",
            {"form": form}
        )


def detail_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", context={"product": product})


def update_product(request, *args, pk, **kwargs):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(initial={
            "title": product.title,
            "author": product.author,
            "content": product.content,
        })
        return render(
            request, "update_product.html",
            context={"form": form}
        )
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, pk=pk)
            product.title = request.POST.get("title")
            product.content = request.POST.get("content")
            product.author = request.POST.get("author")
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