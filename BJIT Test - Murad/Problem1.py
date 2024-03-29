import heapq
# taking the input
n = int(input())
# this is our full list which will contain the nested list
matrix = []
#this list is for the savings the nested list summation
sum_matrix = []

# inserting the elements in main list
for i in range(n):
    matrix.append([])

    for j in range(n):
        j = int(input())
        matrix[i].append(j)

print(matrix)

#appending the list elements sum in another list
sum_matrix = [sum(i) for i in zip(*matrix)]
#sorting the sum list
final_matrix = heapq.nlargest(3, range(len(sum_matrix)), key=sum_matrix.__getitem__)


#printing 
print("Participant1 = ",final_matrix[0])
print("Participant2 = ",final_matrix[1])
print("Participant3 = ",final_matrix[2])

print("Participant1 scored top = ",max(sum_matrix))
print("Participant2 scored lowest = ",min(sum_matrix))
print("Avg score = ",max(sum_matrix)+min(sum_matrix)/2)



