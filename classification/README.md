# Classification

## Data Split
- 90:5:5 의 비율로 split 진행 (데이터의 수가 부족한 관계로 train data를 최대한 확보)
    - train : 601 frames
    - validation : 33 frames
    - test : 34 frames
 

## visualize images (dolphin vs non dolphin)

![Alt text](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/compare_dolphin_vs_non_dolphin.png?raw=true "Optional Title")

눈으로 식별되지 않을 정도로 돌고래의 객체가 작습니다. 배경에 비해 객체의 크기가 작기 때문에 feature를 추상적으로 추출하는 classification task의 performance가 좋지 않을 것으로 예상됩니다.


## Models

총 5개의 모델들에 대해 실험을 진행하였으며, 3개의 CNN 기반 모델과, 2개의 Former 기반 모델로 구성하였습니다.

| Model | Type |
|-------|------|
| Resnet18 | CNN-based |
| Wide_Resnet50_2 | CNN-based |
| EfficientNet_b4 | CNN-based |
| Visformer_Small | Transformer-based |
| Vit_Small_Patch8_224_Dino | Transformer-based |

## Hyper parameters

- epochs : 100
- patience : 5



## Results

예상한 결과이지만 좋은 결과가 나오지 않았습니다. 이미지 속의 감지해야하는 객체의 크기가 아주 작은 만큼 단순한 분류 작업만으로 해결할 수 없었습니다.

| Model | Accuracy | F1_score |
|-------|----------|----------|
| Resnet18 | 0.5 | 0.333 |
| Wide_Resnet50_2 | 0.5 | 0.333 |
| EfficientNet_b4 | 0.441 | 0.178 |
| Visformer_Small | 0.5 | 0.333 |
| Vit_Small_Patch8_224_Dino | 0.5 | 0.333 |


