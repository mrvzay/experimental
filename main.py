import matplotlib.pyplot as plt
X = list(range(0, 100))
y = list(range(0, 200, 2))

# plt.scatter(X , y)
# plt.axis("off")
# plt.title("Sample plot (figure)")
# plt.xlabel("Heghit")
# plt.ylabel("width")
# plt.show()

import sklearn
print(sklearn.__version__)


from sklearn.model_selection import train_test_split
train = int(0.3 * len(X))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train, random_state=42)
len(X), len(y), len(X_train), len(X_test), len(y_train), len(y_test)

# Plot the train data and test data train data in gree color, test data color red
def plot_train_test_data(train_data: int = X_train,
                         train_labels: int = y_train,
                         test_data: int = X_test,
                         test_labels: int = y_test,
                         predictions: int = None):
    """Train and test data ploting (figures) 

    Args:
        train_data (int, optional): _description_. Defaults to X_train.
        train_labels (int, optional): _description_. Defaults to y_train.
        test_data (int, optional): _description_. Defaults to X_test.
        test_labels (int, optional): _description_. Defaults to y_test.
        predictions (int, optional): _description_. Defaults to None.
    """

    plt.figure(figsize=(10, 7))
    # Train data in green color
    plt.scatter(train_data, train_labels, color="green", label="Train")
    # Test data in blue color
    plt.scatter(test_data, test_labels, color="blue", label="Label")
    # Predictions data in red
    if predictions is not None:
        plt.scatter(train_labels, predictions, color="red", label="Predictions")
    plt.axis(False)
    plt.show()

# Visualize train and test data
plot_train_test_data()