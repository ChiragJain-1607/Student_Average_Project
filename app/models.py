from django.db import models

# Create your models here.

# students/models.py

from django.db import models

class AveragePercentage(models.Model):
    average_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Average Percentage: {self.average_percentage}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    maths_marks = models.DecimalField(max_digits=5, decimal_places=2)
    science_marks = models.DecimalField(max_digits=5, decimal_places=2)
    hindi_marks = models.DecimalField(max_digits=5, decimal_places=2)
    english_marks = models.DecimalField(max_digits=5, decimal_places=2)
    sanskrit_marks = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        self.total_marks = (self.maths_marks + self.science_marks +
                            self.hindi_marks + self.english_marks +
                            self.sanskrit_marks)

        if self.total_marks > 0:
            self.percentage = (self.total_marks / 500) * 100

        super().save(*args, **kwargs)

             # Update average percentage after saving student
        AveragePercentage.objects.update_or_create(
            id=1,
            defaults={'average_percentage': Student.objects.aggregate(avg=models.Avg('percentage'))['avg']}
        )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @classmethod
    # def average_percentage(cls):
    #     total_students = cls.objects.count()
    #     if total_students > 0:
    #         total_percentage = cls.objects.aggregate(total_percentage=models.Sum('percentage'))['total_percentage']
    #         return total_percentage / total_students
    #     else:
    #         return 0

