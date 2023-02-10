class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        if self.name == 'Виталя':
            print(f'{self.name} {question}')
            print('Очень интересный вопрос! Не знаю.')
        else:
            print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        someone.answer_question(question)
        print(f'{self.name} {question}')
        # print(f'{self.name} {question}')
        # запросите ответ на вопрос у someone
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
    # если да - ответить на него
    # если нет - вызвать метод answer_question() у родительского класса
    def answer_question(self, question):
        if question:
            print(f'{self.name} {question}')
        else:
            answer = 'Держись, всё получится. Хочешь видео с котиками?'
            super().answer_question(answer)


class CodeReviewer(Human):

    def answer_question(self, question):
        if question:
            print(f'{self.name} {question}')
        else:
            answer = 'Отдохни и возвращайся с вопросами по теории.'
            super().answer_question(answer)


class Mentor(Human):

    def answer_question(self, question):
        if question:

            print(f'{self.name} {question}')
        else:
            answer = 'О, вопрос про проект, это я люблю.'
            super().answer_question(answer)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')