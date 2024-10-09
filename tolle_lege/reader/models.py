from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="pages")
    page_num = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    class Meta:
        ordering = ["book", "page_num"]

    def get_absolute_url(self):
        return f'/reader/{self.book.pk}/{self.pk}/'

    def __str__(self):
        return f"{self.book} - {self.page_num} - {self.title}"


class Morpheme(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="words")
    morpheme = models.CharField(max_length=50)
    page_index = models.IntegerField()
    parse = models.TextField("parse")

    class Meta:
        ordering = ["page_index"]
        unique_together = ('page', 'page_index')

    def __str__(self):
        return self.morpheme
