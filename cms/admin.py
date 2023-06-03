from django.contrib import admin, messages

from cms.models import WebsiteSetting, Slider, Blog, FAQs,Testimonial,OurTeam


def active_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=True)
        messages.success(request, "Selected record(s) marked as active")
    except Exception as e:
        messages.error(request, str(e))


def inactive_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=False)
        messages.success(request, "Selected record(s) marked as inactive")
    except Exception as e:
        messages.error(request, str(e))


@admin.register(WebsiteSetting)
class websiteSettingAdmin(admin.ModelAdmin):
    list_display = ["title", "logo", "email", "phone", "address"]
    search_fields = ["title"]


@admin.register(Slider)
class sliderAdmin(admin.ModelAdmin):
    list_display = ["heading", "sub_heading", "image", "status"]
    list_filter = ["status"]
    search_fields = ["heading"]
    actions = (active_status, inactive_status)


@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title","sub_title", "description", "auther", "image", "status"]
    list_filter = ["status"]
    search_fields = ["title"]
    actions = (active_status, inactive_status)
    date_hierarchy = "date_time"


@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
    list_display = ["question", "answer","status"]
    search_fields = ["question"]
    list_filter=['status']
    actions = (active_status, inactive_status)
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "comment","image", "status"]
    search_fields = ["name"]
    list_filter=['status']
    actions = (active_status, inactive_status)
    
@admin.register(OurTeam)
class  OurTeamAdmin(admin.ModelAdmin):
    list_display = ["name", "position","image", "status"]
    search_fields = ["name"]
    list_filter=['status']
    actions = (active_status, inactive_status)
        