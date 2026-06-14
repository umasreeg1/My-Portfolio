from django.shortcuts import render
from .models import User, ProjectCategory, Certification, Skills, Education

def home(request):
    user = User.objects.first()

    context = {
        "user": user,
        "projects": ProjectCategory.objects.all(),
        "certifications": Certification.objects.all(),
        "skills": Skills.objects.all(),
        "education": Education.objects.all(),
    }

    return render(request, "home.html", context)