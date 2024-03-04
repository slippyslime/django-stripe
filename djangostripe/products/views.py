from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import DetailView, ListView
from .models import Item
import stripe

stripe.api_key = 'sk_test_51Oo5YsHONtmivArNXAcmSqn1UtrzsWj8eI1Q6vWNtLLOymNlK68WQhHlZVKA9FNxvdvnwCMYvODWZCBVABRZbcxV00rAcg20BS'

@api_view(['GET'])
def create_checkout_session(request, pk):
    if request.method == "GET":
        item = Item.objects.all()
        item = str(item[pk - 1])
        price = item.split()
        price = price[len(price) - 1].replace('.', '')
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item[:-len(price)-1],
                    },
                    'unit_amount': int(price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        data = {'sessionId': session.id}
        return Response(data)

class ItemListView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "products/item_list.html"


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "items"
    template_name = "products/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data()
        Price = str(self.get_object()).split(' ')[1]
        context["prices"] = Price
        return context


@api_view(["GET"])
def item_detail(request, pk):
    if request.method == "GET":
        items = Item.objects.all()
        items = [items[pk-1]]
        context = {'items': items}
        template_name = "products/item_detail.html"

        return render(request, template_name, context=context)
