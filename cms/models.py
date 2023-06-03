from django.db import models
from django.template.defaultfilters import slugify
""" model for cms class to dynamic logo, heading, content  """


class WebsiteSetting(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return self.title


class Slider(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.heading} {self.sub_heading}"


class Blog(models.Model):
    title = models.CharField(max_length=29)
    sub_title=models.TextField(max_length=123)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    auther = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    status = models.BooleanField(default=True)

    def __str__(self): 
        return f"{self.title}{self.auther}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)



class FAQs(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial')
    name=models.CharField(max_length=255)
    comment = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class OurTeam(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='our_team')
    position=models.CharField(max_length=255)
    status=models.BooleanField(default=True)    