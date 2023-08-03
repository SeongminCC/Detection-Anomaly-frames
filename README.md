# Detection-Anomaly-frames
Building a system to capture special moments within a video and create a new video from them.

## Project Introduction
본 프로젝트는 바다를 비추고 있는 전망대의 영상 데이터에서 특별한 순간의 frame를 감지하는 것을 목표로 하고 있습니다. 분명하게 정해진 class가 존재하지 않아 여러 task로 접근을 시도합니다.  

다행히도 여러 sample data 들을 찾을 수 있어 각 sample들을 class로 분류한 후 supervised learning을 시도해 볼 수 있었으며, temporal window를 사용하여 Background Estimation을 진행할 생각입니다.  

약 3분의 sample 영상에 대해 frame 단위로 저장하니 총 4246 frames로 구성된 것을 확인할 수 있었습니다. 해당 sample 영상의 경우 돌고래가 바다 수면 위로 떠오르는 모습을 담은 영상이며, 돌고래가 보이는 frame을 따로 분리해주었습니다. 해당 작업은 수동으로 진행하였습니다.

| Time (min:sec) | Frames | Frame Count |
| --- | --- | --- |
| 0:46 | 1123 ~ 1150 | 27 |
| 1:01 | 1482 ~ 1516 | 34 |
| 1:23 | 2010 ~ 2042 | 32 |
| 1:31 | 2207 ~ 2231 | 24 |
| 1:36 | 2317 ~ 2340 | 23 |
| 1:41 | 2438 ~ 2452 | 14 |
| 2:05 | 3006 ~ 3026 | 20 |
| 2:10 | 3124 ~ 3140 | 16 |
| 2:13 | 3216 ~ 3231 | 15 |
| 2:23 | 3446 ~ 3472 | 26 |
| 2:29 | 3593 ~ 3614 | 21 |
| 2:46 | 3976 ~ 4023 | 47 |
| 2:50 | 4104 ~ 4126 | 22 |



## Classification

### Data Split
- 90:5:5 의 비율로 split 진행 (데이터의 수가 부족한 관계로 train data를 최대한 확보)
    - train : 601 frames
    - validation : 33 frames
    - test : 34 frames
 

### visualize images (dolphin vs non dolphin)

![Alt text](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/compare_dolphin_vs_non_dolphin.png?raw=true "Optional Title")

눈으로 식별되지 않을 정도로 돌고래의 객체가 작습니다. 배경에 비해 객체의 크기가 작기 때문에 feature를 추상적으로 추출하는 classification task의 performance가 좋지 않을 것으로 예상됩니다.


### Models

총 5개의 모델들에 대해 실험을 진행하였으며, 3개의 CNN 기반 모델과, 2개의 Former 기반 모델로 구성하였습니다.

| Model | Type |
|-------|------|
| Resnet18 | CNN-based |
| Wide_Resnet50_2 | CNN-based |
| EfficientNet_b4 | CNN-based |
| Visformer_Small | Transformer-based |
| Vit_Small_Patch8_224_Dino | Transformer-based |

### Hyper parameters

- epochs : 100
- patience : 5



### Results

예상한 결과이지만 좋은 결과가 나오지 않았습니다. 이미지 속의 감지해야하는 객체의 크기가 아주 작은 만큼 단순한 분류 작업만으로 해결할 수 없었습니다.

| Model | Accuracy | F1_score |
|-------|----------|----------|
| Resnet18 | 0.5 | 0.333 |
| Wide_Resnet50_2 | 0.5 | 0.333 |
| EfficientNet_b4 | 0.441 | 0.178 |
| Visformer_Small | 0.5 | 0.333 |
| Vit_Small_Patch8_224_Dino | 0.5 | 0.333 |


  

  
## Object Detection

Object dection을 수행하기 위해 23년 1월에 출시된 YOLO v8 모델을 사용하였으며, 다음 [Github page(ultralytics)](https://github.com/ultralytics/ultralytics)를 참고하여 진행하였습니다.  

또한 class는 위와 동일하게 dolphins로 진행하였으며, 

총 3개의 weights에 대해 pretrain을 하여 fine tuning을 진행하였으며, 사용한 weights는 다음과 같습니다.

| Model | Size (pixels) | mAPval 50-95 | Speed CPU ONNX (ms) | Speed A100 TensorRT (ms) | Params (M) | FLOPs (B) |
| --- | --- | --- | --- | --- | --- | --- |
| YOLOv8n | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |
| YOLOv8s | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |
| YOLOv8m | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |

### augmentation

1.	Flip : Horizontal, Vertical
2.	90도 Rotate : Clockwise, Counter-Clockwise, Upside Down
3.	Rotation : Between -15도 ~ 15도

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/train_batch0.jpg)

증강으로 인한 최종 데이터의 각 train val test 수는 다음과 같습니다.
-	Train : 702장
-	Validation : 62장
-	Test : 33장



3개의 weights로 pre-train을 진행한 3개의 모델에 대해 학습 후 334장의 dolphins frames 에 대해 test를 진행했습니다.

### YOLOv8n

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_n.png)

- Detection success : 78 / 334


### YOLOv8s

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_s.png)

- Detection success : 86 / 334


### YOLOv8m

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_m.png)

- Detection success : 17 / 334


---

데이터의 양이 많지 않았던 만큼 어느정도 모델의 규모를 조절해 줄 필요가 있었습니다. nano 버전보다는 small 버전의 weights로 pre-train 하였을 때 더 좋은 performance가 나왔지만, medium 버전의 weights로 pre-train 하여 학습을 시킨 결과 performance가 급격히 떨어지는 것을 확인할 수 있었습니다.
