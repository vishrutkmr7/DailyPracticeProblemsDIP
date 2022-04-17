# This problem was recently asked by Google:

# You are given a hash table where the key is a course code, and the value is a list of all the course codes
# that are prerequisites for the key. Return a valid ordering in which we can complete the courses.
# If no such ordering exists, return NULL.

import operator

def courses_to_take(course_to_prereqs):
    count = {}
    for i in course_to_prereqs:
        if i not in count.keys():
            count[i] = 0

        for j in course_to_prereqs[i]:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
    nullChk = sum(count.values())
    if nullChk == 0:
        return 'NULL'

    sort_count = sorted(count.items(), key=lambda kv:kv[1],reverse=True)
    return [i[0] for i in sort_count]


courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
