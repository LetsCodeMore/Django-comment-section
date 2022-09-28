from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now
                                          )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})
