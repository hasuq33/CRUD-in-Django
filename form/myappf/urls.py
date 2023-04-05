from . import views
from django.urls import path 

urlpatterns = [
      path('form/',views.form,name="form"),
      path('login/', views.login, name="login"),
      path('home/', views.home, name="home"),
      path('logout/', views.logout1, name="logout1"),
      path('student/',views.student,name="student"),
      path('table/',views.table,name="table"),
      path('table/<int:student_id>/edit/',views.edit_student, name='edit_student'),
      path('table/<int:student_id>/delete/',views.delete_student, name='delete_student'),

]
