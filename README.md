# Face-Unwrap
unwraps your face into 2D image from a video

# What this script is going to do?
This script will take in a video file and extract every frame from it and save it into a folder called "frames".
Then it will take all the extracted frames from the "frames" folder and crop them into 1 pixel width without changing its height and saves them into "framecrop" folder
Now, all the cropped frames are combined to form an image that will unwrap your face

# What type of video is better?
For best results, use mp4 format video
video should be 360 degrees showing your head(I already included a video head.mp4, every video should be of that type)

# Requirements:
> OpenCV
> PIL

# NOTE:
There are two files named "deleteme.txt", you need to delete them first in order to use the code.

Everytime you want to create a new composite image, you must delete all the cropped and extracted frames from "frames" and "framecrop" folders.
