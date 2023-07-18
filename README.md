# Text Recognition with YOLOv3 and Tesseract OCR

This repository contains a Python script that performs text recognition from an image using the YOLO (You Only Look Once) model for text detection and Tesseract OCR engine for text recognition. The YOLO model is used to detect text regions in the image, and then Tesseract OCR is applied to recognize the text within those regions.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- OpenCV (`cv2`) for image processing
- Tesseract OCR engine with `pytesseract` Python library
- Pre-trained YOLOv3 model weights (`yolov3.weights`) and configuration file (`yolov3.cfg`)
- An input image file (e.g., `img.jpg`) for text recognition

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/text-recognition-yolo-tesseract.git
cd text-recognition-yolo-tesseract
```

2. Install the required Python libraries:

```bash
pip install opencv-python pytesseract
```

3. Download the YOLOv3 model weights and configuration file from the official YOLO website or the YOLO GitHub repository.

4. Ensure Tesseract OCR is installed on your system. You can download it from: https://github.com/tesseract-ocr/tesseract

## Usage

1. Place your input image file (e.g., `img.jpg`) in the same directory as the script.

2. Run the script:

```bash
python text_recognition.py
```

3. The script will detect text regions in the image using YOLO and display the recognized text on the console. It will also save the output image with text regions highlighted as `output.jpg`.

## Important Notes

- The YOLOv3 weights (`yolov3.weights`) and configuration file (`yolov3.cfg`) are large files and are not included in this repository. Please make sure to download them from the official YOLO website or repository before running the script.

- The `coco.names` file is not required for text recognition, and it is used for object detection tasks with the YOLO model. It is not used in this script.

- The text recognition accuracy heavily depends on the quality of the input image and the performance of the YOLO model and Tesseract OCR. Adjusting the confidence thresholds in the code might be necessary for better results.

## License

This code is provided under the [MIT License](LICENSE).

Feel free to contribute to the repository or use it for your text recognition projects!

For any questions or issues, please open an [issue](https://github.com/your-username/text-recognition-yolo-tesseract/issues).

---

_Replace `your-username` in the GitHub repository URL with your actual GitHub username._
