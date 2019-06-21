from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product_id=product.id)

    if 'reviewed_products' not in request.session.keys():
        request.session['reviewed_products'] = {}

    is_review_exist = request.session['reviewed_products'].get(f'{pk}', False)

    if request.method == 'GET':
        form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid() and not is_review_exist:
            review = Review(text=form.cleaned_data['text'], product_id=pk)
            review.save()
            request.session['reviewed_products'][f'{pk}'] = is_review_exist = True
            request.session.modified = True

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
