#encoding=utf8

import os
import sys
from arg_config import ArgConfig
from squad.evaluate_v1 import *

def do_eval(args):

    expected_version = "1.1"

    with open(args.evaluation_file) as dataset_file:
        dataset_json = json.load(dataset_file)
        if (dataset_json['version'] != expected_version):
            print('Evaluation expects v-' + expected_version +
                ', but got dataset with v-' + dataset_json['version'])
        dataset = dataset_json['data']

        with open(args.output_prediction_file) as prediction_file:
            predictions = json.load(prediction_file)

        print(json.dumps(evaluate(dataset, predictions)))

if __name__ == "__main__":
    args = ArgConfig()
    args = args.build_conf()

    do_eval(args)
