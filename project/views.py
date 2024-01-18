import os
import json
import torch

from django.shortcuts import render, redirect
from .models import Upload, Output_Img
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404

from FastSAM.fastsam import FastSAM, FastSAMPrompt

def upload(request):
    if request.method == "POST":
        image_list = request.FILES.getlist('imgfile')
        for img in image_list:
            upload = Upload()
            upload.imgfile = img
            upload.save()
            
            # # 이미지 파일의 내용을 가져옵니다.
            # image_content = img.read()

            # # 이미지 파일의 이름으로 기존 이미지를 찾거나 새로운 이미지를 생성합니다.
            # # upload, created = Upload.objects.get_or_create(imgfile=img.name)
            # existing_upload = Upload.objects.filter(imgfile=img.name).first()

            # # if created:
            # if not existing_upload:
            #     upload = Upload(imgfile=img.name)
            #     # 이미지가 새로 생성된 경우에만 이미지를 저장합니다.
            #     upload.imgfile.save(img.name, ContentFile(image_content))
            #     upload.save()
        return redirect('http://127.0.0.1:8000/project/annotate/work/')
    return render(request, "project/upload.html")

def annotate_main(request):
    if request.method == "GET":
        images = []
        image_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media\\img\\')
        img_names = os.listdir(image_dir)
        for i in img_names:
            images.append(f'/media/img/{i}')
        images = json.dumps(images)
        return redirect('http://127.0.0.1:8000/project/annotate/')
    return render(request, 'project/annotate.html', {'images': images}) 

def annotate(request):
    if request.method == 'POST':
        points_dict = json.loads(request.POST.get('points_dict'))
        points_list = []
        for points in points_dict['points_list']:
            points = list(map(float, points))
            points = list(map(int, points))
            points_list.append(points)
        points_dict['points_list'] = points_list
        IMAGE_PATH = '.'+str(request.POST.get('currentimagepath'))
        filename = IMAGE_PATH.split('/')[-1]
        model = FastSAM('./FastSAM/weights/FastSAM-x.pt')
        DEVICE = torch.device(
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
            conf=0.4,
            iou=0.9,
        )
        prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)
        ann = prompt_process.point_prompt(points=points_dict['points_list'], pointlabel=points_dict['points_label'])
        prompt_process.plot(
            annotations=ann,
            output_path=f'./media/output/{filename}',
            mask_random_color=True,
            better_quality=True,
            retina=False,
            withContours=True,
        )   
        output_images = []
        output_image_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media\\output\\')
        output_img_names = os.listdir(output_image_dir)
        for i in output_img_names:
            upload = Output_Img()
            upload.output_imgfile = i
            upload.save()
            output_images.append(f'/media/output/{i}')

        output_images = json.dumps(output_images)
        return redirect('http://127.0.0.1:8000/project/annotate/work/')
    return render(request, "project/annotate.html", {'output_images': output_images})

def classes(request):
    
    return render(request, "project/classes.html")

def generate(request):
    
    return render(request, "project/generate.html")
