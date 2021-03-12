import pandas as pd

def get_predictions(y_real, y_pred):
    '''Returns a dataframe with data passed
    Inputs: arrays
    Returns: DataFrame
    '''
    try:
        df = pd.DataFrame(y_real)
        df["prediction"] = y_pred
        return df
    except ValueError as error:
        print(error)
        print(f"The parameters must have the same length")



def plot_importances(model, data):
    '''Plots sorted importances about the features
    Input: Model and Data
    Returns: Plot with the sorted importance of each feature.
    '''
    #Gets the features importances and sorts them
    sorted_importances = model.feature_importances_.argsort()
    #Sets the figure size
    plt.figure(figsize=(15,15))
    #Returns the plot
    return plt.barh(data.columns[sorted_importances], model.feature_importances_[sorted_importances])
  