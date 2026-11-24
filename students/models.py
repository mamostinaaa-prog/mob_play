from django.db import models

# мяу
class Students(models.Model):
    first_name = models.CharField("Имя", max_length = 32)
    second_name = models.CharField("Фамилия", max_length = 32)
    middle_name = models.CharField("Отчество", max_length = 32)
    in_group = models.ForeignKey("Group", models.PROTECT, verbose_name= "Группа", default= None, null=True, related_name="students")
    age = models.IntegerField("Возраст")
    
    def __str__(self):
        return f"{self.second_name} {self.first_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

class Group(models.Model):
    title = models.CharField ("Название", max_length=10)
    course = models.IntegerField ('course', default=1)

    def __str__ (self):
        return f"{self.title} ({self.course})"

    class Meta: 
        verbose_name = "Группа"
        verbose_name_plural = "Группы"