"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    return convert_coordinate(get_coordinate(azara_record)) in rui_record


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'  


def clean_up(combined_record_group):
    kept_records = [str((record[0],) + record[2:5]) for record in combined_record_group]
    return ''.join(rec + '\n' for rec in kept_records)
    #return '\n'.join(kept_records) + '\n'
