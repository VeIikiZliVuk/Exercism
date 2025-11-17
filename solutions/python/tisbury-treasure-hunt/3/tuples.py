"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    , param record,  tuple - with a (treasure, coordinate) pair.
    , return,  str - the extracted map coordinate.
    """
    #record = [
#('Amethyst Octopus', '1F'), 
#('Angry Monkey Figurine', '5B'), 
#('Antique Glass Fishnet Float', '3D'), 
#('Brass Spyglass', '4B'), 
#('Carved Wooden Elephant', '8C'), 
#('Crystal Crab', '6A'), 
#('Glass Starfish', '6D'), 
#('Model Ship in Large Bottle', '8A'), 
#('Pirate Flag', '7F'), 
#('Robot Parrot', '1C'), 
#('Scrimshawed Whale Tooth', '2A'), 
#('Silver Seahorse', '4E'), 
#('Vintage Pirate Hat', '7E')
#]
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    , param coordinate,  str - a string map coordinate
    , return,  tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    , param azara_record,  tuple - a (treasure, coordinate) pair.
    , param rui_record,  tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    , return,  bool - do the coordinates match?
    """
    
    if tuple(azara_record[1]) in rui_record:
        return True
    return False

    #return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    , param azara_record,  tuple - a (treasure, coordinate) pair.
    , param rui_record,  tuple - a (location, coordinate, quadrant) trio.
    , return,  tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'
        


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    , param combined_record_group,  tuple - everything from both participants.
    , return,  str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    kept_records = []
    for record in combined_record_group:
        keep = (record[0], record[2], record[3], record[4])
        kept_records.append(str(keep))
    return '\n'.join(kept_records) + '\n'
