import argument_parser
import PyPDF2

arguments = argument_parser.argument_parser.parse_args()

pdf_file = open(arguments.input_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for i, page in enumerate(pdf_reader.pages):
    print(f'page {i}')
    print(page.extract_text())

if (arguments.epub):
    print('epub branch')

if (arguments.mobi):
    print('mobi branch')

if (arguments.output_path):
    print(f'output_path = {arguments.output_path}')