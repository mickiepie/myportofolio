from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, ExperienceForm
from .models import Project
from main.models import Experience
import datetime;
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied 
from django.views.decorators.http import require_POST




def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Ria Lavenia Kharissa",
        "brand": "Laven",
        "npm": "2506543905",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "I am an Information Systems student at the University of Indonesia with a strong passion for business and technology, particularly in web development, design, and product management. "
            "I am someone who loves to learn, is ambitious to grow, and enjoys social activities."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()

    context = {
        "name": "Ria Lavenia Kharissa",
        "brand": "Laven",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()
    context = {
        'name': 'Ria Lavenia Kharissa',
        'brand': 'Laven',
        'title_query': title_query,
        'is_editor': is_editor,
        'form': ProjectForm(),
    }

    return render(request, 'projects.html', context)

# hanya superuser
@login_required(login_url="/login/")  # memeriksa request.user sebelum isi fungsi dijalankan
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "model": "main.project",
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "link": project.link,
                "thumbnail": project.thumbnail,
            },
            "extra": {
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

# hanya superuser
@login_required(login_url="/login/")  
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# hanya superuser
@login_required(login_url="/login/") 
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

# boleh superuser dan editor
@login_required(login_url="/login/") 
def edit_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    experience= get_object_or_404(Experience, pk=id)
    form=ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {'form': form, 'experience': experience, 'name': 'Ria Lavenia Kharissa'}
    return render(request, "edit_experience.html", context)

# boleh superuser dan editor
@login_required(login_url="/login/") 
def edit_project(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    project= get_object_or_404(Project, pk=id)
    form=ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_project')
    context = {'form': form, 'project': project, 'name': 'Ria Lavenia Kharissa'}
    return render(request, "edit_project.html", context)

# hanya superuser
@login_required(login_url="/login/") 
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience= get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect('main:show_experience')
    return redirect('main:show_experience')

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    #debouncing Tasks
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    #serialisasi semua field
    experience_json = serializers.serialize(
        "json", 
        experiences, 
        use_natural_foreign_keys=True
    )
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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Ria Lavenia Kharissa",
        "form": form,
        "brand": "Laven",
    }
    return render(request, "register.html", context)   

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Ria Lavenia Kharissa",
        "form": form,
        "brand": "Laven"
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def edit_experience_ajax(request, id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        return JsonResponse(
                    {"message": "Hanya pemilik portofolio atau Editor yang dapat mengedit pengalaman."},
                    status=403,
                )
    
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST, instance=experience)
    
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Pengalaman berhasil diperbarui."})
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def edit_project_ajax(request, id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        return JsonResponse(
                    {"message": "Hanya pemilik portofolio atau Editor yang dapat mengedit proyek."},
                    status=403,
                )
    
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST, instance=project)
    
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Proyek berhasil diperbarui."})
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)