import time
import cv2
import argparse

# Import utility functions from utils.py
from utils import capture_screen, find_image, perform_click

# Import constants from config.py
from config import SLEEP_TIME, THRESHOLD, TARGET_IMAGE_PATH


def main(target_image_path, threshold, click_type):
    """
    Main function to find the target image in the screenshot and perform right-clicks
    :param target_image_path: the path to the target image
    :param threshold: matching threshold for identifying the target image
    :return: None
    """
    total_finds = 0
    target_image = cv2.imread(target_image_path)

    try:
        while True:
            try:
                print("Looking for the target image...")
                # Capture the current screen and find the target image in the screenshot
                screenshot = capture_screen()
                match, match_location = find_image(target_image, screenshot)

                # If the match value is greater than or equal to the threshold
                if match:
                    print(f"Target image found at coordinates: {match_location}.")
                    # Increment the total finds
                    total_finds += 1
                    perform_click(match_location, click_type)
                    time.sleep(SLEEP_TIME)
                    print("Waiting for the next match...")
                    # perform_click(match_location, click_type)

            except Exception as e:
                print(f"Error during image processing: {e}")
                time.sleep(1)  # Pause to avoid continuous error printing

    # Handle keyboard interrupt exception
    except KeyboardInterrupt:
        print("Script terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        dest="target_image_path",
        type=str,
        help="The path to the target image (default: %(default)s)",
        default=TARGET_IMAGE_PATH,
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        help="Matching threshold for identifying the target image (default: %(default)s)",
        default=THRESHOLD,
    )
    parser.add_argument(
        "-c",
        "--click-type",
        type=str,
        choices=["left", "right"],
        help="Type of click to perform ('left' or 'right') (default: %(default)s)",
        default="left",
    )
    parser.add_argument(
        "-s",
        "--sleep-time",
        type=str,
        help="Time to delay after click in seconds (default: %(default)s)",
        default=SLEEP_TIME,
    )

    args = parser.parse_args()

    print("Auto-Clicker is running...")
    try:
        main(args.target_image_path, args.threshold, args.click_type)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
