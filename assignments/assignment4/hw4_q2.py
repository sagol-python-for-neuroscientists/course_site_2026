import pandas as pd
import pathlib


# helper functions
def organizing_file(fname: pathlib.Path) -> pd.DataFrame:
    """Returns the data from the txt file as a data frame ready to work on

    Parameters
    ----------
    fname : pathlib.Path
        path to the file that contains the data

    Returns
    -------
    pd.DataFrame
        the same data organized
        text file is read as a df
        year column is the index column named "year"
        number of animals converted to float
    """
    df = pd.read_csv("populations.txt", sep="\t", index_col=0)

    # set the name of index column to "year"
    df.index.name = "year"

    # Convert number-like strings to floats (e.g., "30e3" -> 30000.0)
    df = df.apply(pd.to_numeric)

    return df


# i
def largest_species(fname: pathlib.Path) -> pd.Series:
    """Returns the name of the most widespread species per year.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    largest_by_year : pd.Series
        Name of most common species per year
    """
    # organize the data
    df = organizing_file(fname)

    # Find the animal column with the max value per row (axis 1)
    max_animal = df.idxmax(axis=1)
    return max_animal


# ii
def lynxes_when_hares(fname: pathlib.Path) -> pd.Series:
    """Returns the number of lynxes when hares > foxes.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    lynxes : pd.Series
        Number of lynxes when hares > foxes
    """
    # organize the data
    df = organizing_file(fname)

    # return a series of the lynxes' values when there are more hares than foxes
    # passes a Boolean series directly inside the indexing bracket of our target column. 
    # Pandas filters out the matching rows automatically while maintaining the structural chronological index.
    return df["lynx"][df["hare"] > df["fox"]]


# iii
def mean_animals(fname: pathlib.Path) -> pd.DataFrame:
    """Adds a column with the normalized mean number of animals in each year.

    This means that in the year with most animals, this column will have the value of 1,
    and in the rest of the years the value will be between [0, 1).

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    data : pd.DataFrame
        Original dataset with the new "mean_animals" column.
    """

    # organize the data
    df = organizing_file(fname)

    # sum how many animals per year
    sum_in_year = df[["hare", "lynx", "fox"]].sum(axis=1)

    # calculate normalized value
    df["mean_animals"] = sum_in_year / sum_in_year.max()

    return df
