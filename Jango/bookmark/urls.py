from django.urls import path
from .views import *

urlpatterns = [
    path("", BookmarkListView.as_view(), name = 'list'), # as_view() : 뒤에 오는게 없으면 Bookmark 보여줌
]