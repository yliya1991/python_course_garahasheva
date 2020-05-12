from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return f'{self.id} {self.first_name} {self.last_name}' # noqa

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def inc_age(self) -> None:
        self.age += 1
        self.save()
