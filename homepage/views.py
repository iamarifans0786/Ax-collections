from django.http import HttpResponse
from django.shortcuts import render
from cms.models import Slider, WebsiteSetting, Testimonial, Blog, OurTeam
from product.models import ProductCategory, ProductTags, Product


def home_page(request):
    sliders = Slider.objects.filter(status=True)
    product_categories = ProductCategory.objects.filter(status=True, show_homepage=True)
    product_tags = ProductTags.objects.filter(status=True)
    fashion_product_one = Product.objects.filter(status=True, show_homepage=True)[0:2]
    fashion_product_two = Product.objects.filter(status=True, show_homepage=True)[2:4]
    testimonials = Testimonial.objects.filter(status=True)
    blogs = Blog.objects.filter(status=True)[1:3]
    context = {
        "sliders": sliders,
        "product_categories": product_categories,
        "fashion_product_one": fashion_product_one,
        "fashion_product_two": fashion_product_two,
        "testimonials": testimonials,
        "blogs": blogs,
        "product_tags": product_tags,
    }
    return render(request, "home/home.html", context)


def contact_page(request):
    address = WebsiteSetting.objects.all()
    context = {"address": address}
    return render(request, "contact/contact.html", context)


def about_page(request):
    our_teams = OurTeam.objects.filter(status=True)
    testimonials = Testimonial.objects.filter(status=True)
    context = {
        "testimonials": testimonials,
        "our_teams": our_teams,
    }
    return render(request, "about/about.html", context)


def product_page(request, product_category_slug=None):
    products = Product.objects.filter(status=True)
    context = {
        "products": products,
    }
    if product_category_slug:
        products = Product.objects.filter(
            status=True, product_category__slug=product_category_slug
        )
        context = {
            "products": products,
        }
        return render(request, "product/product.html", context)
    return render(request, "product/product.html", context)


def product_detail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        similer_products = Product.objects.filter(
            status=True, product_category=product.product_category
        ).exclude(id=product.id)
        context = {
            "product": product,
            "similer_products": similer_products,
        }
        return render(request, "product/product-detail.html", context)
    except product.DoesNotExist:
        pass
