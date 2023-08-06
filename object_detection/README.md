# Object Detection

Object dection을 수행하기 위해 23년 1월에 출시된 YOLO v8 모델을 사용하였으며, 다음 [Github page(ultralytics)](https://github.com/ultralytics/ultralytics)를 참고하여 진행하였습니다.  

또한 class는 위와 동일하게 dolphins로 진행하였으며, 

총 3개의 weights에 대해 pretrain을 하여 fine tuning을 진행하였으며, 사용한 weights는 다음과 같습니다.

| Model | Size (pixels) | mAPval 50-95 | Speed CPU ONNX (ms) | Speed A100 TensorRT (ms) | Params (M) | FLOPs (B) |
| --- | --- | --- | --- | --- | --- | --- |
| YOLOv8n | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |
| YOLOv8s | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |
| YOLOv8m | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |

## augmentation

1.	Flip : Horizontal, Vertical
2.	90도 Rotate : Clockwise, Counter-Clockwise, Upside Down
3.	Rotation : Between -15도 ~ 15도

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/train_batch0.jpg)

증강으로 인한 최종 데이터의 각 train val test 수는 다음과 같습니다.
-	Train : 702장
-	Validation : 62장
-	Test : 33장



3개의 weights로 pre-train을 진행한 3개의 모델에 대해 학습 후 334장의 dolphins frames 에 대해 test를 진행했습니다.

## YOLOv8n

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_n.png)

- Detection success : 78 / 334


## YOLOv8s

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_s.png)

- Detection success : 86 / 334


## YOLOv8m

![Results](https://github.com/SeongminCC/Detection-Anomaly-frames/blob/main/results_m.png)

- Detection success : 17 / 334


---

데이터의 양이 많지 않았던 만큼 어느정도 모델의 규모를 조절해 줄 필요가 있었습니다. nano 버전보다는 small 버전의 weights로 pre-train 하였을 때 더 좋은 performance가 나왔지만, medium 버전의 weights로 pre-train 하여 학습을 시킨 결과 performance가 급격히 떨어지는 것을 확인할 수 있었습니다.
