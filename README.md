
# OpenCV Auto-Clicker with SIFT

This Python script utilizes the **SIFT (Scale-Invariant Feature Transform)** algorithm implementation from OpenCV for image matching to create an auto-clicker that clicks on a specified target image in the screen. 

*Note: The SIFT algorithm, being computationally intensive, may result in slower performance on systems with limited processing power.*
## Features

- **SIFT Algorithm:** The script employs the Scale-Invariant Feature Transform (SIFT) for robust and invariant image matching, making it resistant to changes in scale, rotation, and illumination.

- **Click Types:** Choose between left-click and right-click actions based on your requirements.

- **Adjustable Threshold:** Fine-tune the matching sensitivity with the threshold parameter. The script dynamically determines matches based on feature distances, making it adaptable to various images.

- **Sleep Time:** Specify the time to delay after each click to avoid rapid consecutive clicks.

## How to Use

1. Install dependencies listed in requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script with optional command-line arguments:

    ```bash
    python script.py -i path/to/target/image.png -t 10 -c left -s 0.1
    ```

    - `-i` or `--image`: Path to the target image.
    - `-t` or `--threshold`: Matching threshold (default: 10).
    - `-c` or `--click-type`: Type of click ('left' or 'right') (default: 'left').
    - `-s` or `--sleep-time`: Time to delay after click in seconds (default: 0.1).

3. The script will continuously look for the target image on the screen and perform clicks when found.

## Additional Information

- **High Computing Requirements:** The SIFT algorithm, being computationally intensive, may result in slower performance on systems with limited processing power. If you experience significant delays between iterations, consider optimizing the script's performance or running it on a more powerful machine.

- **Target Image Path:** You can specify the path to the target image using the `-i` or `--image` argument. The script reads this image for matching.

- **Threshold:** The matching threshold determines the minimum similarity score required for a match to be considered valid. Adjust it based on your specific matching requirements.

- **Sleep Time:** After each click, the script waits for the specified sleep time to avoid rapid consecutive clicks.

- **Constants:** You can modify constants like THRESHOLD, TARGET_IMAGE_PATH, and SLEEP_TIME in the script to tailor the behavior according to your preferences.

- **Requirements.txt:** Install the required dependencies using the `pip install -r requirements.txt` command.

## Notes

- This script is intended for **educational use only**. Usage for automating interactions with applications or websites may violate terms of service.
- Handle keyboard interrupt (Ctrl+C) to terminate the script.

