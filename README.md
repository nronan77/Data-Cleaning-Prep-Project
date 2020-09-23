# Data Cleaning & Preparation Project

## Reducing the data
1. Create a folder named 'data' under the root directory
2. Rename the data sets to title.basics.tsv, title.ratings.tsv, and title.akas.tsv respectively
then move them into the newly created data folder
3. Finally, run the reduce_data.py script to reduce the data sets to titles that are movies with US as the region.
This should take some time

## Combining the Data set
1. Run the reduce_data.py script to create the reduced data set. Files will be written to the data folder.
2. Run the combine_data.py script once the data is reduced. The combined data will be written to combined.data.tsv 
in the data folder. This should take some time

## Getting info for the data dictionary
1. After combining and reducing the data, run the create_data_dictionary.py script. This will take some time
2. Data dictionary info will be written to data.dict.tsv in the data folder