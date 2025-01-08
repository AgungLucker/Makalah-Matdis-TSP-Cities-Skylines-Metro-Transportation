import math

maxsize = float('inf')

def findFirstMinimum(adjacencyMatrix, i):
    firstMinimum = maxsize
    for k in range(len(adjacencyMatrix)):
        if adjacencyMatrix[i][k] < firstMinimum and i != k:
            firstMinimum = adjacencyMatrix[i][k]
    return firstMinimum

def findSecondMinimum(adjacencyMatrix, i):
    firstminimum, secondMinimum = maxsize, maxsize
    for j in range(len(adjacencyMatrix)):
        if i != j:
            if adjacencyMatrix[i][j] <= firstminimum:
                secondMinimum = firstminimum
                firstminimum = adjacencyMatrix[i][j]
            elif adjacencyMatrix[i][j] <= secondMinimum and adjacencyMatrix[i][j] != firstminimum:
                secondMinimum = adjacencyMatrix[i][j]
    return secondMinimum

def finalPathResult(currentPath, finalPath, adjacencyMatrix):
    for i in range (len(adjacencyMatrix)):
        finalPath[i] = currentPath[i]
    finalPath[len(adjacencyMatrix)] = currentPath[0]
    
def branchandBoundRecursion(adjacencyMatrix, currentBound, currentBiaya, level, currentPath, locationVisited):
    global biayaMinimum
     
    # Basis
    if level == len(adjacencyMatrix):
        if adjacencyMatrix[currentPath[level - 1]][currentPath[0]] != 0:
            currentBiayaMinimum = currentBiaya + adjacencyMatrix[currentPath[level - 1]][currentPath[0]]
            if currentBiayaMinimum < biayaMinimum:
                finalPathResult(currentPath, finalPath, adjacencyMatrix)
                biayaMinimum = currentBiayaMinimum
        return
 
    for i in range(len(adjacencyMatrix)):
        if (adjacencyMatrix[currentPath[level-1]][i] != 0 and not locationVisited[i]):
            tempBound = currentBound
            currentBiaya += adjacencyMatrix[currentPath[level - 1]][i]
 
            # Update bound based on level
            if level == 1:
                currentBound -= (findFirstMinimum(adjacencyMatrix, currentPath[level - 1]) + findFirstMinimum(adjacencyMatrix, i)) / 2
            else:
                currentBound -= (findSecondMinimum(adjacencyMatrix, currentPath[level - 1]) + findSecondMinimum(adjacencyMatrix, i)) / 2
 
            # Rekurens
            if currentBound + currentBiaya < biayaMinimum:
                currentPath[level] = i
                locationVisited[i] = True
                branchandBoundRecursion(adjacencyMatrix, currentBound, currentBiaya, level + 1, currentPath, locationVisited)
 
            # Backtracking
            currentBiaya -= adjacencyMatrix[currentPath[level - 1]][i]
            currentBound = tempBound
            locationVisited = [False] * len(locationVisited)
            for j in range(level):
                if currentPath[j] != -1:
                    locationVisited[currentPath[j]] = True

# Inisialisasi Matriks ketetanggaan
simpulStasiun = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
adjacencyMatrix = [
    [0, 51680, 106400, 74480, 120840, 90060, 57760],  
    [51680, 0, 66500, 68400, 119320, 116660, 71440],  
    [106400, 66500, 0, 64600, 90060, 121600, 82080],  
    [74480, 68400, 64600, 0, 45600, 58520, 23940],
    [120840, 119320, 90060, 45600, 0, 59280, 58900],
    [90060, 116660, 121600, 58520, 59280, 0, 44080],
    [57760, 71440, 82080, 23940, 58900, 44080, 0]
]
symbolToIndexMapper = {chr(65 + i): i for i in range(26)}  
indexToSymbolMapper = {v: k for k, v in symbolToIndexMapper.items()}

# Driver Program
biayaMinimum = maxsize
currentBound = 0
finalPath = [None] * (len(adjacencyMatrix) + 1)
currentPath = [-1] * (len(adjacencyMatrix) + 1)
locationVisited = [False] * len(adjacencyMatrix)

for i in range(len(adjacencyMatrix)):
    currentBound += (findFirstMinimum(adjacencyMatrix, i) + findSecondMinimum(adjacencyMatrix, i))
currentBound = math.ceil(currentBound / 2)

locationVisited[0] = True
currentPath[0] = 0

branchandBoundRecursion(adjacencyMatrix, currentBound, 0, 1, currentPath, locationVisited)

print("")
print("Rute Metro Teroptimal:", " - ".join(indexToSymbolMapper[node] for node in finalPath))
print("Total biaya minimum dari rute Metro teroptimal:", biayaMinimum)
print("")





