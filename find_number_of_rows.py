def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    column=data.split('\n')
    first_column=column[0].split(',')
    return len(first_column)

# Read the csv file
f=open('data.csv')
print(find_number_of_rows(f.read()))
