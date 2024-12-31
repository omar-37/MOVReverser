import cv2
import os
import tempfile

def reverse_video(input_path, output_path):
    # Create a temporary directory to store frames
    with tempfile.TemporaryDirectory() as temp_dir:
        # Open the video file
        cap = cv2.VideoCapture(input_path)
        
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
        
        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"Processing {frame_count} frames...")

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

# Example usage
input_video = "Blurry_Car.mov"  # Path to the input video
output_video = f"{input_video[0:-4]}_reversed.mov"  # Path to save the reversed video 
reverse_video(input_video, output_video)
