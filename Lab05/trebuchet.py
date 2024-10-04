# Author: Erik Bobinski
# Date: 10/4/2024
# Description: User inputs distances for a trebuchet to launch,
# outputs the top 3 distances and the corresponding trial

top3Dist = [0,0,0] # distances in descending order, each element is a launch distance from the trebuchet
top3Trial = [0,0,0] # the trial numbers of the top three distances
Y = True # whether user wishes to input additional trials

# insert new trial if in top 3 greatest distances
trialCnt = 1
while(Y):
    newDist = int( input("Enter a distance as an integer: ") )
    if newDist > top3Dist[0]:
        top3Dist.insert(0, newDist)
        top3Trial.insert(0, trialCnt)
    elif newDist > top3Dist[1]:
        top3Dist.insert(1,newDist)
        top3Trial.insert(1, trialCnt)
    elif newDist > top3Dist[2]:
        top3Dist.insert(2,newDist)
        top3Trial.insert(2,trialCnt)
    userChoice = input("Enter \"Y\" if you wish to enter another trial: ")

    if userChoice == "Y" or userChoice == "y":
        Y = True
    else:
        Y = False
    trialCnt += 1

print("\nBelow are the top three trial distances and their trial number:")
print("Trial    Distance")
print(f"{top3Trial[0]}        {top3Dist[0]} ft\n{top3Trial[1]}        {top3Dist[1]} ft\n{top3Trial[2]}        {top3Dist[2]} ft\n ")
