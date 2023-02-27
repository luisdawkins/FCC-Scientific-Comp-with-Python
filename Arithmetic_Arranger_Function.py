def arithmetic_arranger(problems, displayResult):
    #If problems exceed 5 return error
    if len(problems) > 5:
        return "Error: Too many problems."

    topTier = ""
    bottomTier = ""
    operator = ""
    lines = ""
    totals = ""
    finalResult = ""

    for n in problems:
        #Recieve input
        topNumber = n.split()[0]
        bottomNumber = n.split()[2]
        op = n.split()[1]
        numberOfLines = 0
        workingTopTier = ""
        workingBottomTier = ""
        workingLines = ""
        workingTotals = ""
        workingResult= ""
        calculatedTotals = 0


        #print(topNumber, bottomNumber, op)

        #Validate input data
        #If problem is not "+" or "-" return error
        if str(op) != "+" and str(op) != "-":
            return "Error must be operator"

        #If one operand is not a digit return error
        if not topNumber.isdigit() or not bottomNumber.isdigit():
            return "Error: Numbers must only contain digits."

        #If one operand is more than four digits return error
        if len(topNumber) > 4 or len(bottomNumber) > 4:
            return "Error: Numbers cannot be more than four digits."

        topNumber = int(topNumber)
        bottomNumber = int(bottomNumber)
        operator = op

        #Process data
        if operator == "+":
            calculatedTotals = topNumber + bottomNumber

        if operator == "-":
            calculatedTotals = topNumber - bottomNumber

        #Format data for outputing
        #Determine number of lines
        if topNumber > bottomNumber:
            numberOfLines = len(str(topNumber)) + 2
        else:
            numberOfLines = len(str(bottomNumber)) + 2

        workingTopTier = f"{topNumber:>{numberOfLines+1}}"
        workingBottomTier = f"{operator}{bottomNumber:>{numberOfLines-1}}"
        workingLines = numberOfLines*"_"
        workingTotals = f"{calculatedTotals:>{numberOfLines}}"

        #Process topTier
        if topTier == "":
            topTier = workingTopTier
        else:
            topTier = topTier + "   " + workingTopTier

        #Process bottomTier
        if bottomTier == "":
            bottomTier = workingBottomTier
        else:
            bottomTier = bottomTier + "    " + workingBottomTier

        #Process lines
        if lines == "":
            lines = workingLines
        else:
            lines = lines + "    " + workingLines

        #Process totals
        if totals == "":
            totals = workingTotals
        else:
            totals = totals + "    " + workingTotals

        finalResult = f"{topTier} \n {bottomTier}\n {lines} \n {totals}"

    if displayResult:
        return finalResult

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
#print(arithmetic_arranger(["32 + 69","32 + 698","32 + 698","32 + 698","32 + 698"]))
