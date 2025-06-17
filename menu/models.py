from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return self.url or '#'
        return self.url or '#'
