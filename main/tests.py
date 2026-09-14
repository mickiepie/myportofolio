from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import date
from main.models import Experience, Project


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
        self.assertEqual(str(self.experience), "Open House Fasilkom UI")
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
            link="https://github.com/rialavenia/myportfolio",
            created_at=date(2026, 9, 2)
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