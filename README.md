# Trend of forest areas in Spain and the Balearic Islands

!["forest"](https://www.barcelo.com/guia-turismo/wp-content/uploads/2019/04/sierra-guadarrama-1.jpg)

## Introduction

The study of the condition of forests is very important to know the quality of the services that these ecosystems provide to humans.

In this case, the modeling of the main drivers of change of this condition, can help us to predict what will be the quality of these ecosystems as a function of climatic, topographic and anthropogenic variables.

Besides being useful to know the condition of these forests in future climate scenarios in which we can predict the increase or decrease of this quality as a function of possible changes in temperature and precipitation regimes.

All this is very useful for public administration, politicians, private entities and other stakeholders. Because it serves to evaluate the natural capital, prioritize restoration areas and ultimately to know the areas where vegetation is adapting better to climate change, preserving most of the ecosystem services it offers to society.

Ecosystem services are, for example, providing wood or food, filtering air or water, sequestering carbon or generating tourism or any other recreational activity.


  
## Objective
  
Generate a Machine Learning model capable of predicting the growth and development trend of forest areas in Spain and the Balearic Islands. 

## Variables

### Predictors
    
    pointid: Input ID

    'EU_road': Euclidean distance of the input to roads.  One unit represents 250 m.

    'EU_sett': Euclidean distance of the input to poblations.  One unit represents 250 m.

    'EU_fabric': Euclidean distance of the input industrial areas.  One unit represents 250 m.

    'TFCCTOT': Fraction of total covered capacity. In percentage.

    'TFCCARB': Fraction of tree-covered capacity. In percentage.

    'FCC_POND': Fraction of total covered capacity. Weighting.

    'NOM_FORARB': Type of tree formation.

    'REGBIO': Climate.

    'mdt': Digital elevation model / altitude.

    'aspect': Orientation

    'cci_lc': Soil cover

    'population': Population density of people.

    'prec_acu_m': Average annual accumulated precipitation.

    'sequia_mea': Evotranspiration / Aridity index

    'slope': Slope / Percentage.

    'soc': Soil carbon content.

    'soil_ph': Soil water acidity

    'srad_summe': Solar radiation reaching the Earth on summer.

    'srad_winte': Solar radiation reaching the Earth on winter.

    'temp_mean': Average annual temperature.

    'trend_sequ': Aridity index trend.

    'trend_temp': Temperature trend.

    'wind': Wind Speed.

    'lat': Lattitude.

    'long': Longitude.

    'protected': Natural Protected Area.


### Response
    'ndvi_trend': Normalized Difference Vegetation Index trend.


## Process

The process consists of four steps:

1. Cleaning:
In this process, the DataSet is checked and the following cleaning methods are performed:
    1. Null values : Using techniques such as zero fill, and `KNNIMputer`.
    2. Using techniques such as `SimpleImputer`.
    3. Category Encoging, like `TargetEncoder`.
    4. Drop repeat data.

2. Supervised Learning:
Fit 4 models for each distint climate:
    - Bagging
        1. `RandomForestClassifier`.
        2. `ExtraTreesClasifier`.
    - Boosting
        3. `LightGradientBoostingMachine`.
        4. `Cat>boost`

Select best model according to accuracy score.

Tune select model

3. Analysis
Features Importances
Partial Dependence Plots
Multilabel ROC Curve

## Results

The selected model, and therefore the one with the best accuracy scores, is the `ExtratreesClasifier`.


![Accuracy_Scores](output\select_model.jpg)


## Libraries

Pandas

Matplotlib

Seaborn

Sklearn

Collection

Ibmlearn
