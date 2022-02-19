game1 = int(input("Game 1 score : "))
game2 = int(input("Game 2 score : "))
game3 = int(input("Game 3 score : "))
game4 = int(input("game 4 score : "))
game5 = int(input("game 5 score : "))

PointTotal = game1+game2+game3+game4+game5

print("Total of Points = " + str(PointTotal))
average = PointTotal/5
print("Average of points = " + str(average))