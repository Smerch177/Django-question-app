from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('quiz', views.quiz),
    path('quiz/answer', views.quiz_answer),
    path('quiz/make', views.quiz_make),
    path('quiz/create', views.quiz_create),
    path('quiz_create_random', views.quiz_create_random)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


