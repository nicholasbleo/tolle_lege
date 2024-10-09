from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('', views.library, name='library'),
    path('<int:book_id>/', views.book_pages, name='book_pages'),
    path('<int:book_id>/<int:page_id>/', views.book_page, name='page'),
    path('parse/', views.parse_morpheme, name='parse')
]