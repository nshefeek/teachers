from django.shortcuts import render, redirect
from .models import CsvFile, ImageZipFile
from .forms import CsvFileModelForm, ImageZipFileForm
from directory.models import Teacher
import csv
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def import_csv_view(request):
    form = CsvFileModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvFileModelForm()
        obj = CsvFile.objects.get(loaded=False)
        with open(obj.file_name.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line, row in enumerate(reader):
                print(row)
                # row = ','.join(row).replace(r'\xa0', ' ').split()
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
            obj.loaded = True
            obj.save()
    return render(request, 'importer/import.html', {'csv_form': form})

def import_jpgs_view(request):
    form = ImageZipFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('importer:import-files')
    else:
        form = ImageZipFileForm()
    return render(request, 'importer/import.html', {'image_form': form})