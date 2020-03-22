from django.db import models
from django.forms import TextInput, Textarea
# import timezone
from django.utils import timezone
# import datetime
import datetime




class Post(models.Model):
    post_title = models.CharField(max_length=125)
    post_content = models.TextField(max_length=2500)
    post_image = models.ImageField(blank=False)

    def __str__(self):
        return self.post_title
        return self.post_content

    published_date = models.DateTimeField('Date Published')

    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)




class Choice(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=450)

    def __str__(self):
        return self.choice_text

    # ↓Field ↓Model
    votes = models.IntegerField(default=0)