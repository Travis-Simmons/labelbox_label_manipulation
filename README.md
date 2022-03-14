# Labelbox Label Manipulation

When labeling image data for object detection using the online labeling tool LabelBox it is common practice to have multiple classes. Researcher may want to replace, change, or merge these labels together for model training. This repo will contain scripts the support the manipulation of Labelbox labels.

# replace_labels.py

This script takes in a LabelBox JSON, and two lists. The first list is the label/labels you would like to change, and the second is the labels you would like to chang them to.

## Example

python3 replace_labels.py -i {path to labelbox json} -ol plant rock -rl corn gcp

The above command would change everything labeled plant to corn and everything labeled rock to gcp.

python3 replace_labels.py -i {path to labelbox json} -ol plant rock -rl corn

The above command would change both the objects labeled plant and rock to corn
