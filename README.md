**README**

This script, `script_video.py`, allows you to generate a video montage from a folder of images along with subtitles, and combine it with an audio track. Here's a guide on how to set it up on Ubuntu:

### Prerequisites
1. **Python**: Ensure Python is installed on your system. You can check by running `python3 --version` in your terminal. If not installed, you can install Python using `sudo apt install python3`.

2. **pip**: Make sure you have `pip` installed. You can install it using `sudo apt install python3-pip`.

### Installation Steps
1. **Clone the repository**: Clone this repository to your local machine using Git.
    ```bash
    git clone https://github.com/Anac0n6a/image_in_video
    ```

2. **Navigate to the directory**: Enter into the directory where the script is located.
    ```bash
    cd path/to/image_in_video
    ```

3. **Install dependencies**: Install the required Python packages using pip.
    ```bash
    pip3 install moviepy
    ```

4. **Install ffmpeg**: The script utilizes ffmpeg for video processing. Install it using apt.
    ```bash
    sudo apt install ffmpeg
    ```

### Usage
1. **Prepare your files**:
   - Place your images in a folder. Update the `image_folder` variable in the script with the path to this folder.
   - Ensure you have an audio file (e.g., `.mp3`) and a subtitle file (e.g., `.srt`).

2. **Update script variables**: Update the following variables in the script with the appropriate paths:
   - `image_folder`: Path to the folder containing images.
   - `audio_file`: Path to the audio file.
   - `subtitle_file`: Path to the subtitle file.
   - `output_file`: Path for the output video file.

3. **Run the script**: Execute the script in your terminal.
    ```bash
    python3 script_video.py
    ```

4. **Wait for completion**: The script will generate the video with subtitles. The progress will be displayed in the terminal.

5. **Find your video**: Once the script completes, you'll find your video ready at the specified output path.

### Creating the srt file
**Using AI to Help Create Subtitles**:
  - I used this service and it converted for me from mp3 to srt `https://studio.wavel.ai/` But you can use any other one you find
  - The main thing is that the srt file looks something like this:
```
1
00:00:00,080 --> 00:00:02,400
In a vast mountain range, an aging

2
00:00:02,400 --> 00:00:04,240
eagle realized it had to make a crucial

3
00:00:04,240 --> 00:00:06,000
decision to ensure its survival.

4
00:00:06,400 --> 00:00:09,400
Its beak was bent, talons weak, and feathers
```


### Additional Notes
- You can tweak the effects or customize the script further according to your preferences by modifying the provided functions in the script.
- Ensure your image filenames are sorted in the order you want them to appear in the video.
- Make sure your subtitle file matches the duration of your video. Adjust it accordingly if needed.
  
Enjoy creating your videos with subtitles! If you encounter any issues or have suggestions, feel free to reach me.
