# This problem was recently asked by Google:

# You are given a hash table where the key is a course code, and the value is a list of all the course codes
# that are prerequisites for the key. Return a valid ordering in which we can complete the courses.
# If no such ordering exists, return NULL.

from pprint import pprint
import operator

def courses_to_take(course_to_prereqs):
    # Fill this in.
    count = {}
    final = []
    for i in course_to_prereqs:
        # print(i)
        if i not in count.keys():
            count[i] = 0

        for j in course_to_prereqs[i]:
            if j not in count.keys():
                count[j] = 1
            else:
                count[j] += 1

    sort_count = sorted(count.items(), key=lambda kv:kv[1],reverse=True)
    # Based on the assumption that a course that appears the most amongst the prerequesites must be taken first
    # Pl. suggest an alternative if possible.
    for i in sort_count:
        final.append(i[0])
    
    return final


courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
