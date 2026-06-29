import zipfile
import pandas as pd
import pathlib


# helper functions
def read_csv_in_zip(fname: pathlib.Path) -> pd.DataFrame:
    """reads the csv file that is within a zip file, and return it as a df ready to analyze

    Parameters
    ----------
    fname : pathlib.Path
        path to the zip file

    Returns
    -------
    pd.DataFrame
        the df that is the csv file within the zip file
    """
    # Reading Directly from a ZIP using the python built-in zipfile module
    with zipfile.ZipFile(fname, "r") as z:
        # List files in the ZIP
        csv_name = z.namelist()[0]

        with z.open(csv_name) as f:
            df = pd.read_csv(f, index_col=0)

    return df


# i
def common_complaint(fname: pathlib.Path) -> tuple:
    """Finds and returns the most common complaint as (complaint_name, num).

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the NYC data.

    Returns
    -------
    common_complaint : tuple
        (Complaint name, number of occasions)
    """
    df = read_csv_in_zip(fname)

    # Count the number of occurrences of each complaint type 
    # .value_counts() ranks items by frequency
    complaint_counts = df["Complaint Type"].value_counts()

    # Extract the most common complaint type and its count 
    complaint_name = complaint_counts.index[0] # peak key identity using .index[0]
    num = int(complaint_counts.iloc[0]) # grabs the matching absolute scalar volume using .iloc[0]

    # Return as a tuple
    return (complaint_name, num)


# ii
def parking_borough(fname: pathlib.Path) -> str:
    """Finds and returns the name of the NYC borough that has the
    most complaints of type 'Illegal Parking'.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the NYC data.

    Returns
    -------
    borough_name : str
        Name of the relevant NYC borough.
    """
    df = read_csv_in_zip(fname)

    # count how many times each complaint type appeared per borough
    # .loc isolates: 
    # a specific sub-slice of the master array (rows where the complaint is strictly "Illegal Parking")
    # their corresponding "Borough" tags
    # groups them by frequency

    borough_counts = df.loc[
        df["Complaint Type"] == "Illegal Parking", "Borough"
    ].value_counts()

    # return the borough with the max value of complaints
    # idxmax pulls the geographic location string linked with the highest violation counts
    borough_name = borough_counts.idxmax()
    return borough_name
