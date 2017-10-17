# Gesture Recognition using Networks Library
The Gesture Recognition dataset was created by <a href="https://github.com/ankitesh97">Ankitesh Gupta</a>. For details on how dataset was created check this cool <a href="https://github.com/ankitesh97/Gesture-Recognition-CNN">repository</a>

The images were Normalized using the <b>Mean Pixel Value</b> and the <b>Standard Deviation of the Pixel Value</b> before giving it to the model for <b>Training and Testing.</b> The code for normalizing the data is in preprocess.py

## Model Results On Gesture Recognition

The Model Consists of the Following Layers:

1) Zero Padding Layer \
  i) Height Padding : 2 \
 ii) Width Padding : 2

2) Convolution Layer \
  i) Kernels : 64 \
 ii) Kernel Height : 3 \
iii) Kernel Width  : 3 \
iv ) Stride        : 1

3) Pooling Layer \
  i) Pooling Height : 2 \
 ii) Pooling Width : 2 \
iii) Stride Height : 2 \
 iv) Stride Width  : 2

4) Relu Layer

5) Zero Padding Layer \
  i) Height Padding : 2 \
 ii) Width Padding : 2

6) Convolution Layer \
  i) Kernels : 128 \
 ii) Kernel Height : 3 \
iii) Kernel Width  : 3 \
iv ) Stride        : 1

7) Pooling Layer \
  i) Pooling Height : 2 \
 ii) Pooling Width : 2 \
iii) Stride Height : 2 \
 iv) Stride Width  : 2
8) Relu Layer

9) Flatten Layer

10) Affine Layer : 128 Neurons

11) Affine Layer : 64 Neurons

12) Affine Layer : 16 Neurons

13) Affine Layer : 5 Neurons (This is the Output Layer)

14) Softmax Layer

After <b>100 Epochs</b> The Model Performance is:

<b>Training Accuracy: 100%</b>

<b>Validation Accuracy: 100%</b>

<b>Test Accuracy:  99.8%</b>

It took about **1-1.5 hour** to train this model for 100 Epochs. \
Initial Weights of the Network were assigned using Xavier Initialization. \
The Model was trained using Mini-Batch Gradient Descent with Adam Optimizer. \
The Mini-Batch was sampled at random during training.
### Loss-Iteration Curve
![Loss-Iteration Curve for 100 Epochs](/Loss_Curve.png)

### Using The Trained Model
1) Download the <a href="https://drive.google.com/open?id=0B6OWaNVUCQvaZF9rV3pOWTFnaEU">Model</a>
2) Extract it in models folder
3) Load the Model using the command below
<pre>
from networks.network import network
model = network.load("model.json")
prediction = model.predict(X)
</pre>
