class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.english_score = None
        self.maths_score = None
        self.science_score = None 

    def speak(self):
        """
        commands the students to say its name and age
        """
        print(f"hello! my name is {self.name} and I'm {self.age} years old")

    #def enter_score(self, english, maths, science):
        #self.english_score = english
        #self.maths_score = maths
        #self.science_score = science

james = student("james", 25, "male")
james.speak()
