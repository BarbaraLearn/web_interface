from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return render(request, 'hello.html', {'name' : 'Barbara'})  #HttpResponse(" Basic Django Web Interface!")

from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('download_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

#################################################################################

def upload_success(request):
    return render(request, 'upload_success.html')

################################################################################

from django.http import FileResponse

def download_file(request):
    file_path = r'C:\Users\blebl\Desktop\repos\web_interface\pic.jpg'  # Replace with your actual file path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
    return response