
from django.urls import path
from . import views
from . import course_views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('news_list/',views.NewsListView.as_view(),name='news_list'),
    path('write_news/',views.WriteNewsView.as_view(),name='write_news'),
    path('edit_news/',views.EditNewsView.as_view(),name='edit_news'),
    path('delete_news/',views.delete_news,name='delete_news'),
    path('news_category/',views.news_category,name='news_category'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('edit_news_category/',views.edit_news_category,name='edit_news_category'),
    path('delete_news_category/',views.delete_news_category,name='delete_news_category'),
    path('banners/',views.banners,name='banners'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('banner_list/',views.banner_list,name='banner_list'),
    path('delete_banner/',views.delete_banner,name='delete_banner'),
    path('edit_banner/',views.edit_banner,name='edit_banner'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('qntoken/',views.qntoken,name='qntoken'),
    path('teacher/',views.teacher,name='teacher'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('delete_teacher/',views.delete_teacher,name='delete_teacher'),
    path('edit_teacher/',views.edit_teacher,name='edit_teacher'),
]

# 这是课程相关的url映射
urlpatterns += [
    path('pub_course/',course_views.PubCourse.as_view(),name='pub_course'),
    path('course_list/',course_views.CourseListView.as_view(),name='course_list'),
    path('course_categary/',course_views.Course_Categary,name='course_categary'),
    path('add_course_categary/',course_views.Add_Course_Categary,name='add_course_categary'),
    path('edit_course_category/',course_views.Edit_course_category,name='edit_course_category'),
    path('delete_course_category/',course_views.delete_course_category,name='delete_course_category'),
    path('delete_course/',course_views.Delete_Course,name='delete_course'),
]