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

############################USER MANUAL################################################

Overview
