import math

def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    failed_students = [score for score in student_scores if score <= 40]
    return len(failed_students)

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    threshold = 41 
    return list(range(threshold, highest, round((highest - threshold) / 4)))


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    student_score_pair = list(zip(student_scores, student_names))
    return [
        f"{index + 1}. {student}: {score}"
        for index, (score, student) in enumerate(student_score_pair)
    ]

   


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if(student[1] == 100): return student
    
    return []
    


