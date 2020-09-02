import csv

class Course:
    def __init__(self, name, courseRating, slopeRating, par, f9, b9):
        self.__name = name
        self.__courseRating = courseRating
        self.__slopeRating = slopeRating
        self.__par = par
        self.__f9 = f9
        self.__b9 = b9

    def __repr__(self):
        s = "Name: " + self.__name + "\n" + "   CR: " + str(self.__courseRating) + "\n" + "   SR: " + str(self.__slopeRating) + "\n" + "   Par: " + str(self.__par) + "\n"
        return s

class Score:
    def __init__(self, date, courseName, score, f9, b9):
        self.__date = date
        self.__courseName = courseName
        if score == '':
            self.__score = 0
        else:
            self.__score = score
        if f9 == '':
            self.__f9 = 0
        else:
            self.__f9 = f9
        if b9 == '':
            self.__b9 = 0
        else:
            self.__b9 = b9
    
    def getScore(self):
        return self.__score

    def __repr__(self):
        if self.__score == 0:
            if self.__f9 == 0:
                s = "Score for back 9 Holes at " + str(self.__courseName) + ": " + str(self.__b9)
            else:
                s = "Score for front 9 Holes at " + str(self.__courseName) + ": " + str(self.__f9)
        else:
            s = "Score for 18 Holes at " + str(self.__courseName) + ": " + str(self.__score)
        return s

def main():
    csvfile = open('courses.csv', 'r') #open courses csv file
    coursesCSV = csv.reader(csvfile, delimiter=',')
    courseDict = {}
    for c in coursesCSV:
        newCourse = Course(c[0], c[1], c[2], c[3], c[4], c[5])
        courseDict.update({c[0] : newCourse})

    scsvfile = open('scores.csv', 'r') #open scores csv file
    scoresCSV = csv.reader(scsvfile, delimiter=',')
    scoreDict = {}
    for s in scoresCSV:
        print(s)
        newScore = Score(s[0], s[1], s[2], s[3], s[4])
        scoreDict.update({s[0] : newScore})
    
    #close files
    csvfile.close()
    scsvfile.close()

    #print courses for testing
    l = len(courseDict)
    cDictValues = list(courseDict.values())
    for i in range(l):
        print("C" + str(i+1) + " \n" + str(cDictValues[i]))

    #print scores for testing
    l = len(scoreDict)
    sDictValues = list(scoreDict.values())
    for i in range(l):
        print(str(sDictValues[i]))
        print(str(sDictValues[i].getScore()))


if __name__ == "__main__":
    main()

