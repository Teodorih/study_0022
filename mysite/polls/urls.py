from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/update/', views.QuestionUpdateView.as_view(), name='update'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create_form', views.create_form, name='create_form'),
    path('create', views.create, name='create'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('create_choice', views.ChoiceCreateView.as_view(), name='update'),
    path('<int:pk>/update_choice', views.ChoiceUpdateView.as_view(), name='update'),

]