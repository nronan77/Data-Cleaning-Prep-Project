from matplotlib import pyplot as plt
import statistics
import numpy

data = open("../data/combined.data.tsv", "r", encoding="utf-8")
attribute = input("Please enter a numeric attribute name: ")

attributeIndices = {
    "birthYear": 2,
    "deathYear": 3,
    "startYear": 11,
    "runtimeMinutes": 13,
    "averageRating": 21,
    "numVotes": 22
}

ratioAttributes = ["runtimeMinutes", "averageRating", "numVotes"]

while attribute not in attributeIndices:
    attribute = input("Please enter a valid numeric attribute name: ")

attributeIndex = attributeIndices[attribute]
data.readline()
attributeValues = []
for record in data:
    recordValues = record.split("\t")
    attributeValue = recordValues[attributeIndex]
    attributeValue = attributeValue.replace("\n", "")
    if attributeValue != "\\N":
        if attribute == "averageRating":
            attributeValues.append(float(attributeValue))
        else:
            attributeValues.append(int(attributeValue))

attributeValues = sorted(attributeValues)

q1, q3 = numpy.percentile(attributeValues, [25, 75])
iqr = q3 - q1
mean = statistics.mean(attributeValues)
median = statistics.median(attributeValues)
mode = statistics.mode(attributeValues)
lowerBound = q1 - 1.5 * iqr
upperBound = q3 + 1.5 * iqr
outliers = []
for value in attributeValues:
    if value < lowerBound or value > upperBound:
        outliers.append(value)
outliers = sorted(set(outliers))

print(f"Mean: {mean}    Median: {median}    Mode: {mode}")
print(f"Outliers: {outliers}")
