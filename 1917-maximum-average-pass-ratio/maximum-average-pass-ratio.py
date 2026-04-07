import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def passRatio(pass_i, total_i):
            return pass_i/total_i
        
        changeHeap = []
        for i, class_i in enumerate(classes):
            heapq.heappush(changeHeap, (-1 * (passRatio(class_i[0] + 1, class_i[1] + 1) - passRatio(class_i[0], class_i[1])), i))
        
        for _ in range(extraStudents):
            addStudentClass = heapq.heappop(changeHeap)
            classes[addStudentClass[1]][0] += 1
            classes[addStudentClass[1]][1] += 1
            heapq.heappush(changeHeap, (-1 * (passRatio(classes[addStudentClass[1]][0] + 1, classes[addStudentClass[1]][1] + 1) - passRatio(classes[addStudentClass[1]][0], classes[addStudentClass[1]][1])), addStudentClass[1]))
        
        avgPassRatio = 0
        for class_i in classes:
            avgPassRatio += passRatio(class_i[0], class_i[1])
        return avgPassRatio/len(classes)
        