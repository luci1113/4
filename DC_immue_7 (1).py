import numpy as np 
from sklearn.metrics import classification_report

class AIRS: 
    
    
    '''def __init__(self, num_detectors=1000, hypermutation_rate=0.1):: This line defines the constructor method for the AIRS class. The __init__ method is called automatically when an instance of the class is created.
self: self is a reference to the current instance of the class. It is used to access variables and methods within the class.
num_detectors=1000: This parameter sets the default number of detectors to 1000 if not explicitly provided when creating an instance of the class.
hypermutation_rate=0.1: This parameter sets the default hypermutation rate to 0.1 if not explicitly provided when creating an instance of the class.
self.num_detectors = num_detectors: This line assigns the value of the num_detectors parameter to the num_detectors attribute of the current instance of the class using self. This attribute represents the number of detectors used in the AIRS algorithm.
self.hypermutation_rate = hypermutation_rate: This line assigns the value of the hypermutation_rate parameter to the hypermutation_rate attribute of the current instance of the class using self. This attribute represents the hypermutation rate used in the AIRS algorithm.'''
    def __init__(self, num_detectors=1000, hypermutation_rate=0.1): 
        self.num_detectors = num_detectors 
        self.hypermutation_rate = hypermutation_rate 
    
    def train(self, X, y): 
        
        self.detectors = X[np.random.choice(len(X), self.num_detectors, replace=False)] 
    
    '''def predict(self, X):: This line defines the predict method within the AIRS class. The method takes self (which refers to the current instance of the class) and X as parameters. X represents the input data (samples) for which predictions are to be made.
predictions = []: This line initializes an empty list to store the predicted labels for each sample in X.
for sample in X:: This line starts a loop over each sample in the input data X.
distances = np.linalg.norm(self.detectors - sample, axis=1): This line calculates the Euclidean distance between the input sample sample and each detector in self.detectors. np.linalg.norm is used to compute the Euclidean norm, and axis=1 specifies that the norm should be calculated along the second axis, resulting in an array of distances for each detector.
prediction = int(np.argmin(distances)): This line finds the index of the detector with the minimum distance to the input sample using np.argmin, and converts it to an integer. This index represents the predicted class label for the input sample.
predictions.append(prediction): This line appends the predicted label to the predictions list.
return predictions: Finally, this line returns the list of predicted labels for all samples in X.'''
    def predict(self, X): 
        predictions = [] 
        for sample in X: 
            distances = np.linalg.norm(self.detectors - sample, axis=1) 
            prediction = int(np.argmin(distances)) 
            predictions.append(prediction)
        return predictions 


def generate_dummy_data(samples=100, features=40): 
    data = np.random.rand(samples, features) 
    labels = np.random.randint(0, 2, size=samples) 
    return data, labels 


def split_data(data, labels, split_ratio=0.8): 
    split_index = int(split_ratio * len(data)) 
    train_data, test_data = data[:split_index], data[split_index:] 
    train_labels, test_labels = labels[:split_index], labels[split_index:] 
    return train_data, test_data, train_labels, test_labels 

# Evaluate accuracy 
def evaluate_accuracy(predictions, true_labels): 
    accuracy = np.mean(predictions == true_labels) 
    return accuracy

def main(): 
    
    data, labels = generate_dummy_data() 
    
    train_data, test_data, train_labels, test_labels = split_data(data, labels) 
    
    airs = AIRS(num_detectors=10, hypermutation_rate=0.1) 
    airs.train(train_data, train_labels) 
    '''Initialize and Train AIRS Model:
An instance of the AIRS class is created with specific parameters (num_detectors=10, hypermutation_rate=0.1). This instance represents the Artificial Immune Recognition System (AIRS) model.
The train() method of the AIRS model is called to train the model on the training data (train_data) along with their corresponding labels (train_labels). 
During training, the AIRS model learns to recognize patterns in the data and creates detectors accordingly.'''
  
    predictions = airs.predict(test_data) 
    
    accuracy = evaluate_accuracy(predictions, test_labels) 
    print(f"Accuracy: {accuracy}") 

   

if __name__ == "__main__": 
    main()

