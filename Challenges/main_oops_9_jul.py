import logging # logging

logging.basicConfig(filename='main.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class ineuron:
    logging.info('Welcome to ineuron')
    try:
        logging.info('Here Encapusaltion is happening')

        student = "Yashas Pissay"
        _no_of_course = 5

        def __init__(self):
            self.__course = "Data Science "

        def courses(self):
            print(self.__course)

        def course_change(self, new_course):
            self.__course = new_course

        def jobs(self):
            print('we can reccomad the jobs through ineuron')

    except Exception as e:
            logging.error(e)

i = ineuron()
print(i.student)
print(i._no_of_course)
i.courses()
i.course_change("Data Analaytics")
i.courses()
i.jobs()

class affilicate(ineuron) :
    logging.info('this is child affilicated class inherited from parent ineuron class')
    logging.info('Here  multilevel inheritance and absraction and overriding is happening')
    try :
        __internship = 'data science'

        def interships(self):
            print("i'm currently doing", affilicate.__internship, "internship")

        def jobs(self):
            print('These are overriding statement affilacated jobs through ineuron to diffrenet companies')

        def blogs(self):
            print("I'm writting new blogs about internships and jobs")

    except Exception as e:
        logging.error(e)

j = affilicate()
print(j.student)
print(j._no_of_course)
j.interships()
j.blogs()
j.jobs()


class ineuron_vision:
    logging.info('here polymorshim is happening')
    try:
        def vision(self):
            print('to become successful data scienstist')

        def blogs(self):
            print('in this blog we written about ineuron vision')

    except Exception as e:
        logging.error(e)

def refrences(a):
    a.blogs()
    x = affilicate()
    y = ineuron_vision()
    refrences(x)
    refrences(y)
logging.info('Programm is closed')