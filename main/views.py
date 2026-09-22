from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, ExperienceForm
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
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    if title_query:
        experiences=experiences.filter(title__icontains=title_query)
    context = {
        "name": "Ria Lavenia Kharissa",
        "experience_list": experiences,
        "brand": "Laven",
        "title_query": title_query,
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
        "brand": "Laven",
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

def create_experience(request):
    form= ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {
        'form': form,
        'brand': "Laven",
        'name':"Ria Lavenia Kharissa"

    }
    return render(request, "create_experience.html", context)

def edit_experience(request, id):
    experience= get_object_or_404(Experience, pk=id)
    form=ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {'form': form, 'experience': experience, 'name': 'Ria Lavenia Kharissa'}
    return render(request, "edit_experience.html", context)

def delete_experience(request, id):
    experience= get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect('main:show_experience')
    return redirect('main:show_experience')

def get_experience_json(request):
    experiences = Experience.objects.all()
    experience_json= serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience_json_deserialized(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    deserialized_list = [exp.object for exp in experiences]
    context = {
        "name": "Ria Lavenia Kharissa",
        "experience_list": deserialized_list,
        "brand": "Laven"
    }
    return render(request, "experience.html", context)
    


