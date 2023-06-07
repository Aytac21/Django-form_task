from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def list_view(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, "list.html", context)



def create_view(request):

    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product:list")

    context = {
        "form": form,
    }
    return render(request, "create.html", context)

