from django.db import models



# class Feedback(models.Model):
#     feddback_type=[
#         ('suggestion', 'Suggestion'),
#         ('complaint', 'Complaint'),
#         ('appreciation', 'Appreciation'),
#         ('other', 'Other'),
#     ]
#     name = models.CharField(max_length=100 , blank=True)
#     email = models.EmailField(null=True, blank=True)
#     type = models.CharField(max_length=20, choices=feddback_type, blank=True)
#     message = models.TextField( blank=True)
#     rating = models.IntegerField(default=1)    
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Feedback from {self.name}"


from django.db import models

class Feedback(models.Model):
    feedback_type = [  # Fixed spelling
        ('suggestion', 'Suggestion'),
        ('complaint', 'Complaint'),
        ('appreciation', 'Appreciation'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)  # Allow NULL
    email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=feedback_type, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=1)  # Allow user-defined rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'}"
