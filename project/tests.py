import os
import json
import torch
from FastSAM.fastsam import FastSAM, FastSAMPrompt


class Annotate():
    def __init__(self) -> None:
        self.DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.output_image_dir = f'{self.DIR_PATH}/media/output/'

    def annotate(self, request, Output_Img):
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
        output_img_names = os.listdir(self.output_image_dir)
        for i in output_img_names:
            upload = Output_Img()
            upload.output_imgfile = i
            upload.save()
            output_images.append(f'/media/output/{i}')
        return output_images
    
    # output_images = json.dumps(output_images)
    # return redirect('http://127.0.0.1:8000/project/annotate/work/')
    # return JsonResponse({'output_images': output_images})
