#
# This script loads the combined data in and determines things like
# the number of unique values, total values, and range for numeric values,
# for each attribute.
# Once this info is collected, it writes it to data.dict.tsv
#


# This function creates a dictionary for each attribute, then loads the data in
# from the combined.data.tsv file. Each unique value for each attribute is
# stored in that attribute's dict as a key and a counter is initialized to 1.
# Every time that value is encountered, it increments this counter.
# Once finished, all the attribute dicts are stored in another dict and
# then that dict is returned.
def load_data():
    data = open("../data/combined.data.tsv", "r", encoding="utf-8")

    # Create dicts for each attribute
    nconstDict = {}
    primaryNameDict = {}
    birthYearDict = {}
    deathYearDict = {}
    primaryProfessionDict = {}
    knownForTitleDict = {}
    titleTypeDict = {}
    primaryTitleDict = {}
    originalTitleDict = {}
    localTitleDict = {}
    isAdultDict = {}
    startYearDict = {}
    endYearDict = {}
    runTimeDict = {}
    genreDict = {}
    orderingDict = {}
    regionDict = {}
    languageDict = {}
    typeDict = {}
    attributeDict = {}
    isOriginalTitleDict = {}
    averageRatingDict = {}
    numVotesDict = {}

    # Read first line in since it's just attribute names
    data.readline()
    print("Loading and counting data. This will take a while.")
    # Iterate through each data record in our combined data file
    for record in data:
        # split the data into attributes on the \t character.
        nconst, primaryName, birthYear, deathYear, primaryProfession, \
        knownForTitle, titleType, primaryTitle, originalTitle, localTitle, \
        isAdult, startYear, endYear, runTime, genre, ordering, region, language, \
        attributeType, attribute, isOriginalTitle, avgRating, numVotes = \
            record.split("\t")
        numVotes = numVotes.replace("\n", "")

        # For each attribute, add unique values to counter and initialize to 1.
        # If value already in dict, increment counter.
        if nconst in nconstDict:
            nconstDict[nconst] += 1
        else:
            nconstDict[nconst] = 1

        # For each remaining attribute, if the value is missing, skip over it
        if primaryName == "\\N":
            pass
        elif primaryName in primaryNameDict:
            primaryNameDict[primaryName] += 1
        else:
            primaryNameDict[primaryName] = 1

        if birthYear.isdigit():
            birthYear = int(birthYear)
        if birthYear == "\\N":
            pass
        elif birthYear in birthYearDict:
            birthYearDict[birthYear] += 1
        else:
            birthYearDict[birthYear] = 1

        if deathYear.isdigit():
            deathYear = int(deathYear)
        if deathYear == "\\N":
            pass
        elif deathYear in deathYearDict:
            deathYearDict[deathYear] += 1
        else:
            deathYearDict[deathYear] = 1

        if primaryProfession == "\\N":
            pass
        elif primaryProfession in primaryProfessionDict:
            primaryProfessionDict[primaryProfession] += 1
        else:
            primaryProfessionDict[primaryProfession] = 1

        if knownForTitle == "\\N":
            pass
        elif knownForTitle in knownForTitleDict:
            knownForTitleDict[knownForTitle] += 1
        else:
            knownForTitleDict[knownForTitle] = 1

        if titleType == "\\N":
            pass
        elif titleType in titleTypeDict:
            titleTypeDict[titleType] += 1
        else:
            titleTypeDict[titleType] = 1

        if primaryTitle == "\\N":
            pass
        elif primaryTitle in primaryTitleDict:
            primaryTitleDict[primaryTitle] += 1
        else:
            primaryTitleDict[primaryTitle] = 1

        if originalTitle == "\\N":
            pass
        elif originalTitle in originalTitleDict:
            originalTitleDict[originalTitle] += 1
        else:
            originalTitleDict[originalTitle] = 1

        if localTitle == "\\N":
            pass
        elif localTitle in localTitleDict:
            localTitleDict[localTitle] += 1
        else:
            localTitleDict[localTitle] = 1

        if isAdult == "\\N":
            pass
        elif isAdult in isAdultDict:
            isAdultDict[isAdult] += 1
        else:
            isAdultDict[isAdult] = 1

        # For attributes with a meaningful numeric value, check if its a digit
        # If it is a digit, cast it to an int or float
        if startYear.isdigit():
            startYear = int(startYear)
        if startYear == "\\N":
            pass
        elif startYear in startYearDict:
            startYearDict[startYear] += 1
        else:
            startYearDict[startYear] = 1

        if endYear.isdigit():
            endYear = int(endYear)
        if endYear == "\\N":
            pass
        elif endYear in endYearDict:
            endYearDict[endYear] += 1
        else:
            endYearDict[endYear] = 1

        if runTime.isdigit():
            runTime = int(runTime)
        if runTime == "\\N":
            pass
        elif runTime in runTimeDict:
            runTimeDict[runTime] += 1
        else:
            runTimeDict[runTime] = 1

        if genre == "\\N":
            pass
        elif genre in genreDict:
            genreDict[genre] += 1
        else:
            genreDict[genre] = 1

        if ordering.isdigit():
            ordering = int(ordering)
        if ordering == "\\N":
            pass
        elif ordering in orderingDict:
            orderingDict[ordering] += 1
        else:
            orderingDict[ordering] = 1

        if region == "\\N":
            pass
        elif region in regionDict:
            regionDict[region] += 1
        else:
            regionDict[region] = 1

        if language == "\\N":
            pass
        elif language in languageDict:
            languageDict[language] += 1
        else:
            languageDict[language] = 1

        if attributeType == "\\N":
            pass
        elif attributeType in typeDict:
            typeDict[attributeType] += 1
        else:
            typeDict[attributeType] = 1

        if attribute == "\\N":
            pass
        elif attribute in attributeDict:
            attributeDict[attribute] += 1
        else:
            attributeDict[attribute] = 1

        if isOriginalTitle == "\\N":
            pass
        elif isOriginalTitle in isOriginalTitleDict:
            isOriginalTitleDict[isOriginalTitle] += 1
        else:
            isOriginalTitleDict[isOriginalTitle] = 1

        if avgRating.isdigit():
            avgRating = float(avgRating)
        if avgRating == "\\N":
            pass
        elif avgRating in averageRatingDict:
            averageRatingDict[avgRating] += 1
        else:
            averageRatingDict[avgRating] = 1

        if numVotes.isdigit():
            numVotes = int(numVotes)
        if numVotes == "\\N":
            pass
        elif numVotes in numVotesDict:
            numVotesDict[numVotes] += 1
        else:
            numVotesDict[numVotes] = 1
    data.close()

    # Store data in parent dictionary and return it
    dataDict = {
        "nconst": nconstDict,
        "primaryName": primaryNameDict,
        "birthYear": birthYearDict,
        "deathYear": deathYearDict,
        "primaryProfession": primaryProfessionDict,
        "knownForTitle": knownForTitleDict,
        "titleType": titleTypeDict,
        "primaryTitle": primaryTitleDict,
        "originalTitle": originalTitleDict,
        "localTitle": localTitleDict,
        "isAdult": isAdultDict,
        "startYear": startYearDict,
        "endYear": endYearDict,
        "runtime": runTimeDict,
        "genre": genreDict,
        "ordering": orderingDict,
        "region": regionDict,
        "language": languageDict,
        "type": typeDict,
        "attribute": attributeDict,
        "isOriginalTitle": isOriginalTitleDict,
        "averageRating": averageRatingDict,
        "numVotes": numVotesDict
    }

    return dataDict


