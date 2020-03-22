from django.urls import path




app_name = 'ursitey'
# Aquire views.py
try:
    from .import views
except:
    print('Unable to import views. Please check ursitey/urls.py for more information.' + '\n'
          +'Thank You')

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    # e.g URL: /polls/#/results/
    # -> Result for question #
    path('<int:post_id>/results/', views.results, name='results'),
    # e.g URL: /polls/#/vote/
    # -> You've voted for question #
    path('<int:post_id>/about/', views.vote, name='about'),
]