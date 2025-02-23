from django.db import models

class Thread(models.Model):
    name = models.CharField(("Название"), max_length=255)
    description = models.TextField(("Описание"))

    def _str_(self):
        return self.name
class Post(models.Model):
    title = models.CharField(("Заголовок"), max_length=255)
    description = models.TextField(("Текст"))
    author = models.CharField(("Автор"), max_length=255)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')


    def _str_(self):
        return self.title