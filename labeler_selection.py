#!/usr/bin/env python3
"""
Author : Travis Simmons
Date   : 2022-03-16
Purpose: Select only labels from a certain labeler
Example Deployment: python3 labeler_selection.py -i labelbox.json -rl labeler_1@email.com -kl labeler_2@email.com -of name_switch.json
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

    parser.add_argument('-kl',
                        '--keep_labeler',
                        help='A list of labelers that you want to keep',
                        nargs='+',
                        default=[])

    parser.add_argument('-rl',
                        '--remove_labeler',
                        help='A list of labelers that you want to remove',
                        nargs='+',
                        default=[])

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

    input_filename = args.input_json
    kl_list = args.keep_labeler
    rl_list = args.remove_labeler
    output_filename = args.output_filename

    # create replacement dict
    new_dict = {}

    # we want it so if you only give somethig in the kl it only takes that
    only_keep = False
    only_remove = False

    if len(rl_list) == 0:
        only_keep = True

        print(f'Removing all labels not creted by: {kl_list}')

    if len(kl_list) == 0:
        only_remove = True

        print(f'Removing all labels created by: {rl_list}')

    if (only_remove==False) and (only_keep==False):
        print(f'Removing all labels not created by: {kl_list}')


    with open(input_filename) as f:
        data = json.load(f)

    # probably a more elegant way to do this
    for index, i in enumerate(data):
        try:
            labeler = data[index]['Created By']

            if only_keep == True:
                if not labeler in kl_list:
                    pass
                else:
                    new_dict[index] = data[index]

            elif only_remove == True:
                # pritn('rm only')
                if labeler in rl_list:
                    pass
                else:
                    # print('adding')
                    new_dict[index] = data[index]

            else:
                if not labeler in kl_list:
                    pass
                else:
                    new_dict[index] = data[index]


        except:
            break

    with open(output_filename, 'w') as f:
        json.dump(new_dict, f)

    print(f'Finished, output named: {output_filename}')
    print(f'Removed {len(data) - len(new_dict)} labels, leaving {len(new_dict)} total.')

# --------------------------------------------------
if __name__ == '__main__':
    main()