from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def get_id(self):
        if self.parent:
            return self.parent.get_id() + [self.parent.id]
        else:
            return []

    def children(self):
        return self.menuitem_set.all()

    def __str__(self):
        return self.name
    