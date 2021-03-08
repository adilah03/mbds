### Question 4 ###

# function to load text file as array
from numpy import loadtxt
# function to label features in an array
from scipy.ndimage.measurements import label

# label the input grid, i.e., find number of connected components
# scipy.ndimage.measurements.label() (https://github.com/scipy/scipy/blob/v0.14.0/scipy/ndimage/measurements.py#L46)
# works by iterating over the rows of the grid and labelling connected components in that row
# conflicts in the labels are resolved by taking the smaller label, i.e., number in the previous row
input = loadtxt('./input_question_4', dtype='i', delimiter='\t')
labeled_image, n = label(input)
for i in range(len(labeled_image)):
    print(*labeled_image[i], sep='\t')
