source = input("Enter your X_COORDINATE and Y_COORDINATE DIRECTION:  ")
destination = input("Enter X_COORDINATE and Y_COORDINATE: ")
try:
    sourceList = source.split(" ")
    destinationList = destination.split(" ")
    rowDataFirst = int(sourceList[0].replace(',', ''))
    direction = sourceList[2]
    rowDataSecond = int(sourceList[1])
    colDataFirst = int(destinationList[0].replace(',', ''))
    colDataSecond = int(destinationList[1])
    if (rowDataFirst < 6 or rowDataFirst > 0) and (rowDataSecond < 6 or rowDataSecond > 0) and (colDataFirst < 6 or colDataFirst > 0) and (colDataSecond < 6 or colDataSecond > 0) and (direction == 's' or direction == 'S' or direction == 'n' or direction == 'N' or direction == 'e' or direction == 'E' or direction == 'w' or direction == 'W'):
        totalPowerConsume = 10 * (abs(colDataFirst - rowDataFirst) + abs(colDataSecond - rowDataSecond))
        if colDataFirst > rowDataFirst:
            if direction == 'N' or direction == 'n':
                if colDataSecond > rowDataSecond or colDataSecond == rowDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
                if rowDataSecond > colDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 10)
            if direction == 'S' or direction == 's':
                if colDataSecond > rowDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 10)
                if rowDataSecond > colDataSecond or colDataSecond == rowDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
            if direction == 'W' or direction == 'w':
                remainingPower = 200 - (totalPowerConsume + 10)
            if direction == 'E' or direction == 'e':
                if colDataSecond > rowDataSecond or rowDataSecond > colDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
                if colDataSecond == rowDataSecond:
                    remainingPower = 200 - totalPowerConsume
        if colDataFirst == rowDataFirst:
            if rowDataSecond == colDataSecond:
                    remainingPower = 200
            else:
                if direction == 'N' or direction == 'n':
                    if colDataSecond > rowDataSecond:
                        remainingPower = 200 - totalPowerConsume
                    if rowDataSecond > colDataSecond:
                        remainingPower = 200 - (totalPowerConsume + 10)
                if direction == 'S' or direction == 's':
                    if colDataSecond > rowDataSecond:
                        remainingPower = 200 - (totalPowerConsume + 10) 
                    if rowDataSecond > colDataSecond:
                        remainingPower = 200 - totalPowerConsume
                if direction == 'W' or direction == 'w' or direction == 'E' or direction == 'e':
                    remainingPower = 200 - (totalPowerConsume + 5)
        if rowDataFirst > colDataFirst:
            if direction == 'N' or direction == 'n':
                if rowDataSecond > colDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 10)
                if colDataSecond > rowDataSecond or rowDataSecond == colDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
            if direction == 'S' or direction == 's':
                if rowDataSecond > colDataSecond or rowDataSecond == colDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
                if colDataSecond > rowDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 10)
            if direction == 'W' or direction == 'w':
                if rowDataSecond > colDataSecond or colDataSecond > rowDataSecond:
                    remainingPower = 200 - (totalPowerConsume + 5)
                if rowDataSecond == colDataSecond:
                    remainingPower = 200 - totalPowerConsume
            if direction == 'E' or direction == 'e':
                remainingPower = 200 - (totalPowerConsume + 10)
        print(f"The output should be remaining power G-Man has after taking the shortest path. POWER {remainingPower}")
    else:
        print("X,Y cordination must be 0 to 6 and direction must be n, N ,s, S, w, W, e or E")
except Exception as e:
    print("please follow below input example")
    print("Enter your X_COORDINATE and Y_COORDINATE DIRECTION:  1, 1 N or 1, 1 n here N or n for direction")
    print("Enter X_COORDINATE and Y_COORDINATE: 6, 6")