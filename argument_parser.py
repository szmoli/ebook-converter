import argparse

argument_parser = argparse.ArgumentParser('ebook-converter')

argument_parser.add_argument('-e', '--epub', action='store_true', help='set the output file type to .epub')
argument_parser.add_argument('-m', '--mobi', action='store_true', help='set the output file type to .mobi')
argument_parser.add_argument('-o', '--output_path', type=str, help='specify an output path')
argument_parser.add_argument('-i', '--input_path', type=str, help='specify an input path', required=True)