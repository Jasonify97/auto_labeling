import os, sys
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

def upload_file(request): # /media/img에 파일 업로드     
    if request.method == 'POST' and request.FILES.getlist('file'):
        uploaded_files = request.FILES.getlist('file')
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'img')
        
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        for uploaded_file in uploaded_files:
            file_path = os.path.join(upload_dir, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        return render(request, 'main.html')
    return HttpResponse('Failed') 

from FastSAM.fastsam import FastSAM, FastSAMPrompt
import torch
model_path = os.path.join("FastSAM", "weights", "FastSAM-x.pt")
model = FastSAM(model_path)
DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
IMAGE_PATH =  os.path.join(DIR_PATH, 'media', 'img','1.png')
DEVICE = torch.device(
IMAGE_PATH = 'C:/Users/CASELAB2/Desktop/auto_labeling/media/img/1.png'
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
everything_results = model(
    IMAGE_PATH,
    device=DEVICE,
    retina_masks=True,
    imgsz=1024,
    conf=0.4, # 찾을 확률
    iou=0.9, # 관심영역

)
prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)
ann = prompt_process.everything_prompt()

def prompt(request):
    prompt_process.plot(
    annotations=ann,
    output_path=f'{DIR_PATH}\\media\\output\\',
    mask_random_color=True,
    better_quality=True,
    retina=False,
    withContours=True,
    )
    



