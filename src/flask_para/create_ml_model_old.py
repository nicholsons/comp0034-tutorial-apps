"""
Machine learning is not covered in the module.
This is a simple example of how to create a model using the medal standings data.
`pip install scikit-learn` is required before you can run this code.
"""
import pickle
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


def create_model(alg, output_file):
    """Creates a model using the algorithm provided. Output serialised using pickle.

    Args:
    alg: either lr (LogisticRegression) or dt (DecisionTreeClassifier)
    output_file: name of the output file to save the model

    Returns:
    .pkl Pickled model

    """
    # Initialize the model
    if alg == "dt":
        model = DecisionTreeClassifier()
    elif alg == "lr":
        model = LogisticRegression()
    else:
        raise ValueError("Must provide either 'dt' (DecisionTree) or 'lr' (LogisticRegression)")

    # Read the data into a DataFrame
    para_excel = Path(__file__).parent.parent.joinpath("data", "paralympics.xlsx")
    cols = ["Year", "Rank", "Team", "Gold", "Silver", "Bronze", "Total"]
    df = pd.read_excel(para_excel, sheet_name="medal_standings", usecols=cols)

    # Drop rows with NaNs since the accuracy of the model is not the focus here
    df.dropna(inplace=True)

    # Convert categorical data to numeric
    le = LabelEncoder()

    # This is to create a new DataFrame with the team names and their corresponding codes after the encoding
    # Needed later to convert the team name to the code for prediction
    df_teams = pd.DataFrame()
    df_teams["Teams"] = df["Team"]
    df["Team"] = le.fit_transform(df["Team"])
    # save it to file
    df_teams["Code"] = df["Team"]
    df_teams.drop_duplicates(inplace=True)
    df_teams.to_csv("teams.csv", index=False)

    # X = feature values (Year, Team, Rank, NPC, Gold, Silver, Bronze)
    X = df.iloc[:, 0:-1]
    X = X.values
    # y = target value is total medals
    y = df.iloc[:, -1]

    # Split the data into 80% training and 20% testing
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    model.fit(x_train, y_train)

    # Pickle the model and save to current folder
    pickle_file = Path(__file__).parent.joinpath(output_file)
    pickle.dump(model, open(pickle_file, "wb"))


def train_and_save_model():
    """
    Train a model to predict Total based on Year and Team, and save it to a .pkl file.
    """
    # Read the data into a DataFrame
    para_excel = Path(__file__).parent.parent.joinpath("data", "paralympics.xlsx")
    cols = ["Year", "Rank", "Team", "Gold", "Silver", "Bronze", "Total"]
    data = pd.read_excel(para_excel, sheet_name="medal_standings", usecols=cols)

    # Drop rows with NaNs since the accuracy of the model is not the focus here
    data.dropna(inplace=True)

    # Features and target
    X = data[['Year', 'Team']]
    y = data['Total']

    # One-hot encode the 'Team' column
    preprocessor = ColumnTransformer(
        transformers=[
            ('team', OneHotEncoder(), ['Team'])
        ],
        remainder='passthrough'
    )

    # Create a pipeline with preprocessing and regression model
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    pipeline.fit(X_train, y_train)

    # Save the model to a .pkl file
    joblib.dump(pipeline, '../data/model.pkl')

    print("Model saved to model.pkl")



if __name__ == "__main__":
    # Train the model and save it
    train_and_save_model()

    # create_model("dt", "model.pkl")
    # create_model("lr", "model_lr.pkl")
