from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, Select

from main.models import Project, Experience

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "link",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "link": "URL Proyek",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=1l2MIPkrNXY9Aq-Zi9gQ2OB23pXicmUSO&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "role",
            "category",
            "description",
            "started_at",
            "ended_at",
            "thumbnail",
        ]

        labels= {
            "title": "Nama Pengalaman / Organisasi",
            "role": "Jabatan / Role",
            "category": "Kategori",
            "description": "Deskripsi Pengalaman",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
            "thumbnail": "URL Gambar / Logo",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Open House Fasilkom UI"
                }
            ),
            "role": TextInput(
                attrs={
                    "placeholder": "Contoh: Public Relation Staff"
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pengalaman...", 
                    "rows": 3
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://..."
                }
            ),
        }
