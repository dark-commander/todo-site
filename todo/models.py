from django.db import models
from django.utils import timezone
from crispy_forms.helper import FormHelper



class Todo(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

