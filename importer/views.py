from django.shortcuts import render
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
        print(type(obj))
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for line, row in enumerate(reader):
                # print(row)
                # row = ','.join(row).replace(r'\xa0', ' ').split()
                # print(row)
                if line == 0:
                    continue
                first_name = row[0]
                last_name = row[1]
                image = None if row[2] == r'\xa0' else row[2]
                email = row[3]
                phone = row[4]
                room = row[5]
                subjects = ', '.join(row[6].split(',')[:5])
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
    print(form)
    if form.is_valid():
        form.save()
        form = ImageZipFileForm()
        obj = ImageZipFile.objects.get(loaded=False)

    return render(request, 'importer/import.html', {'image_form': form})