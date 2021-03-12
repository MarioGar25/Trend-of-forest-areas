import pandas as pd

def get_predictions(y_real, y_pred):
    try:
        df = pd.DataFrame(y_real)
        df["prediction"] = y_pred
        return df
    except ValueError as error:
        print(error)
        print(f"The parameters must have the same length")

def plot_importances(model, data):
    sorted_importances = model.feature_importances_.argsort()
    
    plt.figure(figsize=(15,15))
    
    return plt.barh(data.columns[sorted_importances], model.feature_importances_[sorted_importances])

def get_merge(data, y_pred):
    return pd.merge(data, pd.DataFrame(y_pred, columns=["y_pred"]), left_index=True, right_index=True)
  