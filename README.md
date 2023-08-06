# Detection-Anomaly-frames
Building a system to capture special moments within a video and create a new video from them.

## Project Introduction
본 프로젝트는 바다를 비추고 있는 전망대의 영상 데이터에서 특별한 순간의 frame를 감지하는 것을 목표로 하고 있습니다. 분명하게 정해진 class가 존재하지 않아 여러 task로 접근을 시도합니다.  

- [x] Classification
- [x] Object detection
- [ ] Background Estimation


## Data
우선 supervised learning을 적용해보기 위해 순차적으로 class가 포함된 sample data들을 참고하여 전처리를 진행하였습니다.


### Dolphins 
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

