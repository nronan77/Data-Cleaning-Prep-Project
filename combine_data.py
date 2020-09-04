#
# This script reads in the reduced title data sets and
# also the name basics data set, then combines the data into one
# file called combined.data.tsv
#

# Open our reduced title basics data set and iterate through to
# add values to the dictionary
def read_title_basics_data(movies_dictionary):
    title_basics = open("./data/title.basics.reduced.tsv", "r",
                        encoding="utf-8")
    title_basics.readline() # Skip first line since it is just the fields
    print("Reading title basics data")
    for title_basics_record in title_basics:
        tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, \
        endYear, runtimeMinutes, genres = title_basics_record.split("\t")
        genres = genres.replace("\n", "") # Remove newline char from last field

        # Create new dictionary entry with title basics fields
        movies_dictionary[tconst] = {
            "titleType": titleType,
            "primaryTitle": primaryTitle,
            "originalTitle": originalTitle,
            "isAdult": isAdult,
            "startYear": startYear,
            "endYear": endYear,
            "runTimeMinutes": runtimeMinutes,
            "genres": genres
        }
    title_basics.close()


# Reads data from title ratings data and adds to movies dictionary
def read_title_ratings_data(movies_dictionary):
    title_ratings = open("./data/title.ratings.reduced.tsv", "r",
                         encoding="utf-8")
    title_ratings.readline()
    print("Reading title ratings data")
    for title_ratings_record in title_ratings:
        tconst, averageRating, numVotes = title_ratings_record.split("\t")
        numVotes = numVotes.replace("\n", "")

        # Don't need a new entry, so we look it up and add new fields
        movie_record = movies_dictionary[tconst]
        movie_record["averageRating"] = averageRating
        movie_record["numVotes"] = numVotes
    title_ratings.close()


# Reads data from title akas and adds to movies dictionary
def read_title_akas_data(movies_dictionary):
    # Repeat process for title akas data set
    title_akas = open("./data/title.akas.reduced.tsv", "r", encoding="utf-8")
    title_akas.readline()
    print("Readings title akas data")
    for title_akas_record in title_akas:
        titleId, ordering, title, region, language, titleTypes, attributes, \
        isOriginalTitle = title_akas_record.split("\t")
        isOriginalTitle = isOriginalTitle.replace("\n", "")

        # Don't need a new entry, so we look it up and add new fields
        movie_record = movies_dictionary[titleId]
        movie_record["ordering"] = ordering
        movie_record["localizedTitle"] = title
        movie_record["region"] = region
        movie_record["language"] = language
        movie_record["types"] = titleTypes
        movie_record["attributes"] = attributes
        movie_record["isOriginalTitle"] = isOriginalTitle
    title_akas.close()


# Reads data from names.basics.tsv and combines with data in our
# movies dictionary
def combine_data(movies_dictionary):
    name_basics = open("./data/name.basics.tsv", "r", encoding="utf-8")
    combined_data = open("./data/combined.data.tsv", "w", encoding="utf-8")
    # Write all unique fields to first line. The 'title' field is now known
    # as localTitle to better define it according to IMDb's definition
    # knownForTitle is refers to the tconst of the title
    combined_data.write(
        "nconst\tprimaryName\tbirthYear\tdeathYear\t"
        "primaryProfession\tknownForTitle\ttitleType\t"
        "primaryTitle\toriginalTitle\tlocalTitle\t"
        "isAdult\tstartYear\tendYear\truntimeMinutes\t"
        "genre\tordering\tregion\tlanguage\ttype\tattribute\t"
        "isOriginalTitle\taverageRating\tnumVotes\n"
    )
    name_basics.readline()
    print("Reading name basics data and combining with titles data.\n"
          "This will take some time.")
    for name_basics_record in name_basics:
        # First get all the data from the name basics record
        nconst, primaryName, birthYear, deathYear, primaryProfession, \
        knownForTitles = name_basics_record.split("\t")
        knownForTitles = knownForTitles.replace("\n", "").split(",")
        professions = primaryProfession.split(",") # Split ',' separated fields
                                                   # into arrays

        #Iterate through arrays to create entries for all combinations
        for profession in professions:
            for tconst in knownForTitles:
                # Try block in case the tconst referred to a non-movie
                # or missing data
                try:
                    movie_record = movies_dictionary[tconst]
                    titleType = movie_record["titleType"]
                    primaryTitle = movie_record["primaryTitle"]
                    originalTitle = movie_record["originalTitle"]
                    isAdult = movie_record["isAdult"]
                    startYear = movie_record["startYear"]
                    endYear = movie_record["endYear"]
                    runtimeMinutes = movie_record["runTimeMinutes"]
                    ordering = movie_record["ordering"]
                    localTitle = movie_record["localizedTitle"]
                    region = movie_record["region"]
                    language = movie_record["language"]
                    isOriginalTitle = movie_record["isOriginalTitle"]
                    averageRating = movie_record["averageRating"]
                    numVotes = movie_record["numVotes"]
                    genres = movie_record["genres"].split(",")
                    attributes = movie_record["attributes"].split(",")
                    titleTypes = movie_record["types"].split(",")
                # If we get a KeyError, set all title-specific values to '\N'
                except KeyError:
                    titleType = "\\N"
                    primaryTitle = "\\N"
                    originalTitle = "\\N"
                    isAdult = "\\N"
                    startYear = "\\N"
                    endYear = "\\N"
                    runtimeMinutes = "\\N"
                    ordering = "\\N"
                    localTitle = "\\N"
                    region = "\\N"
                    language = "\\N"
                    isOriginalTitle = "\\N"
                    averageRating = "\\N"
                    numVotes = "\\N"
                    genres = ["\\N"]
                    attributes = ["\\N"]
                    titleTypes = ["\\N"]

                # Iterate through title's arrays to create all possible entries
                for genre in genres:
                    for attribute in attributes:
                        for titleType in titleTypes:
                            # Format the string with all values and write to
                            # combined data set file
                            combined_data.write(
                                f"{nconst}\t{primaryName}\t"
                                f"{birthYear}\t{deathYear}\t{profession}\t"
                                f"{tconst}\t{titleType}\t{primaryTitle}\t"
                                f"{originalTitle}\t{localTitle}\t{isAdult}\t"
                                f"{startYear}\t{endYear}\t{runtimeMinutes}\t"
                                f"{genre}\t{ordering}\t{region}\t{language}\t"
                                f"{titleType}\t{attribute}\t{isOriginalTitle}\t"
                                f"{averageRating}\t{numVotes}\n"
                            )
    name_basics.close()
    combined_data.close()


if __name__ == "__main__":
    # Create a dictionary that uses the title's tconst as the key
    # and the value is another dictionary that contains all unique fields across
    # the titles.basics, titles.akas, and titles.ratings data sets
    movies_dictionary = {}

    # Read in data from each reduced data set and name.basics.tsv, then combine
    # into one tsv file
    read_title_basics_data(movies_dictionary)
    read_title_ratings_data(movies_dictionary)
    read_title_akas_data(movies_dictionary)
    combine_data(movies_dictionary)
