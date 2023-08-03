import argparse
import ultralytics
from ultralytics import YOLO

import cv2
import os

path = "/project/smcho1201/bada_project/object_detection/result_yolo8s/runs/detect/train/weights/best.pt"


def get_frame_rate(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return frame_rate


def detect_dolphin(video_path, weight_path):
    model = YOLO(weight_path)
    results = model(video_path)

    detected_frames = []
    for i, result in enumerate(results):
        if len(result.boxes.data) > 0:
            detected_frames.append(i)
    return detected_frames


def frames_to_time(detected_frames, video_path):
    frame_rate = get_frame_rate(video_path)
    time_per_frame = 1.0 / frame_rate

    min_frame, max_frame = detected_frames[0], detected_frames[-1]
    min_time = min_frame * time_per_frame
    max_time = max_frame * time_per_frame

    return min_time, max_time




def video2time(video_path, weight_path = path):
    # Check if the file exists
    if not os.path.isfile(video_path):
        print("The path is incorrect, please provide a valid path.")
        return
    else:
        print("The video path is valid.")

    detected_frames = detect_dolphin(video_path=video_path, weight_path=weight_path)
    min_time, max_time = frames_to_time(detected_frames, video_path)
    print(f"Min Time: {min_time:.2f} seconds")
    print(f"Max Time: {max_time:.2f} seconds\n")

    print(f"The dolphin appeared between {min_time:.2f} and {max_time:.2f} seconds.")


# dolphin_video_path = "/data/badadata/dolphins.mp4"
# samle_video_path = "/data/badadata/sample_data.mp4"    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dolphin detection script.")
    parser.add_argument('--video_path', type=str, required=True, help="Path to the video file.")
    args = parser.parse_args()

    video2time(video_path=args.video_path)
