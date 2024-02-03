import pyautogui
import numpy as np
import cv2

from config import THRESHOLD


def capture_screen():
    """
    Capture the current screen
    :return: the screenshot image
    """
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


def find_image(template, screenshot):
    """
    Find the template image in the screenshot using SIFT feature matching
    :param template: the template image
    :param screenshot: the screenshot image
    :return: the match value and the location of the match
    """
    # Convert images to grayscale
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Initialize the SIFT detector
    sift = cv2.SIFT_create()

    # Find keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(gray_template, None)
    kp2, des2 = sift.detectAndCompute(gray_screenshot, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    # FLANN based matcher
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Get the location of the best match
    if len(good_matches) > THRESHOLD:  # Adjust the threshold as needed
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(
            -1, 1, 2
        )
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(
            -1, 1, 2
        )
        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        h, w = gray_template.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(
            -1, 1, 2
        )
        dst = cv2.perspectiveTransform(pts, M)
        match_location = (int(dst[0][0][0]), int(dst[0][0][1]))
        return True, match_location
    else:
        return False, None


def perform_click(coordinates, click_type):
    """
    Perform a left or right click at the specified coordinates
    :param coordinates: tuple of x and y coordinates
    :param click_type: type of click ("left" or "right")
    :return: None
    """
    if click_type == "left":
        pyautogui.leftClick(coordinates[0], coordinates[1])
    elif click_type == "right":
        pyautogui.rightClick(coordinates[0], coordinates[1])
    else:
        raise ValueError("Invalid click_type. Expected 'left' or 'right'.")
