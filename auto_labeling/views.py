# import os, sys
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render, redirect
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# def start(request):
#     return render(request, 'start.html')

# def main(request):
#     return render(request, 'main.html')

# def upload_file(request): # /media/img에 파일 업로드     
#     if request.method == 'POST' and request.FILES.getlist('file'):
#         uploaded_files = request.FILES.getlist('file')
#         upload_dir = os.path.join("static","images")
#         print("upload_file 들어옴!")
#         # image_paths = []
#         if not os.path.exists(upload_dir):
#             os.makedirs(upload_dir)
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join(upload_dir, uploaded_file.name)
#             with open(file_path, 'wb+') as destination:
#                 for chunk in uploaded_file.chunks():
#                     destination.write(chunk)
#         #     image_paths.append(os.path.join("static","images", uploaded_file.name))
#         # image_paths = [image_path.replace('\\', '/') for image_path in image_paths] , {'image_paths': image_paths}
#         return redirect('http://127.0.0.1:8000/main/')
#     return HttpResponse('Failed')

# from FastSAM.fastsam import FastSAM, FastSAMPrompt
# import torch
# model_path = os.path.join("FastSAM", "weights", "FastSAM-x.pt")
# model = FastSAM(model_path)
# DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# DEVICE = torch.device(
#     "cuda"
#     if torch.cuda.is_available()
#     else "mps"
#     if torch.backends.mps.is_available()
#     else "cpu"
# )

# def Post_xy_point(request):
#     if request.method == 'POST':
#         click_x = int(request.POST.get('clickX'))
#         click_y = int(request.POST.get('clickY'))
#         print(click_x, click_y)
#         IMAGE_PATH =  os.path.join(DIR_PATH, 'static', 'images','3.jpg')
#         everything_results = model(
#             IMAGE_PATH,
#             device=DEVICE,
#             retina_masks=True,
#             imgsz=1024,
#             conf=0.4, # 찾을 확률
#             iou=0.9, # 관심영역
#         )
#         prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)
#         ann = prompt_process.point_prompt(points=[[click_x, click_y]], pointlabel=[1])
#         # ann = prompt_process.everything_prompt()
#         prompt_process.plot(
#             annotations=ann,
#             output_path=os.path.join(DIR_PATH, 'static', 'images','3.jpg'),
#             mask_random_color=True,
#             better_quality=True,
#             retina=False,
#             withContours=True,
#         )

#         return render(request, "main.html")
