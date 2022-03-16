# Labelbox Label Manipulation

When labeling image data for object detection using the online labeling tool LabelBox it is common practice to have multiple classes. Researcher may want to replace, change, or merge these labels together for model training. This repo will contain scripts the support the manipulation of Labelbox labels.

# label_replacement.py

This script takes in a LabelBox JSON, and two lists. The first list is the label/labels you would like to change, and the second is the labels you would like to chang them to.

## Examples

python3 label_replacement.py -i {path to labelbox json} -ol plant rock -rl corn gcp

The above command would change everything labeled plant to corn and everything labeled rock to gcp.

python3 label_replacement.py -i {path to labelbox json} -ol plant rock -rl corn

The above command would change both the objects labeled plant and rock to corn

# labeler_selection.py

This script takes in a LabelBox JSON, and two lists. The first list is a list of labeler's emails that you want to keep their work. The second list is a list of labeler's emails that you do not want to keep their work. The script preforms as expected when only given one of the two lists.

## Examples

python3 labeler_selection.py -i /home/travis/repos/labelbox_label_manipulation/export-2022-03-14T15_05_28.986Z.json -rl labeler1@email.com -of name_switch.json

Removing all labels created by: ['labler1@email.com']

Finished, output named: name_switch.json

Removed 1130 labels, leaving 869 total.




python3 labeler_selection.py -i /home/travis/repos/labelbox_label_manipulation/export-2022-03-14T15_05_28.986Z.json -kl labeler1@email.com -of name_switch.json

Removing all labels not created by: ['labler1@email.com']

Finished, output named: name_switch.json

Removed 896 labels, leaving 1130 total.




python3 labeler_selection.py -i /home/travis/repos/labelbox_label_manipulation/export-2022-03-14T15_05_28.986Z.json -kl labeler1@email.com labeler2@email.com -of name_switch.json

Removing all labels not created by: ['labler1@email.com', 'labeler2@email.com']

Finished, output named: name_switch.json

Removed 700 labels, leaving 230 total.

