import pandas as pd

# Load the data from the CSV file
archivo = pd.read_csv('arteDeLaAnalitica\avocado_full.csv')

# Filter the data for the regions New York, California and Charlotte
new_york = archivo[archivo['region'] == 'NewYork']
california = archivo[archivo['region'] == 'California']
charlotte = archivo[archivo['region'] == 'Charlotte']

# Define a list of tuples with the results of the analysis
results = []

# Total production of avocados in the regions
total_new_york = new_york['Total Volume'].sum()
total_california = california['Total Volume'].sum()
total_charlotte = charlotte['Total Volume'].sum()

# Average production of avocados in the regions
average_new_york = new_york['Total Volume'].mean()
average_california = california['Total Volume'].mean()
average_charlotte = charlotte['Total Volume'].mean()

# Standard deviation of the production of avocados in the regions
std_new_york = new_york['Total Volume'].std()
std_california = california['Total Volume'].std()
std_charlotte = charlotte['Total Volume'].std()

# Percentage of small avocado bags in the regions
small_bags_new_york = new_york['Small Bags'].sum() / new_york['Total Bags'].sum() * 100
small_bags_california = california['Small Bags'].sum() / california['Total Bags'].sum() * 100
small_bags_charlotte = charlotte['Small Bags'].sum() / charlotte['Total Bags'].sum() * 100

# Percentage of large avocado bags in the regions
large_bags_new_york = new_york['Large Bags'].sum() / new_york['Total Bags'].sum() * 100
large_bags_california = california['Large Bags'].sum() / california['Total Bags'].sum() * 100
large_bags_charlotte = charlotte['Large Bags'].sum() / charlotte['Total Bags'].sum() * 100

# Percentage of extra large avocado bags in the regions
extra_large_bags_new_york = new_york['XLarge Bags'].sum() / new_york['Total Bags'].sum() * 100
extra_large_bags_california = california['XLarge Bags'].sum() / california['Total Bags'].sum() * 100
extra_large_bags_charlotte = charlotte['XLarge Bags'].sum() / charlotte['Total Bags'].sum() * 100

# regions for printing
regions = ['New York', 'California', 'Charlotte']
# Tags for printing
tags = ['Total production', 'Average production', 'Standard deviation',
        'Percentage of small bags', 'Percentage of large bags', 'Percentage of extra large bags']
# Fill the list of tuples with the results
results.append((total_new_york, average_new_york, std_new_york, small_bags_new_york, large_bags_new_york, extra_large_bags_new_york))
results.append((total_california, average_california, std_california, small_bags_california, large_bags_california, extra_large_bags_california))
results.append((total_charlotte, average_charlotte, std_charlotte, small_bags_charlotte, large_bags_charlotte, extra_large_bags_charlotte))

# Iterate over the results and print them
for i in range (len(regions)):
    print('Results for the region of', regions[i])
    for j in range(len(tags)):
        print(tags[j], ':', results[i][j])
    print()