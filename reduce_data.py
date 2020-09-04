#
# This script reduces the IMDb titles data set down to those
# which have 'US' as the region and a type of 'movie'
#


# Constants for retrieving specific fields from the data
TITLE_TCONST_INDEX = 0
TITLE_TYPE_INDEX = 1
REGION_INDEX = 3

# Dictionary to track which titles are both movies and from the US
# The tconst for the respective title is used as the key and the value
# is another dictionary with the following structure:
# {
#     "isMovie": boolean,
#     "fromUS": boolean
# }
# If both values are true, the title is added to the reduced data set
titles_dictionary = {}


# This loop is a first pass over the title basics data to determine which
# titles are movies.
# We first open the file, specifying utf-8 encoding to ensure no read errors.
title_basics = open("./data/title.basics.tsv", "r", encoding="utf-8")
for title_basics_record in title_basics:
    fields = title_basics_record.split("\t") # Split fields on the tab char

    # Get the tconst field and create dict entry for it.
    titles_dictionary[fields[TITLE_TCONST_INDEX]] = {
        # Check if title is a movie and set isMovie bool accordingly.
        # Init fromUS bool to false as default value.
        "isMovie": True if fields[TITLE_TYPE_INDEX] == "movie" else False,
        "fromUS": False
    }


# Next we iterate through the title akas to check which titles have a US region
# Also open a file to write our reduced title akas data to
title_akas = open("./data/title.akas.tsv", "r", encoding="utf-8")
title_akas_reduced = open("./data/title.akas.reduced.tsv", "w",
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
            "fromUS":False
        }

    # Check if region is true, if so set bool value in dict,
    # then check if title is a movie and write to reduced data if it is.
    if fields[REGION_INDEX] == "US":
        title_record["fromUS"] = True

        if title_record["isMovie"]:
            title_akas_reduced.write(title_akas_record)
title_akas.close()
title_akas_reduced.close()


# Now we go back to the title basics data to write its reduced data set,
# first moving the cursor back to the start of the file.
title_basics.seek(0)
title_basics_reduced = open("./data/title.basics.reduced.tsv", "w", encoding="utf-8")
title_basics_reduced.write(title_basics.readline())
for title_basics_record in title_basics:
    fields = title_basics_record.split("\t")
    title_record = titles_dictionary[fields[TITLE_TCONST_INDEX]]

    # Add to data if it is from US and a movie
    if title_record["fromUS"] and title_record["isMovie"]:
        title_basics_reduced.write(title_basics_record)
title_basics.close()
title_basics_reduced.close()


# Now we repeat the same steps as above for our title ratings file
title_ratings = open("./data/title.ratings.tsv", "r", encoding="utf-8")
title_ratings_reduced = open("./data/title.ratings.reduced.tsv", "w", encoding="utf-8")
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
