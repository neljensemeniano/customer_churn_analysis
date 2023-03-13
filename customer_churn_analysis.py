import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class CustomerChurnAnalysis:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def clean_data(self):
        # Drop missing values
        self.data = self.data.dropna()
        # Convert categorical variables to dummy variables
        self.data = pd.get_dummies(self.data, columns=['gender', 'payment_method'])
        # Scale numerical variables
        self.data['tenure'] = (self.data['tenure'] - self.data['tenure'].mean()) / self.data['tenure'].std()
        self.data['monthly_charges'] = (self.data['monthly_charges'] - self.data['monthly_charges'].mean()) / self.data['monthly_charges'].std()

    def train_model(self):
        X = self.data.drop(['customer_id', 'churn'], axis=1)
        y = self.data['churn']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = LogisticRegression().fit(X_train, y_train)

    def predict_churn(self, customer_data):
        customer_data = pd.DataFrame(customer_data, index=[0])
        customer_data = pd.get_dummies(customer
