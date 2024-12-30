# Machine Unlearning for Neural Network

Machine unlearning typically refers to the process of removing or forgetting information associated with a specific class or subset of data from a machine learning model. This can involve forgetting `a type of class entirely`, `removing samples` belonging to a particular class, or adjusting the model's parameters `to reduce the influence of specific classes or samples`.

In machine unlearning, when the samples of forget classes are fed to the model after the unlearning process, the behavior of the model can vary depending on the specific unlearning technique employed and how the model is designed to handle such cases. Here are some possible scenarios:

- Model Outputs Invalid Predictions: If the unlearning process removes the knowledge related to the forget classes entirely from the model, then when samples of forget classes are fed to the model, it might output invalid predictions or predictions unrelated to any known class. This is because the model no longer has the ability to recognize or classify samples from the forget classes.
- Model Outputs Probabilities: Some unlearning techniques involve updating the model to output probabilities for each class. In this case, even after unlearning, the model may still output probabilities for all classes, including the forget classes. However, the probabilities associated with the forget classes may be significantly lower compared to other classes.
- Model Outputs Special Tokens: In certain scenarios, the model may be designed to output special tokens or indicators when it encounters samples from forget classes. These special tokens may indicate that the model has recognized the sample as belonging to a forget class or that the model is uncertain about the prediction due to encountering a forget class.
- Model Outputs Previous Knowledge: Depending on the unlearning technique used, the model may retain some level of previous knowledge related to forget classes. In this case, when samples of forget classes are fed to the model, it might still exhibit behaviors similar to when it was trained on those classes, although the model's performance on forget classes might degrade over time as it continues to adapt to new data.

Overall, the behavior of the model when samples of forget classes are fed to it after the unlearning process depends on various factors, including the specific unlearning technique used, the model architecture, and how the model is designed to handle forget classes. It's important to carefully design and evaluate the unlearning process to ensure appropriate handling of forget classes and to maintain the model's performance over time.

**In this work, the label `0` has been assigned for forget class samples if it is fed to the model.**


## 1. Neural Network in General: 
It is in the "Unlearning Neural Network.ipynb" file. 

Zeroing out the weights only in the output layer is a simplistic approach and may not fully remove the influence of the forgotten class from the model. A more comprehensive approach would involve adjusting the weights in all layers of the network to mitigate the impact of the forgotten class. 

One way to achieve this is by fine-tuning the model using a modified loss function or regularization technique that penalizes the model for predicting the forgotten class. However, this process would involve retraining the model to some extent, which should be avoided.

Another approach is to directly manipulate the weights in all layers of the network to minimize the influence of the forgotten class. This could be done through various techniques, such as weight pruning, where weights corresponding to the forgotten class are set to zero or reduced in magnitude. However, implementing such techniques manually would be complex and may not guarantee optimal performance.  `We use this method in out implementation.`

Ultimately, completely removing the influence of a forgotten class without retraining the model is a challenging problem and may not have a straightforward solution. Depending on the specific requirements and constraints of your application, you may need to balance the trade-offs between computational complexity, model performance, and the desired level of forgetting.

## 2. Progressive Learning:

For progressive learning, it is showin in `Unlearning_ProgressiveLearning_MNIST.ipynb` and `Unlearning_ProgressiveLearning_MNIST_Randomization.ipynb` where task is forgetted for dynamic neural architecture. For the static architecture, synaptic intelligence mechanism is used. In notebooks `MNIST_unlearning_SynapticIntelligence.ipynb` and `Unlearning_ProgressiveLearning_MNIST.ipynb` the forget weights are zeroed out while in notebooks `MNIST_unlearning_SynapticIntelligence_Randomization.ipynb` and `Unlearning_ProgressiveLearning_MNIST_Randomization.ipynb` the forget weights are assigned with random numbers.`


# Future Work:
Investigating partial unlearning for tasks within progressive learning presents a promising avenue for future research. Instead of completely unlearning a task, the focus would be on selectively forgetting specific patterns within a subset of classes. We have demonstrated the unlearning mechanism within a FF-FC-NN architecture. It remains to be explored how this mechanism may evolve when applied to convolutional, recurrent, and graph neural network architectures within a progressive learning framework.
