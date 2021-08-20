import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

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
  

def plot_ROC_curve(y, pred_proba, classes = 3, style = "seaborn", title = "Multiclass"):
    '''Plots ROC curve
    Inputs: 
        y: Target variable
        pred_proba: Prediction probabilities 
        classes: Distinct values in the target variable. Default = 3
        style: matplotlib figure style. Default = "seaborn"
             Options
            ---------------------
            'Solarize_Light2',
            '_classic_test_patch',
            'bmh',
            'classic',
            'dark_background',
            'fast',
            'fivethirtyeight',
            'ggplot',
            'grayscale',
            'seaborn',
            'seaborn-bright',
            'seaborn-colorblind',
            'seaborn-dark',
            'seaborn-dark-palette',
            'seaborn-darkgrid',
            'seaborn-deep',
            'seaborn-muted',
            'seaborn-notebook',
            'seaborn-paper',
            'seaborn-pastel',
            'seaborn-poster',
            'seaborn-talk',
            'seaborn-ticks',
            'seaborn-white',
            'seaborn-whitegrid',
            'tableau-colorblind10'
        title: Graph title. Default = "Multiclass ROC curve"            
    Return: ROC Curve graph'''
    
    #creates three empty dictionaries based on true and false positive rate and threshold
    false_positive_rate = {}
    true_positive_rate = {}
    threshold = {}

    #creates a variable with the number of distinct values in the target variable
    n_classes = classes

    #creates an ROC curve based on target variable and prediction probabilities 
    for c in range(n_classes):
        false_positive_rate[c], true_positive_rate[c], threshold[c] = roc_curve(y_true = y, 
                                                                                y_score = pred_proba[:,c],
                                                                                pos_label = c)    
    
    #creates ROC curve with random values
    random_probs = [0 for rand in range(len(y))]
    p_fpr, p_tpr, _ = roc_curve(y_true = y, 
                                y_score = random_probs,
                                pos_label = 1)
        
    
  
    #sets graph size
    plt.figure(figsize = [12,7])
    #sets graph stle
    plt.style.use(style)
    #plots ROC curves 
    plt.plot(false_positive_rate[0], 
             true_positive_rate[0],
             linestyle = "--",
             color = "red",
             label = "Class 0 vs Rest")
    plt.plot(false_positive_rate[1],
             true_positive_rate[1],
             linestyle = "--",
             color = "green",
             label = "Class 1 vs Rest")
    plt.plot(false_positive_rate[2],
             true_positive_rate[2],
             linestyle = "--",
             color = "blue",
             label = "Class 2 vs Rest")
    #sets random ROC curve (diagonal line)
    plt.plot(p_fpr, 
             p_tpr)
    #sets graph title
    plt.title(f"{title} ROC Curve")
    #sets graphs labels
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive rate")
    #sets x limit
    plt.xlim(-0.005, 1)
    #sets y limit
    plt.ylim(0,1.05)
    #sets legend
    plt.legend(loc = "best")
    #returns plot
    return plt.show()