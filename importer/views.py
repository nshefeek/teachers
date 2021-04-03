from django.shortcuts import render, redirect, reverse
from .models import CsvFile, ImageZipFile, MultipleFiles
from .forms import CsvFileModelForm, ImageZipFileForm, MultipleFileForms
from directory.models import Teacher
from django.contrib.auth.decorators import login_required

import io
import csv
from zipfile import ZipFile

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
                print(row)
                if line == 0 or not row[0]:
                    continue
                first_name = row[0]
                last_name = row[1]
                image = 'profile_pics/'+row[2].strip() if row[2].strip() else 'default.jpg'
                email = row[3]
                phone = row[4]
                room = row[5]
                subjects = ', '.join(row[6].split(',')[:5]).title()
                try:
                    Teacher.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    image = image, 
                    email = email,
                    phone = phone,
                    room = room,
                    subjects = subjects,
                )
                except Exception as e:
                    print(e, email)

        with ZipFile(zip_file, 'r') as f:
            f.extractall('media/profile_pics/')

        file_obj.csv_activated = True
        file_obj.zip_extracted = True
        file_obj.save()
        

    return render(request, 'importer/import.html', {'form': form})

# @login_required
# def import_images_view(request):
#     form = ImageZipFileForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         zip_file = ImageZipFile.objects.get(request.FILES['file_name'])
#         with ZipFile(zip_file) as f:
#             f.extract('profile_pics/')
#         return redirect('importer:import-files')
#     else:
#         form = ImageZipFileForm()

#     return render(request, 'importer/import.html', {'form': form})