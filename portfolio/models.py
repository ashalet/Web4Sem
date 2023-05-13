from django.db import models


class Assets(models.Model):
    name_of_work = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='portfolio/static/portfolio/img/', unique=True)
    duration = models.IntegerField(default=None)

    def __str__(self):
        return self.name_of_work

    class Meta:
        verbose_name = "Работa"
        verbose_name_plural = "Работы"
        ordering = ['id']


class Work(models.Model):
    asset = models.OneToOneField(Assets, on_delete=models.CASCADE)
    description = models.CharField(max_length=4096)
    start_date = models.DateField()
    end_date = models.DateField()
    blender = models.BooleanField(null=True)
    photoshop = models.BooleanField(null=True)
    zbrush = models.BooleanField(null=True)
    bdf = models.BooleanField(null=True)

    def __str__(self):
        return str(self.asset)

    class Meta:
        verbose_name = "Работa_полн."
        verbose_name_plural = "Работы_полн."
        ordering = ['id']


class Render(models.Model):
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    render_image_path = models.ImageField(upload_to='portfolio/static/portfolio/img/', unique=True)

    def __str__(self):
        return str(self.asset)

    class Meta:
        verbose_name = "Рендер"
        verbose_name_plural = "Рендеры"
        ordering = ['id']


class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    date = models.DateField('Дата публикации')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
