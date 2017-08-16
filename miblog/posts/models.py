from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

# Create your models here.
from django.utils.text import slugify

from django.conf import settings


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    titulo = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to=upload_location,
                               null=True,
                               blank=True,
                               height_field="height_field",
                               width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    contenido = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-actualizado"]


# funcion recursiva para crear el slug

def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
