from django.shortcuts import render

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
    }
    return render(request, "experience.html", context)
