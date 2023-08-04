def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    row=data.split('\n')
    first_row=row[0].split(',')
    return len(first_row)

# Read the csv file
f=open('data.csv')
print(find_number_of_columns(f.read()))
