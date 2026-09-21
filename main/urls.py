from django.urls import path
from main.views import show_projects, create_project, create_experience, edit_experience, delete_experience, get_experience_json, show_experience_json_deserialized
from main.views import show_main, show_experience, get_projects_json, delete_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('projects/', show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),

    path('experience/create/', create_experience, name='create_experience'),
    path('experience/edit/<uuid:id>/', edit_experience, name='edit_experience'),
    path('experience/delete/<uuid:id>/', delete_experience, name='delete_experience'),
    path('experience/json/', get_experience_json, name='get_experience_json'),
    path('experience/json-deserialized/', show_experience_json_deserialized, name='show_experience_json_deserialized'),
]