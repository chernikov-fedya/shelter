from django.db import models
from django.utils.datetime_safe import date
from django.utils.text import slugify
from django.urls import reverse

class Gender(models.Model):
    gender = models.CharField("Пол", max_length=30)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Breed(models.Model):
    name = models.CharField("Порода животного", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Type(models.Model):
    name = models.CharField("Вид животного", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"

class Vaccination(models.Model):
    name = models.CharField("Прививки", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Прививка"
        verbose_name_plural = "Прививки"

class Size(models.Model):
    name = models.CharField("Размер", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

class Age(models.Model):
    name = models.CharField("Возраст", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возраста"

class Temperament(models.Model):
    name = models.CharField("Темперамент", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Темперамент"
        verbose_name_plural = "Темпераменты"
    
class Animal(models.Model):
    name = models.CharField("Кличка", max_length=60)
    type = models.ForeignKey(Type, verbose_name="вид", on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, verbose_name="порода", on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField("Вес", default=0)
    gender = models.ForeignKey(Gender, verbose_name="пол", related_name="animal_gender", on_delete=models.CASCADE)
    number = models.IntegerField("Номер", default="")
    age = models.ForeignKey(Age, verbose_name="возраст", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="animal/", default="default.jpg")
    extra_photo = models.ImageField("Дополнительное фото", upload_to="animal/", default="default.jpg")
    size = models.ForeignKey(Size, verbose_name="размер", on_delete=models.CASCADE)
    description = models.TextField("Описание", default="")
    go_to_shelter = models.DateField("Дата поступления в приют", default=date.today)
    temperament = models.ForeignKey(Temperament, verbose_name="темперамент", on_delete=models.CASCADE)
    character = models.TextField("Характер",default="")
    health = models.CharField("Здоровье", max_length=100,default="")
    #vaccination = models.ForeignKey(Vaccination, verbose_name="прививки", on_delete=models.CASCADE)
    sterilize = models.BooleanField("Стерилизация", default="")
    video = models.FileField("Видео",upload_to="upload_location",blank=True,null=True)
    needs = models.CharField("Нужды", max_length=100, default="")
    in_shelter = models.BooleanField("Нахождение в приюте", default=True)
    draft = models.BooleanField("Черновик", default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('appShelter:animalcard',
                           args=[self.id, self.slug])

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

class Rewies(models.Model):
    #Отзывы
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    animal = models.ForeignKey(Animal, verbose_name="Животное", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.animal}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
#name: 123
#password: 123
