import numpy as np
from sklearn.metrics import classification_report
class NegativeSelectionAlgorithm:
    def __init__(self, threshold=0.1):
        self.threshold = threshold
        self.detector_set = None

    def train(self, X_train):
        self.detector_set = self.generate_detector_set(X_train)

    def predict(self, X_test):
        if self.detector_set is None:
            raise Exception("Model not trained")

        predictions = []
        for sample in X_test:
            is_anomaly = self.detect_anomaly(sample)
            predictions.append(1 if is_anomaly else 0)
        return predictions

    def generate_detector_set(self, X_train):
        detector_set = []
        # Generate detector set using X_train
        # For simplicity, let's randomly select a subset of X_train as detectors
        num_detectors = len(X_train) // 10  # Choose 10% of the data as detectors
        detector_indices = np.random.choice(len(X_train), num_detectors, replace=False)
        detector_set = X_train[detector_indices]
        return detector_set

    def detect_anomaly(self, sample):
        for detector in self.detector_set:
            # Calculate similarity between sample and detector (e.g., Euclidean distance)
            similarity = np.linalg.norm(sample - detector)
            # If similarity is below threshold, sample is considered an anomaly
            if similarity < self.threshold:
                return False  # Not an anomaly
        return True  # Anomaly detected

# Example usage:
# Generate sample data (replace this with your actual data)
X_train = np.random.rand(100, 5)  # 100 samples, 5 features
X_test = np.random.rand(20, 5)  # 20 samples for testing

# Initialize and train the model
ais_model = NegativeSelectionAlgorithm(threshold=0.1)
ais_model.train(X_train)

# Predict anomalies in the test data
predictions = ais_model.predict(X_test)
print("Predictions:", predictions)

# Rename the variable to avoid conflict with the imported function
report = classification_report(predictions, X_test)
print(f"Classification Report: {report}")
