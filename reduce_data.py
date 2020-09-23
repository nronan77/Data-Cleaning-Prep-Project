#
# This script reduces the IMDb titles data set down to those
# which have 'US' as the region and a type of 'movie'
#


# Constants for retrieving specific fields from the data
TITLE_TCONST_INDEX = 0
TITLE_TYPE_INDEX = 1
REGION_INDEX = 3


# This function is a first pass over the title basics data to read the data in
# and determine which titles are movies
def read_title_basics_data(titles_dictionary):
    # Open files with utf-8 encoding to ensure no read/write errors
    title_basics = open("../data/title.basics.tsv", "r", encoding="utf-8")
    for title_basics_record in title_basics:
        fields = title_basics_record.split("\t") # Split fields on the tab char

        # Get the tconst field and create dict entry for it.
        titles_dictionary[fields[TITLE_TCONST_INDEX]] = {
            # Check if title is a movie and set isMovie bool accordingly.
            # Init fromUS bool to false as default value.
            "isMovie": True if fields[TITLE_TYPE_INDEX] == "movie" else False,
            "fromUS": False
        }
    title_basics.close()

# This function iterates through the title akas data to check which titles
# have a US region and write valid data to the reduced data file
def read_title_akas_and_reduce(titles_dictionary):
    title_akas = open("../data/title.akas.tsv", "r", encoding="utf-8")
    title_akas_reduced = open("../data/title.akas.reduced.tsv", "w",
                              encoding="utf-8")
    # Copy fields over to reduced data file
    title_akas_reduced.write(title_akas.readline())
    for title_akas_record in title_akas:
        fields = title_akas_record.split("\t")

        # Try block in case tconst does not exist in our titles dictionary
        try:
            title_record = titles_dictionary[fields[TITLE_TCONST_INDEX]]
        except KeyError:
            # If it doesn't exist, set
            title_record = {
                "isMovie": False,
                "fromUS": False
            }

        # Check if region is true, if so set bool value in dict,
        # then check if title is a movie and write to reduced data if it is.
        if fields[REGION_INDEX] == "US":
            title_record["fromUS"] = True

            if title_record["isMovie"]:
                title_akas_reduced.write(title_akas_record)
    title_akas.close()
    title_akas_reduced.close()


# This function returns to the title_basics data file once we know the
# title's region to write valid data to the reduced data set
def reduce_title_basics(titles_dictionary):
    title_basics = open("../data/title.basics.tsv", "r", encoding="utf-8")
    title_basics_reduced = open("../data/title.basics.reduced.tsv", "w",
                                encoding="utf-8")
    title_basics_reduced.write(title_basics.readline())
    for title_basics_record in title_basics:
        fields = title_basics_record.split("\t")
        title_record = titles_dictionary[fields[TITLE_TCONST_INDEX]]

        # Add to data if it is from US and a movie
        if title_record["fromUS"] and title_record["isMovie"]:
            title_basics_reduced.write(title_basics_record)
    title_basics.close()
    title_basics_reduced.close()


# Repeats steps from previous functions to read and reduce
# title ratings data
def read_title_ratings_and_reduce(titles_dictionary):
    title_ratings = open("../data/title.ratings.tsv", "r", encoding="utf-8")
    title_ratings_reduced = open("../data/title.ratings.reduced.tsv", "w",
                                 encoding="utf-8")
    title_ratings_reduced.write(title_ratings.readline())
    for title_ratings_record in title_ratings:
        fields = title_ratings_record.split("\t")

        try:
            title_record = titles_dictionary[fields[TITLE_TCONST_INDEX]]
        except KeyError:
            title_record = {
                "fromUS": False,
                "isMovie": False
            }

        if title_record["fromUS"] and title_record["isMovie"]:
            title_ratings_reduced.write(title_ratings_record)
    title_ratings.close()
    title_ratings_reduced.close()


if __name__ == "__main__":
    # Dictionary to track which titles are both movies and from the US
    # The tconst for the respective title is used as the key and the value
    # is another dictionary with the following structure:
    # {
    #     "isMovie": boolean,
    #     "fromUS": boolean
    # }
    # If both values are true, the title is added to the reduced data set
    titles_dictionary = {}

    # Then we move on to reducing data to titles with US as the region
    # and movie as the titleType
    read_title_basics_data(titles_dictionary)
    read_title_akas_and_reduce(titles_dictionary)
    reduce_title_basics(titles_dictionary)
    read_title_ratings_and_reduce(titles_dictionary)
