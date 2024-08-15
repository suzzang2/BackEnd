from django.db import models

# Create your models here.
class Comment(models.Model):
   id = models.AutoField(primary_key=True)
   body = models.TextField(verbose_name="내용")
   writer = models.CharField(verbose_name="작성자", max_length=10)
   user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
   post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)