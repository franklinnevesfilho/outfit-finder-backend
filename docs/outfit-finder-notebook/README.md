# Outfit Finder Notebook
#### By: [Franklin Neves Filho](https://www.franklinnevesfilho.com/)

This notebook demonstrates how I used the [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset) to create a Machine learning model that suggests the users outfits.

## Dataset

It contains the following columns:
```
- id
- gender
- masterCategory
- subCategory
- articleType
- baseColour
- season
- year
- usage
```
After processing the data, removing uneccesary columns and renaming others, the dataset looks like this:
```
- gender
- category
- style
- color
- season
- usage
```

## About The Model
The model uses the users information (gender and closet) to suggest clothing items based on a specific occasion.

This is achieved by using the `KNeighborsClassifier` from the `sklearn` library, alongside the 'StandardScaler' to normalize the data.

The model is then trained using the `fit` method and evaluated using the `score` method.

The model is used by getting the probability that a clothing item has to a specific occasion using the `predict_proba` method.

And with this information my program is able to suggest clothing items that have a probability higher than 0.5.

## Results
The model achieved an accuracy of `0.82`.

### Conclusion

The model is able to suggest clothing items to users based on the occasion.

### Next Steps

The next step into creating a more functional outfit finder, would be to use the data collected by this model to suggest outfits based on the user's preferences.

This could be done using a Deep Learning approach learning the users preferences and making a suggestion based on environmental factors as well.


# License
```
 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2024 Franklin Neves Filho 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)
