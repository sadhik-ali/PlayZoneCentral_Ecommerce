from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView

# Cart
from .models import Category, Product, LogoSectionProduct
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

import stripe
from django.conf import settings
from django.views import View


class index(TemplateView):
  template_name ="web/index.html" 
   
  def get_context_data(self, **kwargs) :
      context = super().get_context_data(**kwargs)
      context["categories"] = Category.objects.all()
      context["product"] = Product.objects.all()
      context["ProuctLogo"] = LogoSectionProduct.objects.all()
      context["display_categories"] = Category.objects.filter(display_in_home=True)
      return context
  
class detail_page(DetailView):
  template_name ="web/detail_page.html" 
  model = Product



stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        products = Product.objects.all()
        line_items = []
        for product in products:
            line_items.append({
                "price_data": {
                    "currency": "INR",
                    "unit_amount": int(product.price) * 100,
                    "product_data": {
                        "name": product.name,
                        # Add other product details if needed
                    },
                },
                "quantity": 1,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url='http://localhost:8000/thanks',
            cancel_url='http://localhost:8000/than',
        )
        return redirect(checkout_session.url)




    def post(self, request, *args, **kwargs):
        products = Product.objects.all()
        line_items = []
        for product in products:
            line_items.append({
                "price_data": {
                    "currency": "INR",
                    "unit_amount": int(product.price) * 100,
                    "product_data": {
                        "name": product.name,
                        # Add other product details if needed
                    },
                },
                "quantity": 1,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url='http://localhost:8000/thanks',
            cancel_url='http://localhost:8000/than',
        )
        return redirect(checkout_session.url)



class SuccessView(TemplateView):
    template_name = "web/payment/success.html"

class CancelView(TemplateView):
    template_name = "web/payment/cancel.html"



def checkout(request):
  return render(request, 'web/checkout.html')




def success(request):
  return render(request, 'web/success.html')



@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')

