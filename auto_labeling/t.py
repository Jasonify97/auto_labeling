
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from FastSAM.fastsam import FastSAM, FastSAMPrompt
import torch
from django.conf import settings


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
prompt_process.plot(
annotations=ann,
output_path=f'{DIR_PATH}\\media\\output\\',
mask_random_color=True,
better_quality=True,
retina=False,
withContours=True,
)