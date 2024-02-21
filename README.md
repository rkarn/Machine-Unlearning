# Machine Unlearning for MNIST

Machine unlearning refers to the process of removing or updating the knowledge related to specific classes or instances from a trained model. 

## 1. Decision Tree:
One approach to achieve unlearning with decision trees involves retraining the model on the remaining data after removing the instances corresponding to the forget classes. However, this method may not be very efficient or practical, especially for large datasets or complex models, as it requires significant computational resources to retrain the model from scratch.

Alternatively, you can implement custom unlearning mechanisms by modifying the decision tree model directly. For example, you can adjust the decision thresholds, prune the tree to remove specific branches, or incorporate forgetting mechanisms into the learning algorithm.

It's important to note that unlearning in machine learning is still an active area of research, and there isn't a one-size-fits-all solution for every scenario. 

**So in this work, the modification of the tree to remove the branches corresponding to the forget class is adopted.**

**In the jupyternotebook, the first part show difficulty in pruning the nodes/branch. So an alternate mechansim is adopted where a chain of if\else statements are added.**



In machine unlearning, when the samples of forget classes are fed to the model after the unlearning process, the behavior of the model can vary depending on the specific unlearning technique employed and how the model is designed to handle such cases. Here are some possible scenarios:

- Model Outputs Invalid Predictions: If the unlearning process removes the knowledge related to the forget classes entirely from the model, then when samples of forget classes are fed to the model, it might output invalid predictions or predictions unrelated to any known class. This is because the model no longer has the ability to recognize or classify samples from the forget classes.
- Model Outputs Probabilities: Some unlearning techniques involve updating the model to output probabilities for each class. In this case, even after unlearning, the model may still output probabilities for all classes, including the forget classes. However, the probabilities associated with the forget classes may be significantly lower compared to other classes.
- Model Outputs Special Tokens: In certain scenarios, the model may be designed to output special tokens or indicators when it encounters samples from forget classes. These special tokens may indicate that the model has recognized the sample as belonging to a forget class or that the model is uncertain about the prediction due to encountering a forget class.
- Model Outputs Previous Knowledge: Depending on the unlearning technique used, the model may retain some level of previous knowledge related to forget classes. In this case, when samples of forget classes are fed to the model, it might still exhibit behaviors similar to when it was trained on those classes, although the model's performance on forget classes might degrade over time as it continues to adapt to new data.

Overall, the behavior of the model when samples of forget classes are fed to it after the unlearning process depends on various factors, including the specific unlearning technique used, the model architecture, and how the model is designed to handle forget classes. It's important to carefully design and evaluate the unlearning process to ensure appropriate handling of forget classes and to maintain the model's performance over time.

**In this work, the label `0` has been assigned for forget class samples if it is fed to the model.**


## 2. Neural Network: 

