"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    return tuple(azara_record[1]) in rui_record


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'  


#def clean_up(combined_record_group):
    #kept_records = []
    #for record in combined_record_group:
        #keep = (record[0], record[2], record[3], record[4])
        #kept_records.append(str(keep))
    #return '\n'.join(kept_records) + '\n'

# I can change the 'keep' line into:
#keep = (record[0],) + record[2:5]

#so, yes, we can do List comprehension here... transform all the kept_records into strings and then iterate them for every record.


def clean_up(combined_record_group):
    kept_records = [str((record[0],) + record[2:5]) for record in combined_record_group]
    return '\n'.join(kept_records) + '\n'
