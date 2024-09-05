Project Overview:
This project aims to develop a real-time sign language detection system that can interpret hand gestures into corresponding letters using machine learning techniques. The key tools being used include Python, TensorFlow, OpenCV, and MediaPipe. The project focuses on detecting hand gestures from a video feed, processing the gestures using a model, and translating them into readable text.

Team Members:
Samyog Sah
Sujit Manandhar
Nabin Bhattarai

Develop a machine learning model using TensorFlow to detect and classify hand gestures.
Implement real-time video feed capture using OpenCV to process hand gestures.
Integrate MediaPipe for hand landmark detection.
Translate gestures into corresponding letters for communication.
Progress to Date:
Project Setup and Environment Configuration:

Installed necessary libraries such as TensorFlow, OpenCV, MediaPipe, NumPy, and Pandas.
Set up the development environment using PyCharm, created the project structure, and initialized the dataset.
Dataset Preparation:

The dataset required for the detection of hand gestures has been collected and structured.
Classes for different hand gestures were labeled and stored in a structured format for training.
Model Development:

A TensorFlow model has been developed using the keypoint classifier approach.
The model has been trained using the pre-processed dataset, focusing on hand gesture recognition.
Model validation and testing have been performed on a small set of test data, and initial results show good accuracy.
Real-Time Detection:

Integrated OpenCV to capture live video feed for real-time gesture detection.
Implemented MediaPipe for detecting and tracking hand landmarks, which are processed by the model.
Real-time detection is working, and the system is able to translate gestures into letters.
Literature Review:

Reviewed and analyzed several research papers related to social media algorithms and their impact on online behavior, providing insights for future improvements in AI algorithms.
Research papers studied include:
Impact of Social Media Algorithms on Online Communities' Behavior
How Social Media Algorithms Influence User Decision Making
Documentation:

Organized the project's documentation, including an introduction, significance, and literature review.
Updated project progress in Trello for team collaboration and task tracking.
Challenges:
Real-Time Performance: The system's accuracy and speed need further optimization for handling real-time detection efficiently without significant lag.
Dataset Imbalance: The dataset requires further augmentation to ensure that all gestures are evenly represented for better model performance.
UI Development: Currently, the system does not have a user interface, and the output is reflected only on the terminal and OpenCV window.
Next Steps:
Continue optimizing the model for real-time performance.
Expand the dataset by collecting more samples for training and validation.
Implement additional features like gesture-to-word translation and a more comprehensive interface for better usability.
Finalize the documentation, covering research methodology, conclusions, and user guide.
Conclusion:
The project is on track, with significant progress made in dataset preparation, model development, and real-time gesture detection. The team is working toward improving performance and expanding the model's capability to cover more gestures and enhance accuracy. Ongoing documentation and research will support the successful completion of the project.

############################USER MANUAL######################

# Overview

This ASL Detector is a cutting-edge AI-powered application that uses computer vision and deep learning to recognize and classify American Sign Language (ASL) characters in real-time. This application utilizes the device's camera to capture hand landmarks and coordinates, which are then processed by a deep learning model to identify the corresponding ASL character.

<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/6945d009-8aa7-4bf7-99f8-9743662c5248" width="50%">
</p>

# Usage
By default, when you launch app.py, the inference mode is active. It can also be manually activated in other modes by pressing “n”.

<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/16ed949f-5aa8-4ed4-b49e-a7eb365c8923" width="60%">
</p>

# Table of Contents

1. [Features](#Features)
2. [Requirements](#Requirements)
3. [Installation](#Installation)
4. [Model Training](#Model-Training)
5. [Contributing](#Contributing)


# Features

- **Real-time ASL detection using the device's camera.**
- **Accurate classification of ASL characters using a deep learning model.**
- **Hand landmark tracking for precise gesture recognition.**
- **Support for a wide range of ASL characters and phrases.**
- **High accuracy and robustness in varying lighting conditions.**

# Requirements:

- OpenCV
- MediaPipe
- Pillow
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Matplotlib
- Tensorflow

> [!IMPORTANT]
> If you face an error during training from the line converting to the tflite model, use TensorFlow v2.16.1.

# Installation:

1. Clone the Repository:

```
git clone https://github.com/SamyogSah/Sign-Language-Detection.git
```

3. Install Dependencies:

```
pip install -r requirements.txt
```

4. Run the Application:

```
python main.py
```

# Model Training

If you wish to train the model on your dataset, follow these steps:

   ### Data Collection

1. Manual Key Points Data Capturing

Activate the manual key point saving mode by pressing "k", which will be indicated as “MODE: Logging Key Point”.<br>
If you press any uppercase letter from “A” to “Z”, the key points will be recorded and added to the “model/keypoint_classifier/keypoint.csv” file as demonstrated below.

<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/e0393472-f7c6-41f7-b5a6-3814dc4b7044">
<p/>

> [!NOTE]
> Each time you press the uppercase letter a single entry point is appended to keypoint.csv.

2. Automated Key Points Data Capturing

Activate the automatic key point saving mode by pressing "d", which will change the content of the camera window to an image of OM606.
<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/f4b11849-7fd9-423b-aee3-efa31f300159" width="70%"><br>
<p/>

> [!NOTE]
> You need to specify the dataset directory in ```app.py```

   ### Training

Launch the Jupyter Notebook "[keypoint_classification.ipynb](keypoint_classification.ipynb)" and run the cells sequentially from the beginning to the end.<br>
If you wish to alter the number of classes in the training data, adjust the value of "NUM_CLASSES = 26" and make sure to update the labels in the "[keypoint_classifier_label.csv](model/keypoint_classifier/keypoint_classifier_label.csv)" file accordingly.
<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/0a4c4ce9-4afa-4852-a410-2b9bb280e4b8" width="70%"><br>
<p/>

   ### Model Structure

The following is the image of the model structure that was prepared in the "[keypoint_classification.ipynb](keypoint_classification.ipynb)" notebook.

<p align="center">
   <img src="https://github.com/AkramOM606/American-Sign-Language-Detection/assets/162604610/e0940c53-f12b-46da-8526-2ffb9a011634">
<p/>

