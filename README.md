# Backup-Camera-Simulation
![ADAS Image](https://github.com/LadyEngineerHere/ladyengineerhere-image-resources/raw/main/adas.png)


# Introduction:

This project aims to simulate an Advanced Driver Assistance System (ADAS) feature by overlaying backup guidelines onto a 10-second video captured on an iPhone 12 Pro Max. The simulation enhances the original footage with additional visual cues, enhancing the driver's situational awareness during backup maneuvers.

# Tools and Techniques Used:

- Programming Language: Python
- Libraries: OpenCV
- Text Editor: Visual Studio

# Code Overview:

- The Python script uses OpenCV to read the original video, resize it, and overlay backup guidelines onto each frame. Here's a brief overview of the key components:

1.**Input Files:**
- Original video: ten_sec_clip.mov from the iPhone 12 Pro Max.
- Overlay image: backup_overlay.png obtained from an online source.

2.**Resizing:**
The original video is resized to a custom dimension (415x240) to match the desired output.

3.**Overlay Logic:**
- The overlay image is resized to fit the new dimensions.
- The overlay logic is implemented in the loop, where each frame is resized, and the overlay is blended onto it based on the alpha channel.
- The overlay includes backup guidelines represented in red, yellow, and green colors.

4.**Output:**
- The processed frames are written to an output video (output_video.mp4) with the specified dimensions and frame rate.

5.**ADAS Simulation:**
- The simulation aims to replicate ADAS features by providing visual cues (backup guidelines) to the driver during reverse maneuvers.
- The overlay follows a color scheme: Red for proximity warnings, Yellow for cautious distance, and Green for a safe zone.

# Assumptions:
- The assumptions made during this simulation include the availability of accurate depth information for implementing color-coded backup guidelines.
- The overlay image obtained from Google serves as a generic representation of backup guidelines and may not precisely adhere to ADAS standards.

# Conclusion:
This project demonstrates a simple yet effective simulation of ADAS features by overlaying backup guidelines on an iPhone 12 Pro Max video. The implemented logic enhances driver awareness during reverse maneuvers, contributing to overall vehicle safety.

# Additional Notes

The prototype includes a pre-configured index.html file, providing a visual representation of the project. Simply open the HTML file in a web browser to view the prototype.
Remember to verify and adjust file paths in the code to match your local machine's directory structure.
