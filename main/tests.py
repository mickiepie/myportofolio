from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import date
from main.models import Experience, Project
from main.forms import ExperienceForm
import json


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Open House Fasilkom UI",
            description="Served as Master of Ceremony and faculty representative in school visitation programs, delivering presentations and engaging prospective students to promote Fakultas Ilmu Komputer Universitas Indonesia.",
            category="committee",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), f"{self.experience.role} at {self.experience.title}")
        self.assertEqual(self.experience.category, "committee")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Committee")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)
        

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            description="Developed a dynamic personal web portfolio.",
            tech_stack="Python, Django, HTML, CSS",
            link="https://github.com/rialavenia/myportfolio"
        )

    def test_project_url_and_template(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")

    def test_project_content_display(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.tech_stack)
        self.assertContains(response, self.project.description)

class ExperienceTest(TestCase):
    def setUp(self):
            self.client=Client()
            self.experience = Experience.objects.create(
                title="Open House Fasilkom UI",
                description="Served as Master of Ceremony and faculty representative in school visitation programs, delivering presentations and engaging prospective students to promote Fakultas Ilmu Komputer Universitas Indonesia.",
                category="committee",
                role="Public Relation Staff",
                started_at=date(2025, 8, 1),
                
                
    )

    def test_show_experience(self):
        response=self.client.get(reverse('main:show_experience'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')
        self.assertContains(response, "Public Relation Staff")

    def test_expeerience_form_validation(self):
        form_data={
            'title': 'BETIS Fasilkom UI',
            'role': 'Event staff',
            'description': 'Membantu mengkoordinasikan acara',
            'started_at': '2025-08-01',
            'category': 'committee',
            'thumbnail': 'https://example.com/ta.png'
        }

        form=ExperienceForm(data=form_data)
        print("Detail: ", form.errors)
        self.assertTrue(form.is_valid())

        empty_form= ExperienceForm(data={})
        self.assertFalse(empty_form.is_valid())

    def test_create_experience(self):
        new_data = {
            'title': 'UI/UX Designer',
            'role': 'Lead Designer',
            'description': 'Merancang web',
            'started_at': '2025-02-01',
            'category': 'full-time',
            'thumbnail': 'https://example.com/design.png'
        }
        response = self.client.post(reverse('main:create_experience'), data=new_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Experience.objects.filter(title="UI/UX Designer").exists())

    def test_edit_experience(self):
        update_data={
            'title': 'Senior Software Engineer',
            'role': 'Fullstack',
            'description': 'Blablabla',
            'started_at': '2025-01-01',
            'category': 'internship',
            'thumbnail': 'https://example.com/image.png'
        }
        response=self.client.post(
            reverse('main:edit_experience', args=[self.experience.id]),
            data=update_data
        )
        self.assertEqual(response.status_code, 302)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title,  "Senior Software Engineer")

    def test_delete_experience(self):
        response=self.client.post(reverse('main:delete_experience', args=[self.experience.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())

    def test_search_experience(self):
        response = self.client.get(reverse('main:show_experience') + '?title=Open')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Open House Fasilkom UI")

        response_empty = self.client.get(reverse('main:show_experience') + '?title=abcdef')
        self.assertNotContains(response_empty, "Open House Fasilkom UI")

    def test_get_experience_json(self):
        response = self.client.get(reverse('main:get_experience_json'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['fields']['title'], "Open House Fasilkom UI")
