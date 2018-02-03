import argparse

from source2ir import source2ir

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with kotlin source codes')
parser.add_argument('--output_folder', '-o', nargs=1, type=str, help='output folder with IR as JSON')

args = parser.parse_args()
input_folder = args.input_folder[0]
output_folder = args.output_folder[0]

source2ir(input_folder, output_folder)
