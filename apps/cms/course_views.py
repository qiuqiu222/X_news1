#encoding: utf-8
from django.shortcuts import render
from .forms import PubCourseForm,AddCourseCategaryForm,EditCourseCategoryForm
from apps.course.models import Course,CourseCategory,Teacher
from django.views.generic import View
from utils import restful
from django.views.decorators.http import require_POST,require_GET
from datetime import datetime
from django.utils.timezone import make_aware
from urllib import parse
from django.core.paginator import Paginator

class PubCourse(View):
    def get(self,request):
        context = {
            'categories': CourseCategory.objects.all(),
            'teachers': Teacher.objects.all()
        }
        return render(request,'cms/pub_course.html',context=context)

    def post(self,request):
        form = PubCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get("cover_url")
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            teacher_id = form.cleaned_data.get('teacher_id')

            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)

            Course.objects.create(title=title, video_url=video_url, cover_url=cover_url, price=price, duration=duration,
                                  profile=profile, category=category, teacher=teacher)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


def Course_Categary(request):
    course_categories = CourseCategory.objects.all()
    context = {
        'course_categories':course_categories
    }
    print(course_categories
    )
    return render(request,'cms/course_categary.html',context=context)

@require_POST
def Add_Course_Categary(request):
    form = AddCourseCategaryForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        exists = CourseCategory.objects.filter(name=name).exists()
        if exists:
            return restful.params_error(message="该分类已经存在")
        CourseCategory.objects.create(name=name)
        return restful.ok()

@require_POST
def Edit_course_category(request):
    forms = EditCourseCategoryForm(request.POST)
    if forms.is_valid():
        pk = forms.cleaned_data.get('pk')
        name = forms.cleaned_data.get('name')
        exist = CourseCategory.objects.filter(name=name).exists()
        if exist:
            return restful.params_error("该分类已存在")
        try:
            CourseCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error("该分类不存在")
    else:
        return restful.params_error(message=forms.get_errors())

@require_POST
def delete_course_category(request):
    pk = request.POST.get('pk')
    CourseCategory.objects.filter(pk=pk).delete()
    return restful.ok()

class CourseListView(View):
        def get(self, request):
            # request.GET：获取出来的所有数据，都是字符串类型
            page = int(request.GET.get('p', 1))
            start = request.GET.get('start')
            end = request.GET.get('end')
            title = request.GET.get('title')
            # request.GET.get(参数,默认值)
            # 这个默认值是只有这个参数没有传递的时候才会使用
            # 如果传递了，但是是一个空的字符串，那么也不会使用默认值
            category_id = int(request.GET.get('category', 0) or 0)

            courses = Course.objects.select_related('category', 'teacher')

            if start or end:
                if start:
                    start_date = datetime.strptime(start, '%Y/%m/%d')
                else:
                    start_date = datetime(year=2018, month=6, day=1)
                if end:
                    end_date = datetime.strptime(end, '%Y/%m/%d')
                else:
                    end_date = datetime.today()
                courses = courses.filter(pub_time__range=(
                make_aware(start_date), make_aware(end_date)))

            if title:
                courses = courses.filter(title__icontains=title)

            if category_id:
                courses = courses.filter(category=category_id)

            paginator = Paginator(courses, 2)
            page_obj = paginator.page(page)

            context_data = self.get_pagination_data(paginator, page_obj)

            context = {
                'categories': CourseCategory.objects.all(),
                'courses': page_obj.object_list,
                'page_obj': page_obj,
                'paginator': paginator,
                'start': start,
                'end': end,
                'title': title,
                'category_id': category_id,
                'url_query': '&' + parse.urlencode({
                    'start': start or '',
                    'end': end or '',
                    'title': title or '',
                    'category': category_id or ''
                })
            }

            print('=' * 30)
            print(category_id)
            print('=' * 30)

            context.update(context_data)

            return render(request, 'cms/course_list.html', context=context)

        def get_pagination_data(self, paginator, page_obj, around_count=2):
            current_page = page_obj.number
            num_pages = paginator.num_pages

            left_has_more = False
            right_has_more = False

            if current_page <= around_count + 2:
                left_pages = range(1, current_page)
            else:
                left_has_more = True
                left_pages = range(current_page - around_count, current_page)

            if current_page >= num_pages - around_count - 1:
                right_pages = range(current_page + 1, num_pages + 1)
            else:
                right_has_more = True
                right_pages = range(current_page + 1,
                                    current_page + around_count + 1)

            return {
                # left_pages：代表的是当前这页的左边的页的页码
                'left_pages': left_pages,
                # right_pages：代表的是当前这页的右边的页的页码
                'right_pages': right_pages,
                'current_page': current_page,
                'left_has_more': left_has_more,
                'right_has_more': right_has_more,
                'num_pages': num_pages
            }

@require_POST
def Delete_Course(request):
    pk = request.POST.get('pk')
    try:
        Course.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该课程不存在')
