# Remote-emotions
This repository hosts the coding created to realise the two works described in the paper ‘Remote Emotions: web applications as interfaces for performers and audience to classify the emotional content of their voices live and as tools for Computer-Assisted-Composition’.

The folder **app_composition** contains the Flask application with which the violinist can record and classify sounds into 8 emotion categories as well as send data to four ESP32 microcontrollers. In the same folder, there is also an anonymised copy of the **music score**. Inside the **ESP32** folder one can find the code in Micropython used for the microcontrollers.

The folder **Model&Data_preparation** contains the Python code for preparing the datasets and a second one to train the CNN model used by both works in this repository.

The folder **app_installation** contains a Flask web-application, which can be accessed remotely, and a local Flask application, which connects the global app and a Pure Data patch — MAIN.pd, which controls the sound processing of an installation. Inside the folder **Pd_patches** one can find all the necessary Pure Data files.
