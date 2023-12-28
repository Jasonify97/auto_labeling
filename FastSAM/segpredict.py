from fastsam import FastSAM, FastSAMPrompt
import torch, os



model_path = os.path.join("FastSAM", "weights", "FastSAM-x.pt")
model = FastSAM(model_path)
# IMAGE_PATH = os.path.join("FastSAM","1.jpg")///
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IMAGE_PATH =  f"{DIR_PATH}/1.jpg"
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
    conf=0.4, # 찾을 확률
    iou=0.9, # 관심영역
)
prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)

print(everything_results[0].masks)

# everything prompt
# ann = prompt_process.everything_prompt()

# # bbox prompt labeling box 처럼 4개의 값을 인풋으로
# # bbox default shape [0,0,0,0] -> [x1,y1,x2,y2]
# bboxes default shape [[0,0,0,0]] -> [[x1,y1,x2,y2]]
# ann = prompt_process.box_prompt(bbox=[200, 200, 300, 300])
# ann = prompt_process.box_prompt(bboxes=[[200, 200, 300, 300], [500, 500, 600, 600]])

# # text prompt
# ann = prompt_process.text_prompt(text='a photo of a dog')

# # point prompt xy좌표
# # points default [[0,0]] [[x1,y1],[x2,y2]]
# # point_label default [0] [1,0] 0:background, 1:foreground
# ann = prompt_process.point_prompt(points=[[620, 360]], pointlabel=[1])

# prompt_process.plot(
#     annotations=ann,
#     output_path=f'{DIR_PATH}/output/hi.jpg',
#     mask_random_color=True,
#     better_quality=True,
#     retina=False,
#     withContours=True,
# )
