# YOLO Object Detection for Ticket Booking Agency

This repository contains the code for training and implementing YOLO (You Only Look Once) object detection on ticket images in the context of the Online Ticket Booking Agency application. YOLO is a powerful deep learning-based object detection algorithm that can identify ticket bounding boxes in images, enabling automated ticket verification and processing.

## Data Preparation

The code reads ticket images and corresponding ground truth information (bounding box annotations) from the `Data/images/` and `Data/ground_truth/` directories, respectively. It preprocesses the data to create training examples for YOLO.

## Model Training

The YOLO model is trained using Next.js, TypeScript, and Tailwind CSS. The data is fed into the model to learn ticket object detection based on predefined grid sizes. The model outputs bounding boxes and confidence scores for each ticket detected in an image.

## Running the Application

To run the ticket booking agency application with YOLO object detection:

1. Clone this repository to your local machine using the following command:
   ```
   git clone <repository_url>
   ```

2. Install the required dependencies by running the following command:
   ```
   pip install numpy pandas opencv-python tqdm scipy matplotlib
   ```

3. Ensure that you have the necessary ticket images and ground truth data in the correct directories, as described in the code.

4. Execute the Python script to preprocess the data and train the YOLO model:
   ```python
   import numpy as np
   import pandas as pd
   import cv2
   import os
   import tqdm
   from scipy.io import loadmat
   import matplotlib.pyplot as plt
   ```

5. After training, the application will perform object detection on a few sample ticket images, displaying the processed images with bounding boxes around the tickets.

## Contribution

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Thank you for visiting this repository! Get ready to revolutionize the ticket booking experience with YOLO object detection for the Online Ticket Booking Agency.
