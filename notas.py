'''
Creating a program to compute statistics means that you won't have to whip out your calculator and manually crunch numbers.
1 - Writing a function to print out the list of grades;
2 - Create another function to compute the sum of all of the test grades.
3 - The average can be found by dividing the sum of the grades by the total number of grades.
4 - computing the variance: A very large variance means that the students' grades were all over the place, while a small variance means that the majority of students did fairly well.
5 - Standard Deviation: The standard deviation is the square root of the variance.
'''

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance (scores):
    average = grades_average(scores)
    variance = 0
    for i in scores:
        variance += (average - i) ** 2
    return variance/ float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
