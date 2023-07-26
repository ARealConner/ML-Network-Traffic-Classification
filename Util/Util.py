import os

import pandas as pd


def get_results_location(models_folder, model_name: str):
    """
    Get the location of the results file for saving test results.
    If folder and file do not exist, they are created.

    :param models_folder: The type of model we are training - this decides where the trained model is saved
    :param model_name: the name of the file to save the model to
    :type model_name: str
    :return: the location of the result's file
    :rtype: str
    """
    location = os.path.join(models_folder + "/results/", model_name)
    os.makedirs(location, exist_ok=True)
    return os.path.join(location, "results.txt")


def get_model_location(models_folder, model_name: str):
    """
    Retrieves a path to a saved model in the format
    <models_folder>/models/<model_name>/model.pkl
    from current directory (should be called from main).

    :param models_folder:
    :param model_name: A sub-folder in <model type>/models/ to <model name>
    :type model_name: str
    :return: the relative path to the model from current dir, None if model does not exist
    :rtype: str
    """
    location = os.path.join(models_folder + "/models/", model_name)
    if os.path.isfile(os.path.join(location, "model.pkl")):
        os.makedirs(location, exist_ok=True)
        return os.path.join(location, "model.pkl")
    else:
        print("file does not exist")
        return None


def set_model_location(models_folder, model_name):
    """
    Function to create the model in the models folder of the selected model type.

    :param models_folder: the type of model we are training - this decides where the trained model is saved
    :type models_folder: str
    :param model_name: sub-folder under models is named for the current tested model
    :type model_name: str
    :return: relative path to the folder from project root
    :rtype: str
    """
    location = os.path.join(models_folder + "/models/", model_name)
    os.makedirs(location, exist_ok=True)
    return os.path.join(location, "model.pkl")


def load_dataset(filename):
    """
    Read dataset into DataFrame structure

    :param filename: Name of the file to load
    :return: DataFrame structure (pandas) of dataset
    """
    df = pd.read_csv(filename, low_memory=False)
    df.info(verbose=True)  # Print details about the dataset
    return df


def prepare_data(df, attributes=None, length=-1):
    """
    Prepare data for training

    Note: May be irrelevant, @Corey adjust as needed for the changes

    :param df: "Data frame" Data loaded from csv
    :param attributes: Data headers to normalize into integer values SVM: ["Dst_Pt", "Src_IP", "Bytes", "Label"]
    :param length: Length of data to prepare
    :return:
        x, y (tuple):
            x = Samples
            y = Labels
    """
    if length > 0:
        df = df.iloc[:length]

    if attributes is not None:
        df = df[attributes]

    # convert Flags column to numeric via factorize
    df.loc[:, "Flags"] = pd.factorize(df["Flags"])[0]

    x = df.drop(columns=["Label"])
    y = df["Label"]

    # debug print
    print(str(len(df)) + " examples in dataset")

    return x, y
