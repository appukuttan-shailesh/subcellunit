'''
SBtab Tools
===========

These functions facilitate the use of SBtab.
They can be used to create SBtab objects, by merging strings or read files, respectively.
'''

import tablib
import copy
import SBtab
import os.path
import tablibIO

def oneOrMany(spreadsheet_file):
    '''
    Checks for multiple tables in a file and cuts them into separate tablib object.

    Parameters
    ----------
    spreadsheet_file : tablib object
        Tablib object of the whole SBtab table.
    '''
    sbtabs = []

    # Copy file, one for iteration, one for cutting
    sbtab_document = copy.deepcopy(spreadsheet_file)

    # Create new tablib object
    sbtab = tablib.Dataset()

    # Cutting sbtab_document, write tablib objects in list
    if len(spreadsheet_file) != 0:  # If file not empty
        for row in spreadsheet_file:
            if len(sbtab) == 0:  # If first line, append line w/o checking
                sbtab.rpush(sbtab_document.lpop())
            else:
                for i, entry in enumerate(row):
                    # If header row (!!), write to new tablib object and store the last one
                    if entry.startswith('!!'):
                        sbtabs.append(sbtab)
                        sbtab = tablib.Dataset()
                        sbtab.rpush(sbtab_document.lpop())
                        break
                    # If not header row, append line to tablib object
                    if len(row) == i + 1:
                        sbtab.rpush(sbtab_document.lpop())
        sbtabs.append(sbtab)

    # Return list of tablib objects
    return sbtabs

def openSBtab(filepath):
    '''
    Opens SBtab from file.

    Parameters
    ----------
    filepath : str
        Path of the spreadsheet file.
    '''
    if not os.path.isfile(filepath):
        return None

    dataset = tablibIO.importSet(filepath)
    sbtab = SBtab.SBtabTable(dataset, filepath)

    return sbtab

def openSBtab_asBook(filepath):
    '''
    Opens SBtab from file.

    Parameters
    ----------
    filepath : str
        Path of the spreadsheet file.
    '''
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'rb') as myfile:
        databook = tablibIO.importSetNew(myfile.read(), filepath)
    sbtabs_dict = {}
    for dataset in databook.sheets():
        sbtabs_dict[dataset.title] = SBtab.SBtabTable(dataset, filepath)
    return sbtabs_dict


def createDataset(header_row, columns, value_rows, filename):
    '''
    Creates an SBtab object by merging strings or list of strings.
    Takes a header row, main column row, and the value rows as lists of strings and returns an SBtab object.

    Parameters
    ----------
    header_row : str
        String of the header row.
    columns: list
        List of strings, names of the columns.
    value_rows : list
        List of lists containing the different rows of the table.
    '''
    # Initialize variables
    sbtab_temp = []
    sbtab_dataset = tablib.Dataset()
    header = header_row.split(' ')

    # Delete spaces in header, main column and data rows
    header = [x.strip(' ') for x in header]
    columns = [x.strip(' ') for x in columns]
    for row in value_rows:
        try:
            for entry in row:
                entry = entry.strip(' ')
        except:
            continue

    # Add header, main column and data rows to temporary list object
    sbtab_temp.append(header)
    sbtab_temp.append(columns)
    for row in value_rows:
        sbtab_temp.append(row)

    # Delete all empty entries at the end of the rows
    for row in sbtab_temp:
        if len(row) > 1:
            while not row[-1]:
                del row[-1]

    # Make all rows the same length
    longest = max([len(x) for x in sbtab_temp])
    for row in sbtab_temp:
        if len(row) < longest:
            for i in range(longest - len(row)):
                row.append('')
            sbtab_dataset.append(row)
        else:
            sbtab_dataset.append(row)

    # Create SBtab object from tablib dataset
    sbtab = SBtab.SBtabTable(sbtab_dataset, filename)
    return sbtab
