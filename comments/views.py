from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가
from django.views.decorators.http import require_http_methods
from comments.models import *

# Create your views here.

def comment_basic(request):
   if request.method == "GET":
      return JsonResponse({
         'status' : 200,
         'data' : "This is comment defualt page"
      })
   
def index(request):
   return render(request, 'index.html')

@require_http_methods(["GET"])
def get_comment_detail(request,id):
   comment = get_object_or_404(Comment, pk=id)
   comment_detail_json = {
      "id" : comment.id,
      "body" : comment.body,
      "writer" : comment.writer,
      # "user_id" : comment.user_id,
      # "post_id" : comment.post_id,
   }

   return JsonResponse({
      'status' : 200,
      'message' : '댓글 조회 성공',
      'data' : comment_detail_json
   })