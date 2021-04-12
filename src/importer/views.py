from django.shortcuts import render
from directory.models import Teacher, Subject
from .models import MultipleFiles
from .forms import MultipleFileForms
from django.contrib.auth.decorators import login_required
import csv
from zipfile import ZipFile
from teachers.settings import BASE_DIR


# helper function for subject object creation
# can be removed if subjects are added via admin panel
def create_subjects(subject_list):
    subjects_in_db = set(subject[-1] for subject in Subject.objects.values_list())
    subjects_not_present = set(subject_list) - subjects_in_db
    if subjects_not_present:
        for subject in subjects_not_present:
            Subject.objects.create(title=subject)


@login_required
# Create your views here.
def import_file_view(request):
    form = MultipleFileForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = MultipleFileForms()
        file_obj = MultipleFiles.objects.filter(csv_activated=False, zip_extracted=False).get()
        csv_file = file_obj.csv_file.path
        zip_file = file_obj.zip_file.path
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line, row in enumerate(reader):
                if line == 0 or not row[0]:
                    continue
                first_name = row[0]
                last_name = row[1]
                image = 'profile_pics/'+row[2].strip() if row[2].strip() else 'default.jpg'
                email = row[3]
                phone = row[4]
                room = row[5]
                subjects = row[6].title().split(', ')[:5]
                create_subjects(subjects)   # Comment out this line if subjects are added via admin panel
                try:
                    teacher = Teacher.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    image = image, 
                    email = email,
                    phone = phone,
                    room = room,
                )
                    # teacher.subjects.add(*[Subject.objects.get(title=subject).id for subject in subjects])
                    teacher.subjects.add(
                        *Subject.objects.filter(
                            title__in=subjects
                            ).values_list("id", flat=True))

                except Exception as e:
                    print(e, email)     # Can be improved by using logging module to log errors

        with ZipFile(zip_file, 'r') as f:
            f.extractall(BASE_DIR/'media/profile_pics/')

        file_obj.csv_activated = True
        file_obj.zip_extracted = True
        file_obj.save()
        
    return render(request, 'importer/import.html', {'form': form})