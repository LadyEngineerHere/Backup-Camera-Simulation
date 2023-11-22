import cv2

# Paths to the video and overlay image
video_path = "/Users/amandanassar/Desktop/ADAS_Project/ten_sec_clip.mov"
overlay_path = "/Users/amandanassar/Desktop/ADAS_Project/backup_overlay.png"

# Output video path
output_video_path = "/Users/amandanassar/Desktop/ADAS_Project/output_video.mp4"

# Set the new dimensions
new_width = 415
new_height = 240

# Read the video and overlay image
video = cv2.VideoCapture(video_path)
overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

# Get the original dimensions of the video
original_width = int(video.get(3))
original_height = int(video.get(4))

# Resize the overlay image to match the new dimensions
overlay = cv2.resize(overlay, (new_width, new_height))

# Create a VideoWriter object to save the resized video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_video_path, fourcc, 30, (new_width, new_height))

# Set the duration of the clip in seconds
clip_duration = 10
frame_rate = int(video.get(5))
end_frame = int(clip_duration * frame_rate)

# Loop through each frame of the original video
for _ in range(end_frame):
    # Read the next frame
    ret, frame = video.read()
    if not ret:
        break

    # Resize the frame
    frame = cv2.resize(frame, (new_width, new_height))

    # Overlay the image onto the frame
    for c in range(0, 3):
        frame[:, :, c] = frame[:, :, c] * (1 - overlay[:, :, 3] / 255.0) + overlay[:, :, c] * (overlay[:, :, 3] / 255.0)

    # Write the frame to the output video
    output_video.write(frame)

# Release the video capture and video writer objects
video.release()
output_video.release()
cv2.destroyAllWindows()