# This function takes the data dict we created, determines the number of
# unique values, total values, and interval for numeric values, for each
# attribute. This data is then written to data.dict.tsv
def write_dict_file(dataDict):
    # Load attribute dicts from parent dict
    nconstDict = dataDict["nconst"]
    primaryNameDict = dataDict["primaryName"]
    birthYearDict = dataDict["birthYear"]
    deathYearDict = dataDict["deathYear"]
    primaryProfessionDict = dataDict["primaryProfession"]
    knownForTitleDict = dataDict["knownForTitle"]
    titleTypeDict = dataDict["titleType"]
    primaryTitleDict = dataDict["primaryTitle"]
    originalTitleDict = dataDict["originalTitle"]
    localTitleDict = dataDict["localTitle"]
    isAdultDict = dataDict["isAdult"]
    startYearDict = dataDict["startYear"]
    endYearDict = dataDict["endYear"]
    runTimeDict = dataDict["runtime"]
    genreDict = dataDict["genre"]
    orderingDict = dataDict["ordering"]
    regionDict = dataDict["region"]
    languageDict = dataDict["language"]
    typeDict = dataDict["type"]
    attributeDict = dataDict["attribute"]
    isOriginalTitleDict = dataDict["isOriginalTitle"]
    averageRatingDict = dataDict["averageRating"]
    numVotesDict = dataDict["numVotes"]

    print("Writing Data Dictionary File")
    # Create new file for data dictionary
    dataDictFile = open("../data/data.dict.tsv", "w", encoding="utf-8")
    dataDictFile.write(
        "attribute\tuniqueValues\ttotalValues\tdataType\tmeasurement\trange\n"
    )

    # For each attribute, retrieve unique values from number of keys,
    # then sum value for each key in dict to get total number of values.
    # Finally, write unique values, total values, data type, measurement type,
    # and range to new file. Range is NA if not applicable
    nconstUniqueValues = len(nconstDict)
    totalNconsts = 0
    for nconst in nconstDict:
        totalNconsts += nconstDict[nconst]
    dataDictFile.write(
        f"nconst\t{nconstUniqueValues}\t{totalNconsts}\tstring\tnominal\tNA\n"
    )

    primaryNameUniqueValues = len(primaryNameDict)
    totalPrimaryNames = 0
    for primaryName in primaryNameDict:
        totalPrimaryNames += primaryNameDict[primaryName]
    dataDictFile.write(
        f"primaryName\t{primaryNameUniqueValues}\t{totalPrimaryNames}\t"
        f"string\tnominal\tNA\n"
    )

    birthYearUniqueValues = len(birthYearDict)
    totalBirthYears = 0
    # For each numeric attribute, get the keys from the dict, then determine
    # the min and max values to get the range
    birthYears = birthYearDict.keys()
    minBirthYear = min(birthYears)
    maxBirthYear = max(birthYears)
    for birthYear in birthYearDict:
        totalBirthYears += birthYearDict[birthYear]
    dataDictFile.write(
        f"birthYear\t{birthYearUniqueValues}\t{totalBirthYears}\tinteger\t"
        f"interval\t[{minBirthYear}-{maxBirthYear}]\n"
    )

    deathYearUniqueValues = len(deathYearDict)
    totalDeathYears = 0
    deathYears = deathYearDict.keys()
    minDeathYear = min(deathYears)
    maxDeathYear = max(deathYears)
    for deathYear in deathYearDict:
        totalDeathYears += deathYearDict[deathYear]
    dataDictFile.write(
        f"deathYear\t{deathYearUniqueValues}\t{totalDeathYears}\tinteger\t"
        f"interval\t[{minDeathYear}-{maxDeathYear}]\n"
    )

    primaryProfessionUniqueValues = len(primaryProfessionDict)
    totalPrimaryProfessions = 0
    for primaryProfession in primaryProfessionDict:
        totalPrimaryProfessions += primaryProfessionDict[primaryProfession]
    dataDictFile.write(
        f"primaryProfession\t{primaryNameUniqueValues}\t{totalPrimaryProfessions}\t"
        f"string\tcategorical\tNA\n"
    )

    knownForTitleUniqueValues = len(knownForTitleDict)
    totalKnownForTitles = 0
    for knownForTitle in knownForTitleDict:
        totalKnownForTitles += knownForTitleDict[knownForTitle]
    dataDictFile.write(
        f"knownForTitle\t{knownForTitleUniqueValues}\t{totalKnownForTitles}\t"
        f"string\tnominal\tNA\n"
    )

    titleTypeUniqueValues = len(titleTypeDict)
    totalTitleTypes = 0
    for titleType in titleTypeDict:
        totalTitleTypes += titleTypeDict[titleType]
    dataDictFile.write(
        f"titleType\t{titleTypeUniqueValues}\t{totalTitleTypes}\tstring\t"
        f"nominal\tNA\n"
    )

    primaryTitleUniqueValues = len(primaryTitleDict)
    totalPrimaryTitles = 0
    for primaryTitle in primaryTitleDict:
        totalPrimaryTitles += primaryTitleDict[primaryTitle]
    dataDictFile.write(
        f"primaryTitle\t{primaryTitleUniqueValues}\t{totalPrimaryTitles}\tstring\t"
        f"nominal\tNA\n"
    )

    originalTitleUniqueValues = len(originalTitleDict)
    totalOriginalTitles = 0
    for originalTitle in originalTitleDict:
        totalOriginalTitles += originalTitleDict[originalTitle]
    dataDictFile.write(
        f"originalTitle\t{originalTitleUniqueValues}\t{totalOriginalTitles}\t"
        f"string\tnominal\tNA\n"
    )

    localTitleUniqueValues = len(localTitleDict)
    totalLocalTitles = 0
    for localTitle in localTitleDict:
        totalLocalTitles += localTitleDict[localTitle]
    dataDictFile.write(
        f"localTitle\t{localTitleUniqueValues}\t{totalLocalTitles}\tstring\t"
        f"nominal\tNA\n"
    )

    totalIsAdults = 0
    for isAdult in isAdultDict:
        totalIsAdults += isAdultDict[isAdult]
    dataDictFile.write(f"isAdult\t2\t{totalIsAdults}\tbool\tcategorical\tNA\n")

    startYearUniqueValues = len(startYearDict)
    totalStartYears = 0
    startYears = startYearDict.keys()
    minStartYear = min(startYears)
    maxStartYear = max(startYears)
    for startYear in startYearDict:
        totalStartYears += startYearDict[startYear]
    dataDictFile.write(
        f"startYear\t{startYearUniqueValues}\t{totalStartYears}\tinteger\t"
        f"interval\t[{minStartYear}-{maxStartYear}]\n"
    )

    dataDictFile.write("endYear\t0\t0\tinteger\tinterval\tNA\n")

    runTimeUniqueValues = len(runTimeDict)
    totalRunTimes = 0
    runTimes = runTimeDict.keys()
    minRunTime = min(runTimes)
    maxRunTime = max(runTimes)
    for runTime in runTimeDict:
        totalRunTimes += runTimeDict[runTime]
    dataDictFile.write(
        f"runtimeMinutes\t{runTimeUniqueValues}\t{totalRunTimes}\tinteger\tratio\t"
        f"[{minRunTime}-{maxRunTime}]\n"
    )

    genreUniqueValues = len(genreDict)
    totalGenres = 0
    for genre in genreDict:
        totalGenres += genreDict[genre]
    dataDictFile.write(
        f"genre\t{genreUniqueValues}\t{totalGenres}\tstring\tcategorical\tNA\n"
    )

    orderingUniqueValues = len(orderingDict)
    totalOrderings = 0
    for ordering in orderingDict:
        totalOrderings += orderingDict[ordering]
    dataDictFile.write(
        f"ordering\t{orderingUniqueValues}\t{totalOrderings}\tinteger\tnominal\t"
        f"NA\n"
    )

    totalRegions = regionDict['US']
    dataDictFile.write(f"region\t1\t{totalRegions}\tstring\tcategorical\tNA\n")

    languageUniqueValues = len(languageDict)
    totalLanguages = 0
    for language in languageDict:
        totalLanguages += languageDict[language]
    dataDictFile.write(
        f"language\t{languageUniqueValues}\t{totalLanguages}\tstring\tcategorical\t"
        f"NA\n"
    )

    typeUniqueValues = len(typeDict)
    totalTypes = 0
    for attributeType in typeDict:
        totalTypes += typeDict[attributeType]
    dataDictFile.write(
        f"type\t{typeUniqueValues}\t{totalTypes}\tstring\tcategorical\tNA\n"
    )

    attributeUniqueValues = len(attributeDict)
    totalAttributes = 0
    for attribute in attributeDict:
        totalAttributes += attributeDict[attribute]
    dataDictFile.write(
        f"attribute\t{attributeUniqueValues}\t{totalAttributes}\tstring\t"
        f"categorical\tNA\n"
    )

    totalIsOriginalTitles = 0
    for isOriginalTitle in isOriginalTitleDict:
        totalIsOriginalTitles += isOriginalTitleDict[isOriginalTitle]
    dataDictFile.write(
        f"isOriginalTitle\t2\t{totalIsOriginalTitles}\tbool\tcategorical\tNA\n"
    )

    avgRatingUniqueValues = len(averageRatingDict)
    totalAvgRatings = 0
    avgRatings = averageRatingDict.keys()
    minAvgRating = min(avgRatings)
    maxAvgRating = max(avgRatings)
    for avgRating in averageRatingDict:
        totalAvgRatings += averageRatingDict[avgRating]
    dataDictFile.write(
        f"averageRating\t{avgRatingUniqueValues}\t{totalAvgRatings}\tfloat\tratio\t"
        f"[{minAvgRating}-{maxAvgRating}]\n"
    )

    numVotesUniqueValues = len(numVotesDict)
    totalNumVotesRecords = 0
    numVotesRecords = numVotesDict.keys()
    minNumVotes = min(numVotesRecords)
    maxNumVotes = max(numVotesRecords)
    for numVotes in numVotesDict:
        totalNumVotesRecords += numVotesDict[numVotes]
    dataDictFile.write(
        f"numVotes\t{numVotesUniqueValues}\t{totalNumVotesRecords}\tinteger\t"
        f"ratio\t[{minNumVotes}-{maxNumVotes}]\n"
    )


# Run the script, first loading in the data and returning a dataDict,
# then writing it to the new file
if __name__ == "__main__":
    dataDict = load_data()
    write_dict_file(dataDict)
