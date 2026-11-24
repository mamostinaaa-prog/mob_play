from django.shortcuts import render, redirect, get_object_or_404
from students.models import Students, Group


def get_student_list(request):
    context = {
        "students": Students.objects.all(),
        "edu_title": "2026/2027"
    }
    return render(request, 'students/students_list.html', context)


def get_index(req):
    return render(req, 'index.html')


def get_group_list(req):
    data = {
        'groups': Group.objects.all()
    }
    return render(req, 'group/group_list.html', context=data)


def get_group_detail(req):
    data = {
        'group': get_object_or_404(Group, pk=req.GET.get('pk'))
    }
    return render(req, 'group/group_detail.html', context=data)


def get_student_info(req):
    if "s_id" not in req.GET:
        return redirect('students_list')

    student = Students.objects.filter(pk=req.GET['s_id']).first()

    if student is None:
        return render(req, 'students/detail.html', context={}, status=404)

    return render(req, 'students/detail.html', context={'student': student})
