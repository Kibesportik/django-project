from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product, Category, Order
from .forms import ProductCreationForm, CategoryCreationForm, OrderForm

class IndexView(ListView):
    template_name = 'index.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.prefetch_related('products').all()

class CreateOrder(CreateView):
    template_name = 'index.html'
    form_class = OrderForm
    model = Order
    success_url = '/'

    def form_valid(self, form):
        form.instance.product = Product.objects.get(id=self.kwargs['product_id'])
        self.form = form.save()
        return JsonResponse({},status=200)

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

def product_search(request):
    search_word = request.GET.get('search_word', '')
    products = Product.objects.filter(name__icontains=search_word)
    for i in products:
        print(i.name)
    product_list = list(products.values('id', 'name','price','description'))
    return JsonResponse(product_list, safe=False, status=200)
