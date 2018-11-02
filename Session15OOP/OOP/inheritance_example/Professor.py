from BabsonPerson import BabsonPerson
from Person import Person

class Professor(BabsonPerson):

    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def speak(self, utterance):
        new_utterance = 'In course' + self.course + 'we say'
        return BabsonPerson.speak(self, new_utterance + utterance)

    def lecture(self, topic):
        return 




def main():
    # prof1 = Professor('Zhi Li', 5)
    # prof2 = Professor('Feld', 4.3)
    # prof3 = Professor('Bauer', 4.5)
    # prof4 = BabsonPerson('Matt Damon')

    # professor_list = [prof1, prof2, prof3, prof4]

    # print(prof1)

    # print(prof1.get_rating())

    print(prof1.get_course())

    # print(isStudent(s1))

    # p1 = Person('Taylor Swift')
    # print(isStudent(p1))

if __name__ == '__main__':
    main()
