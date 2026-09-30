from django.urls import path
from main.views import show_projects, create_project, create_experience, edit_experience, delete_experience, get_experience_json, show_experience_json_deserialized
from main.views import show_main, show_experience, get_projects_json, delete_project, register, login_user, logout_user, edit_project, toggle_star, create_project_ajax

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
    path('project/edit/<uuid:id>/', edit_project, name='edit_project'),
    path('experience/delete/<uuid:id>/', delete_experience, name='delete_experience'),
    path('experience/json/', get_experience_json, name='get_experience_json'),
    path('experience/json-deserialized/', show_experience_json_deserialized, name='show_experience_json_deserialized'),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),

    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
]