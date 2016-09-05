# NOTE: This is a modification of https://gist.github.com/jrivero/1085501

import os
import csv

# Note that this path assumes the path from the location that this is being executed from.
def setup_split(path, name_convention):

    if os.path.isfile(path + 'split.txt'):
        return
    
    output_path, path = prep_paths(path, name_convention)
    name_convention = name_convention[:-4]
    split(open(path, 'r'), name_convention, output_path, 100000000)

def prep_paths(path, name_convention):
    output_path = path
    path = path + name_convention
    return output_path, path

def prep_io(filehandler, name_convention, output_path, current_piece):
    reader = csv.reader(filehandler, delimiter=',')
    
    output_name_template = name_convention + '_%s.csv'

    current_out_path = os.path.join(
         output_path,
         output_name_template  % current_piece
    )
    
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=',')

    return reader, current_out_writer, output_name_template

def set_limits(headers, row_col_density):
    row_limit = row_col_density / len(headers)
    current_limit = row_limit
    return row_limit, current_limit

def split(filehandler, name_convention, output_path, row_col_density=100000000):

    current_piece = 1
    reader, current_out_writer, output_name_template = prep_io(filehandler, name_convention, output_path, current_piece)
    headers = reader.next()
    row_limit, current_limit = set_limits(headers, row_col_density)
    
    current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
               output_path,
               output_name_template  % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=',')
            current_out_writer.writerow(headers)
        current_out_writer.writerow(row)
