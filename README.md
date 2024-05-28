# Posture Correction Chair using Reinforcement Learning

## Overview

This project aims to improve users' sitting posture by providing real-time feedback. Good posture while working is crucial for maintaining a healthy life. Bad posture can lead to various health issues such as spinal dysfunction, incontinence, constipation, heartburn, and slowed digestion, as reported by the Harvard Medical School. The posture correction chair is designed to help users maintain an ideal posture during long sitting periods by providing corrective feedback based on posture analysis.

## Hardware Requirements

- **Chair with Integrated Sensors**: The chair is equipped with six sensors to calculate the user's posture.
- **Microcontroller**: This is used to process sensor data and provide feedback.
- **Feedback Mechanism**: This can be auditory, visual, or haptic feedback to alert the user about their posture.

<table>
  <tr>
    <td><img src="https://github.com/dheerajkallakuri/Posture-Correction-Chair/assets/23552796/24804d8f-e95d-44ea-84fc-83855b29f499" alt="cr1" height="300"></td>
    <td><img src="https://github.com/dheerajkallakuri/Posture-Correction-Chair/assets/23552796/9034e26a-74a7-42c0-8b06-e797183cd3d1" alt="cr2" height="300"></td>
  </tr>
</table>

## Description

The posture correction chair works by:
1. **Sensor Data Collection**: Six sensors installed in the chair continuously monitor the user's posture.
2. **State Definition**: The collected posture data defines the user's current state.
3. **Policy Creation**: A reinforcement learning algorithm, utilizing the Markov Decision Process (MDP), is used to map states to actions (feedback recommendations).
4. **Feedback Generation**: Based on the policy, the system generates feedback to encourage the user to adopt an ideal sitting posture.

### Setup
- Load `sesnor_fusion.ino` in Arduino connected to the computing device.
- Run `pcc.gui` on the computing device.

### Reinforcement Learning

Reinforcement learning (RL) is a reward-driven learning algorithm where agents make decisions to maximize cumulative rewards. In this project:
- **Markov Decision Process (MDP)**: Used to map states (postures) to actions (feedback).
- **Policy**: Defines the optimal state-action mapping to ensure users maintain an ideal posture using the Policy iteration algorithm.

### Graphical User Interface Overview

This section outlines the key components and functionalities of the graphical user interface for monitoring and improving user posture based on sensor data.

#### Textboxes for Sensor Values (Sensor1-Sensor6)
- **Purpose**: Display the weight distribution across six sensors as percentages.
- **Usage**: Helps users understand how their weight is distributed on the chair.

#### Action Textbox
- **Purpose**: Displays status messages and actionable instructions for the user to achieve a good posture.
- **Messages Displayed**:
  - **CALIBRATION IN PROGRESS**: Shown when the calibration button is clicked while the user is in a good posture.
  - **CALIBRATION IS DONE**: Shown once the calibration process for a good posture is completed.
  - **No one is sitting**: Displayed when sensor readings are between 0 and 2, indicating the chair is not in use.
  - **Ideal Position**: Displayed when the user sits in the calibrated ideal posture.
  - **Set of Actions**: Displayed when the user is not in the ideal position, providing specific actions such as "shift left," "shift right," or "shift back" to help the user correct their posture.

#### Pose Textbox
- **Purpose**: Indicates the overall posture quality.
- **Messages Displayed**:
  - **Good Pose**: Shown when the user is in the ideal position.
  - **Bad Pose**: Shown for any position other than the ideal posture.

#### Graph
- **Purpose**: Visualizes the live sensor data.
- **Details**: Plots time vs. percentage values to show how weight distribution changes over time.

#### Buttons
1. **Calibration Button**
   - **Purpose**: Calibrates the system to recognize the user's good posture.
   - **Usage**: The user should sit in their ideal posture and click this button. The system then records the weight distribution for future reference.
   
2. **Start Button**
   - **Purpose**: Begins real-time monitoring and data processing.
   - **Usage**: When clicked, the system starts displaying real-time sensor values in the Sensor1-Sensor6 textboxes, updates the graph, and provides feedback in the action textbox.
   
3. **Stop Button**
   - **Purpose**: Stops all monitoring and data processing.
   - **Usage**: Resets sensor values to 0, clears the graph, and halts data processing.

This interface ensures users can monitor their posture in real-time and receive actionable feedback to maintain or achieve an ideal sitting posture. The calibration process helps tailor the feedback to the user's unique posture, enhancing the system's effectiveness in promoting ergonomic sitting habits.

## Output

<img width="300" height="300" alt="random iteration" src="https://github.com/dheerajkallakuri/Posture-Correction-Chair/assets/23552796/0cefa011-6026-48d7-a88b-14ae2b2b8d22">

The system will provide real-time feedback to the user, encouraging them to maintain an ideal sitting posture. The feedback will help in:
- Reducing the risk of health issues associated with bad posture.
- Improving overall sitting habits during long working hours.

## Presentation

![Presentation Preview](Presentation.pdf)

## Video Demonstration

For a visual demonstration of this project, please refer to the video linked below:

[Project Video Demonstration](https://youtu.be/rPdr48VaFvE)

[![Project Video Demonstration](https://img.youtube.com/vi/rPdr48VaFvE/0.jpg)](https://www.youtube.com/watch?v=rPdr48VaFvE)


