from django.db import models


class QuizHistory(models.Model):
    username = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    score = models.IntegerField()
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.material} - {self.score}"

    class Meta:
        ordering = ['-created_at']
