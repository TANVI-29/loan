from django.db import models

# Create your models here.


class Feedback(models.Model):
    feddback_type=[
        ('suggestion', 'Suggestion'),
        ('complaint', 'Complaint'),
        ('appreciation', 'Appreciation'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=feddback_type,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')],null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"