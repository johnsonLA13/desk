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

    def getCourseRating(self):
        return float(self.__courseRating)

    def getSlopeRating(self):
        return float(self.__slopeRating)

    def getCRratio(self):
        cr = float(self.__courseRating)
        par = float(self.__par)
        return cr / par

    def getPar(self):
        return float(self.__par)

    def getF9(self):
        return float(self.__f9)

    def getB9(self):
        return float(self.__b9)

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

    def getCourseName(self):
        return self.__courseName

    def getScoreActual(self):
        if self.__score == 0:
            if self.__f9 == 0:
                return self.__b9
            else:
                return self.__f9
        else:
            return self.__score

    def getScore(self):
        return float(self.__score)

    def getF9(self):
        return float(self.__f9)

    def getB9(self):
        return float(self.__b9)

    def __repr__(self):
        if self.__score == 0:
            if self.__f9 == 0:
                s = "Score for back 9 Holes at " + str(self.__courseName) + ": " + str(self.__b9)
            else:
                s = "Score for front 9 Holes at " + str(self.__courseName) + ": " + str(self.__f9)
        else:
            s = "Score for 18 Holes at " + str(self.__courseName) + ": " + str(self.__score)
        return s

def calculateHandicaps(c_dict, s_dict):
    handicaps = [] #initiate handicap list
    scoreListLen = len(s_dict)
    sValues = list(s_dict.values())
    for i in range(scoreListLen):
        scoreObj = sValues[i]
        score = float(scoreObj.getScoreActual())
        course = c_dict[scoreObj.getCourseName()]
        cr = float(course.getCourseRating())
        sr = float(course.getSlopeRating())
        if scoreObj.getScore() == 0:
            if scoreObj.getF9() == 0:
                #cr = float(course.getB9() * course.getCRratio())
                score = score * 2 #multiply score by two if only back 9 holes played
            else:
                #cr = float(course.getF9() * course.getCRratio())
                score = score * 2 #multiply score by two if only front 9 holes played
        print(score)
        handicap = round(((score - cr) * 113.0) / sr, 2)
        handicaps.append(handicap)
    handicaps.sort()
    return handicaps

def calculateHandicap(handicap_list):
    rounds = len(handicap_list)
    if rounds >= 8 and rounds < 10:
        sum = 0
        for r in range(3):
            sum += handicap_list[r]
            print(sum)
        avg = sum / 3
    return avg * 0.96



def main():
    csvfile = open('courses.csv', 'r') #open courses csv file
    coursesCSV = csv.reader(csvfile, delimiter=',')
    next(coursesCSV)
    courseDict = {}
    for c in coursesCSV:
        newCourse = Course(c[0], c[1], c[2], c[3], c[4], c[5])
        courseDict.update({c[0] : newCourse})

    scsvfile = open('scores.csv', 'r') #open scores csv file
    scoresCSV = csv.reader(scsvfile, delimiter=',')
    next(scoresCSV)
    scoreDict = {}
    for s in scoresCSV:
        print(s)
        newScore = Score(s[0], s[1], s[2], s[3], s[4])
        scoreDict.update({s[0] : newScore})
    
    #close files
    csvfile.close()
    scsvfile.close()

    #print courses for testing
    c_l = len(courseDict)
    cDictValues = list(courseDict.values())
    for i in range(c_l):
        print("C" + str(i+1) + " \n" + str(cDictValues[i]))

    #print scores for testing
    s_l = len(scoreDict)
    sDictValues = list(scoreDict.values())
    for i in range(s_l):
        print(str(sDictValues[i]))
        print(sDictValues[i].getScore())

    hcs = calculateHandicaps(courseDict, scoreDict)
    print(hcs)
    hc = round(calculateHandicap(hcs), 2)
    print("Your Handicap is: " + str(hc))



if __name__ == "__main__":
    main()

