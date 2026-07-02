# vision/

Computer-vision pipeline for counting walk-ins and (later) measuring staff activity.

## What lives here

- `count_walkins.py` — takes a video file, returns a unique-person count using YOLOv8 + a lightweight tracker.
- `staff_activity.py` (future) — pose estimation to measure stylist active time vs idle time in the salon.
- `greet_time.py` (future, for Lenskart) — measures seconds between a customer entering and a staff member approaching.

## Why YOLOv8?

- Pretrained on COCO (person is class 0). Zero fine-tuning needed for v1.
- Runs on CPU at 2–5 fps on a modern laptop. Good enough for nightly batch processing.
- Ultralytics library has clean Python API. `pip install ultralytics` is the entire setup.

## Notes for the tracker

Person detection is not enough — the same person walking across three frames is three detections. We need to deduplicate. Options:

1. **Simple IoU tracker** (v1). ~30 lines of Python. Adequate for entrance cameras where people cross a line and don't linger.
2. **ByteTrack / DeepSORT** (v2). Better in crowded scenes. Use once accuracy of the simple tracker drops below 85%.

## Running the placeholder

```bash
cd vision
pip install ultralytics opencv-python
python count_walkins.py --video sample.mp4
```
