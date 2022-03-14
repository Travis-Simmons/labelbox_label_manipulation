#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2022-02-10
Purpose: RGB indices extraction
"""

import argparse
import os
import sys
import json


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    parser.add_argument('-i',
                        '--input_json',
                        help='JSON exported from labelbox labels',
                        metavar='str',
                        type=str,
                        required=True)

    parser.add_argument('-ol',
                        '--original_labels',
                        help='A list of labels you want to replace',
                        nargs='+',
                        required=True)

    parser.add_argument('-rl',
                        '--replacement_labels',
                        help='replacement labels',
                        nargs='+',
                        required=True)

    parser.add_argument('-of',
                        '--output_filename',
                        help='Output file name.',
                        metavar='str',
                        type=str,
                        default='label_replaced.json')

    return parser.parse_args()




# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    input_filename = args.input_filename
    ol_list = args.original_labels
    rl_list = args.replacement_labels
    output_filename = args.output_filename

    # create replacement dict
    r_dict = {}

    # if only one replacement label was provided,
    # replace all labels with it
    if len(rl_list) == 0:
        replacement_label = rl_list[0]

        for i in ol_list:
            r_dict[i] = replacement_label

    # if more than one label is given, then do a 1:1 replacement
    else:
        for index, row in enumerate(ol_list):
            r_dict[row] = rl_list[index]



    with open(input_filename) as f:
        data = json.load(f)

    for index, i in enumerate(data):

        # print(data[index].keys())
        labels = data[index]['Label']['objects']

        for lab_num, i in enumerate(labels):

            # lookup old label, if it is not one you want to replace, then skip it
            old_label = data[index]['Label']['objects'][lab_num]['title']
            try:
                new_label = r_dict[old_label]

                # repalce the label
                data[index]['Label']['objects'][lab_num]['title'] = new_label
                data[index]['Label']['objects'][lab_num]['value'] = new_label
            except:
                pass



    with open(output_filename, 'w') as f:
        json.dump(data, f)


# --------------------------------------------------
if __name__ == '__main__':
    main()