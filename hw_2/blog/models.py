# blog/models.py
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
