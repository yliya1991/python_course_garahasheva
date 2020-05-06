from django.db import models

class Teacher(models.Model):
    course = models.PositiveIntegerField()
    course_student_supervisor = models.PositiveIntegerField()
    lecturer = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def full_group(self):
        return f'{self.coourse} {self.course_student_supervisor} {self.lecturer} {self.first_name} {self.last_name}'

    def info(self):
        return f'{self.course} {self.course_student_supervisor} {self.lecturer}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'