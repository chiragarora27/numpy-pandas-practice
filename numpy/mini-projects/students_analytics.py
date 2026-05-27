import numpy as np

marks_data = np.random.randint(1, 101, size=[100, 5])

total_marks = np.sum(marks_data, axis=1)
total_marks = np.reshape(total_marks, shape=[100, 1])

student_ids = np.array([n for n in range(0, 100)])
student_ids = np.reshape(student_ids, shape=[100, 1])

new_data = np.hstack([student_ids, total_marks])


def average_per_student(data):
    store_avg = np.average(data, axis=1)
    store_avg = np.reshape(store_avg, shape=[store_avg.size, 1])
    print(store_avg)


def average_per_subject(data):
    store_avg = np.average(data, axis=0)
    print(store_avg)


def topper():
    topper_index = np.argmax(total_marks)
    print(topper_index)


def lowest():
    lowest_index = np.argmin(total_marks)
    print(lowest_index)


def score_above_90(data):
    tops = data[(data > 90).any(axis=1)]
    print(tops)


def bonus_marks(data):
    new_marks = data + 1
    print(data[0])
    print(new_marks[0])


def subject_highest(data):
    highest = np.max(data, axis=0)
    print(highest)


def std_deviation(data):
    std_dev = np.std(data, axis=0)
    print(std_dev)


def normalize_marks(data):
    min = np.min(data)
    max = np.max(data)

    normalized = (data - min) / (max - min)
    print(normalized)


def rank_students(data):
    sorted_marks = data[data[:, 1].argsort()[::-1]]
    print(sorted_marks)


def failed_students(data):
    fails = data[(data < 40).any(axis=1)]
    no_of_fails = fails[(fails >= 40)] = 0
    no_of_fails = fails[(fails < 40)] = 1

    sum_of_fails = np.sum(no_of_fails, axis=1)
    # sum_of_fails gives the number of failures per student
