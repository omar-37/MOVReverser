# Video-Reverser: Reverse Video Frame-by-Frame

This Python project reverses a video frame-by-frame to ensure precise reversal, addressing issues seen in real-time reversal implementations like iMovie. By processing each frame individually, this tool avoids the "chunked reversal" effect often encountered in other software. (In most cases it will not result in a different result when exported)

## Features

- **Frame-by-frame precision**: Ensures every frame is reversed in the correct order.
- **Customizable output**: Supports various video codecs and output formats.
- **Doe not affect audio tracks**: Audio is not included in output video so you may handle it how you wish.
- **Easy to use**: Just drag the input video to the terminal and the reversed video will be in the same directory.


## Requirements

Ensure you have the following installed:

- Python 3.8+
- (To support all of .mp4.mov.avi.mkv.wmv.flv.webm), `ffmpeg` should be installed
- Required Python libraries (install via pip):
  ```bash
  pip install opencv-python
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/omar-37/Video_Reverser.git
   cd Video-Reverser
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Clone the repository.
2. Run the script with the following command:
   ```bash
   python Video-Reverser/reverse_video.py
   ```
3. Drag and drop the file into the terminal (or past it's path in).
4. Reversed video will be placed in the same directory as source video.


## How It Works

1. **Frame Extraction**: The script uses OpenCV to read each frame of the video.
2. **Reversing Frames**: Frames are stored in memory and reversed.
3. **Rebuilding the Video**: The reversed frames are stitched back together into a new video file.
4. **Audio Handling**: Audio is removed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy reversing! 🎥
