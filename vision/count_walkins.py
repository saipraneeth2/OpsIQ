"""Count unique walk-ins from a video file.

Placeholder. To be filled in during Week 2 of the roadmap
(docs/02-roadmap-90-days.md).

Sketch:
    1. Load video with OpenCV.
    2. For every N-th frame (aim ~2 fps), run YOLOv8 person detection.
    3. Feed detections into a simple IoU tracker to assign track IDs.
    4. Count a walk-in when a track crosses a configured entry line (x=y=...).
    5. Print total unique-entry count.

Usage:
    python count_walkins.py --video path/to/day.mp4 --entry-line 0.5
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Count unique walk-ins in a video.")
    p.add_argument("--video", required=True, help="Path to video file (mp4/mkv).")
    p.add_argument(
        "--entry-line",
        type=float,
        default=0.5,
        help="Y-coordinate (0-1) of the entry crossing line.",
    )
    p.add_argument("--fps", type=float, default=2.0, help="Frames per second to sample.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    print(f"[opsiq.vision] TODO — count walk-ins in {args.video}")
    print(f"[opsiq.vision] entry-line={args.entry_line} sample-fps={args.fps}")
    # Implementation lands in Week 2.


if __name__ == "__main__":
    main()
