from django.shortcuts import redirect, render
from cms.models import (
    Slider,
    WebsiteSetting,
    Testimonial,
    Blog,
    OurTeam,
    FAQs,
    CustomerInquiry,
)
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, email, phone, message)
        inquiry = CustomerInquiry.objects.create(
            name=name, email=email, phone=phone, message=message
        )
        inquiry.save()
        return redirect("home_page")
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
    search = request.GET.get("search")
    sorting = request.GET.get("sorting")
    filters = {"status": True}

    if product_category_slug == None:
        products = Product.objects.filter(**filters)

    if product_category_slug:
        filters["product_category__slug"] = product_category_slug
        products = Product.objects.filter(**filters)

    if search:
        filters["name__icontains"] = request.GET.get("search")
        products = Product.objects.filter(**filters)

    if sorting == "low":
        products = Product.objects.filter(**filters).order_by("price")

    if sorting == "high":
        products = Product.objects.filter(**filters).order_by("-price")

    context = {
        "products": products,
    }
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


def FAQsView(request):
    faqs = FAQs.objects.filter(status=True)
    return render(request, "FAQs.html", {"faqs": faqs})


def blog_page(request):
    blogs = Blog.objects.filter(status=True)
    return render(request, "blog/blog.html", {"blogs": blogs})


def blog_detail(request, blog_slug):
    blog = Blog.objects.get(status=True, slug=blog_slug)
    recent_blogs = Blog.objects.filter(status=True)[2:6]
    popular_blogs = Blog.objects.filter(status=True, popular_blog_status=True)
    context = {
        "blog": blog,
        "recent_blogs": recent_blogs,
        "popular_blogs": popular_blogs,
    }
    return render(request, "blog/blog-detail.html", context)

