# students-results
class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}
        #{"english": [10, 10, 20, 60, 100],"maths": [10, 10, 20, 60, 100]}

    def enter_score(self):
        number_of_subjects = int(input(f"\nInput subjects to be registered for {self.name} "))

        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            number_of_scores = 4
            score_list = []

            for x in range(number_of_scores):
                score = int(input(f"Enter score {x+1} for {subject_name}: "))
                score_list.append(score)

            total = sum(score_list)
            score_list.append(total)

            self.subjects[subject_name] = score_list
            print(f"For {subject_name}, the scores so far are: {self.total}")
