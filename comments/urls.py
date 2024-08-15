from django.urls import path
from comments.views import *

urlpatterns = [
   path('', comment_basic, name = 'comment_basic'),
   path('<int:id>', get_comment_detail, name = "댓글 조회"),
]