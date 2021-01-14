from textblob import TextBlob
import json
import statistics
import textstat
import numpy as np
import matplotlib.pyplot as plt
import requests

try:
    url = "https://dgoldberg.sdsu.edu/515/customer_service_tweets_full.json"
    r = requests.get(url)
    data = r.json()
except:
    with open("Enter file path here") as f:
        data=json.load(f)

# Filterig data
mainList = [['@sprintcare'], ['@Ask_Spectrum'], ['@AskPlayStation'], ['@XboxSupport'], ['@UPSHelp'], ['@AmazonHelp'],
            ['@AppleSupport'], ['@Uber_Support'], ['@SpotifyCares'], ['@comcastcares'], ['@TMobileHelp'],
            ['@hulu_support']]
for i in data:
    for j in mainList:
        if i['Company'] == j[0]:
            j.append(i['Text'])


# Calculating average polarity
def avgPolarity(mainList):
    meanList = {}
    for item in mainList:
        list1 = []
        for j in item[1:]:
            r = TextBlob(j).polarity
            list1.append(r)
        x = statistics.mean(list1)
        meanList[item[0]] = x
    return meanList


# average subjectivity
def avgSubjectivity(mainList):
    meanList = {}
    for item in mainList:
        list1 = []
        for j in item[1:]:
            r = TextBlob(j).subjectivity
            list1.append(r)
        x = statistics.mean(list1)
        meanList[item[0]] = x
    return meanList


# average subjectivity
def avgSubjectivity(mainList):
    meanList = {}
    for item in mainList:
        list1 = []
        for j in item[1:]:
            r = TextBlob(j).subjectivity
            list1.append(r)
        x = statistics.mean(list1)
        meanList[item[0]] = x
    return meanList


# fkg Level
def fkglLevel(mainList):
    meanList = {}
    for item in mainList:
        list1 = []
        for j in item[1:]:
            r = textstat.flesch_kincaid_grade(j)
            list1.append(r)
        x = statistics.mean(list1)
        meanList[item[0]] = x
    return meanList


# Calculating smogIndex
def smogIndex(mainList):
    meanList = {}
    for item in mainList:
        list1 = []
        for j in item[1:]:
            r = textstat.smog_index(j)
            list1.append(r)
        x = statistics.mean(list1)
        meanList[item[0]] = x
    return meanList

#formality index
def formalityIndex():
    #enter the code here
    return


# search mode
def search(mainList, answer4):
    result1 = avgPolarity(mainList)
    result2 = avgSubjectivity(mainList)
    result3 = fkglLevel(mainList)
    result4 = smogIndex(mainList)
    for i, v in result1.items():
        if i == answer4:
            print('Average Polarity', ':', v)
    for i, v in result2.items():
        if i == answer4:
            print('Average Subjectivity', ':', v)
    for i, v in result3.items():
        if i == answer4:
            print("Flesch-Kincaid Grade Level-FKGL", ':', v)
    for i, v in result4.items():
        if i == answer4:
            print("SMOG index", ':', v)


# Generating barchart
def barchart(result, Tital, ylable):
    objects = []
    performance = []
    for k, v in result.items():
        objects.append(k)
        performance.append(v)
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(rotation=45, ha="right")
    plt.xticks(y_pos, objects)
    plt.ylabel(ylable)
    plt.title(Tital)
    plt.show()


# mai Body of program
while True:
    answer1 = input("Would you like to run another analysis (yes/no)? ")
    if answer1.lower() == "yes":
        answer2 = input(
            "Which analysis would you like to perform (polarity /subjectivity / readability / formality / search)? ")
        if answer2.lower() == "polarity":
            result = avgPolarity(mainList)
            for k, v in result.items():
                print(k, ':', v)
            Tital = "Average Polarity by Twitter handle"
            ylable = "Average polarity"
            barchart(result, Tital, ylable)

        elif answer2.lower() == "subjectivity":
            result = avgSubjectivity(mainList)
            for k, v in result.items():
                print(k, ':', v)
            Tital = "Average Subjectivity by Twitter handle"
            ylable = "Average Subjectivity"
            barchart(result, Tital, ylable)

        elif answer2 == "readability":
            answer3 = input("Would you like to analyze FKGL or SMOG? ")
            if answer3.lower() == "FKGL":
                result = fkglLevel(mainList)
                for k, v in result.items():
                    print(k, ':', v)
                Tital = "Flesch-Kincaid Grade Level by Twitter handle"
                ylable = "Flesch-Kincaid Grade Level-FKGL"
                xlable = "Twitter handle"
                barchart(result, Tital, ylable)
            else:
                result = smogIndex(mainList)
                for k, v in result.items():
                    print(k, ':', v)
                Tital = "SMOG index by Twitter handle"
                ylable = "SMOG"
                xlable = "Twitter handle"
                barchart(result, Tital, ylable)

        elif answer2.lower() == "formality":
            # calculate formality



            pass

        elif answer2 == "search":
            answer4 = input("Which Twitter handle would you like to search? ")
            answer4.lower()
            search(mainList, answer4)

        else:
            print("Sorry, that type of analysis is not supported. Please try again.")

    elif answer1.lower() == "no":
        break
    else:
        print("Sorry, that type of analysis is not supported. Please try again.")

