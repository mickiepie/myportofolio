from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm
from .models import Project
from main.models import Experience


def show_main(request):
    context = {
        "name": "Ria Lavenia Kharissa",
        "brand": "Laven",
        "npm": "2506543905",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "I am an Information Systems student at the University of Indonesia with a strong passion for business and technology, particularly in web development, design, and product management. "
            "I am someone who loves to learn, is ambitious to grow, and enjoys social activities."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ria Lavenia Kharissa",
        "experience_list": Experience.objects.all(),
        "brand": "Laven"
    }
    return render(request, "experience.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        'name': 'Ria Lavenia Kharissa',
        'brand': 'Laven',
        'project_list': projects,
        'title_query': title_query,
    }

    return render(request, 'projects.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context={
        "name": "Ria Lavenia Kharissa",
        "form": form ,
    }

    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")