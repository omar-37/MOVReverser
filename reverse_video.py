import cv2
import os
import tempfile
import concurrent.futures

def reverse_video(input_path, output_path):
    # Create a temporary directory to store frames
    with tempfile.TemporaryDirectory() as temp_dir:
        # Open the video file
        cap = cv2.VideoCapture(input_path)
        
        if not cap.isOpened():
            print(f"Error: Could not open video {input_path}.")
            return
        
        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"Processing {frame_count} frames from {input_path}...")

        # Step 1: Save frames to disk
        frame_paths = []
        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_path = os.path.join(temp_dir, f"frame_{frame_idx:06d}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_paths.append(frame_path)
            frame_idx += 1
        
        cap.release()
        
        # Step 2: Write reversed frames to the output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
        
        for frame_path in reversed(frame_paths):
            frame = cv2.imread(frame_path)
            out.write(frame)
        
        out.release()
        print(f"Reversed video saved to {output_path}")

def process_videos_in_directory(directory_path):
    compatible_extensions = ['.mp4', '.avi', '.mov']  # Add more extensions if needed
    video_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.splitext(f)[1].lower() in compatible_extensions]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for video_file in video_files:
            output_video = f"{os.path.splitext(video_file)[0]}_reversed.mov"
            futures.append(executor.submit(reverse_video, video_file, output_video))
        
        for future in concurrent.futures.as_completed(futures):
            future.result()

# Example usage
input_path = str(input("Enter the path to a video file or a directory:\n"))

if os.path.isdir(input_path):
    process_videos_in_directory(input_path)
else:
    output_video = f"{os.path.splitext(input_path)[0]}_reversed.mov"
    reverse_video(input_path, output_video)
