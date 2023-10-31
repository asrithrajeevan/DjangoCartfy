from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProductForm, ProductUpdateForm, ProductDeleteForm
from .models import Product, CartItem
from django.http import Http404

# Create your views here.


# @login_required()
def index(request):
    item_dict = {
        'items' : Product.objects.all
    }
    if request.method == "POST":
        print("it is post")
    return render(request, "home.html", item_dict)



def add_to_cart(request, product_id):
    try:
        product = get_object_or_404(Product,pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product not found....")
    user = request.user 

    # Check if the item is already in the cart, and if so, update the quantity
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_view")  # Redirect to the cart view



def cart_view(request):

    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.product_price * item.quantity for item in cart_items)
    items = len(cart_items)
    for item in cart_items:
        item.total = item.product.product_price * item.quantity 
        total_price += item.total 

    return render(request, "cart.html", {"cart_items": cart_items, "total_price": total_price, "lenght" : items})



def remove_item_from_cart(request, product_id):
    if request.method == "POST":
        try:
            item = get_object_or_404(CartItem, pk=product_id)
            item.delete()

        except CartItem.DoesNotExist:
            raise Http404("Item not found")

        return redirect('cart_view')  # Redirect to the cart view after item removal

    return HttpResponse(status=405)




def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect("register") # register is a url name
    
    
    form = UserForm()
    reg_form={
        "form" : form
    }
    return render(request, "registration/registration.html", reg_form)



# for adding new product
def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST,  request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print("Form is valid")
        else:
            print("product not valid")

    form = ProductForm()
    item_form={
        "form" : form
    }
    return render(request,"newproduct.html", item_form)



# for updating new prodduct
def update_product(request):
    try:
        item_id = 1  # we can enter the item id for updating item
        product = Product.objects.get(pk=item_id)
    except Product.DoesNotExist:
        raise Http404("Given query not found....")
    print(product.product_name)
    
    if request.method == "POST":
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Updated")
    else:
        form = ProductUpdateForm(instance=product)
    
    context = {
        "form": form,
        "product": product
    }
    return render(request, "update_product.html", context)



# delete product
def delete_product(request):
    try:
        item_id = 1  # we can enter the item id for deleting item
        product = Product.objects.get(pk=item_id)
    except Product.DoesNotExist:
        raise Http404("Given query not found....")
    
    if request.method == "POST":
        product.delete()
        return redirect("product_list")  # Redirect to the product list view after deletion
    else:
        form = ProductDeleteForm(instance=product)

    context = {
        "form": form,
        "product": product
    }
    return render(request, "delete_product.html", context)