# Smart-Sprayer-Rover
Smart Sprayer Rover is an ESP32-based agricultural robot that# uses AI to detect unhealthy plant leaves and automatically spray pesticides or fertilizers. It helps reduce chemical wastage, saves labor, and supports smart farming.

# Overview
The Smart Sprayer Rover is an IoT-based agricultural robot designed to automate crop monitoring and spraying operations. The rover uses Artificial Intelligence (AI) to detect plant health through image processing and automatically sprays pesticides or fertilizers only on affected plants. This approach reduces chemical wastage, saves labor, and improves farming efficiency.
The project combines robotics, IoT, computer vision, and automation technologies to support precision agriculture and smart farming.

# Features
🌿 AI-based leaf health detection (Healthy/Unhealthy)
📷 Real-time image capture using a camera
🚜 Autonomous rover movement
📏 Obstacle detection using ultrasonic sensors
💧 Automatic pesticide/fertilizer spraying
🌐 Web-based monitoring and control interface
📡 Wireless communication using ESP32
⚡ Low-cost and efficient smart farming solution

# Hardware Components
ESP32 Development Board
L298N Motor Driver
DC Geared Motors (60 RPM)
Ultrasonic Sensor (HC-SR04)
Water Pump
Relay Module
Rover Chassis
Battery Pack (12V)
Camera (Laptop/Web Camera or ESP32-CAM)
Connecting Wires

# Software Requirements
Python
Thonny IDE / VS Code
Arduino IDE
Machine Learning Model (CNN)
HTML, CSS, JavaScript
ESP32 Libraries

# System Architecture
Camera captures plant leaf images.
AI model classifies the leaf as Healthy or Unhealthy.
If the leaf is unhealthy:
Command is sent to ESP32.
Water pump is activated.
Pesticide/Fertilizer is sprayed.
Ultrasonic sensor detects obstacles and helps navigation.
Data and rover status are displayed on the web interface.

# Working Principle
The rover moves through the agricultural field while continuously monitoring plants. Images captured by the camera are processed using a trained AI model. The model identifies whether the plant is healthy or unhealthy.
When an unhealthy plant is detected, the ESP32 receives the command and activates the pump through a relay module. The spraying process targets only affected plants, reducing unnecessary chemical usage.
The web interface allows users to monitor rover activity and control operations remotely.

# Technologies Used
Internet of Things (IoT)
Artificial Intelligence (AI)
Computer Vision
Machine Learning (CNN)
Embedded Systems
Robotics
Wireless Communication

# Applications
Smart Agriculture
Precision Farming
Automated Pesticide Spraying
Crop Health Monitoring
Research and Educational Projects

# Advantages
Reduces chemical wastage
Saves labor and time
Improves crop management
Increases farming efficiency
Low-cost automation solution
Environment-friendly spraying approach

# Future Improvements
GPS-based navigation
Solar-powered operation
Mobile application integration
Multi-disease detection
Real-time cloud data logging
Autonomous path planning

# Project Outcome
The Smart Sprayer Rover demonstrates how AI, IoT, and robotics can be integrated to create an intelligent agricultural system capable of monitoring crop health and performing automated spraying operations. The project contributes to modern precision farming by improving efficiency, reducing resource consumption, and supporting sustainable agriculture.
