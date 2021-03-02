def arithmetic_arranger(problems, answers = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    ans1 = ''
    ans2 = ''
    ans3 = ''
    ans4 = ''
    i = 0

    for sum in problems:
        i += 1
        
        sum = sum.split()

        num2 = sum.pop()
        symbol = sum.pop()
        num1 = sum.pop()

        try:
            int(num1)
        except:
            return "Error: Numbers must only contain digits."
        try:
            int(num2)
        except:
            return "Error: Numbers must only contain digits."

        if int(num1) > 9999 or int(num2) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        if symbol != '+':
            if symbol != '-':
                return "Error: Operator must be '+' or '-'."
        
        if symbol == '+':
            num1 = int(num1)
            num2 = int(num2)
            ans = num1 + num2
            ans = int(ans)
            
        elif symbol == '-':
            num1 = int(num1)
            num2 = int(num2)
            ans = num1 - num2
            ans = int(ans)
            
        num1 = str(num1)
        num2 = str(num2)
        dlen = len(max([num1, num2], key=len))

        if answers == False:
            ans1 += f"  {num1:>{dlen}}"
            ans2 += f"{symbol} {num2:>{dlen}}"
            ans3 += f"{'-'*(dlen+2):>{dlen}}"

        elif answers == True:            
            ans1 += f"  {num1:>{dlen}}"
            ans2 += f"{symbol} {num2:>{dlen}}"
            ans3 += f"{'-'*(dlen+2):>{dlen}}"
            if ans < 0: 
                ans4 += f" {ans:>{dlen}}"
            else:
                ans4 += f"  {ans:>{dlen}}"
        
        if i < len(problems):
            ans1 += f"    "
            ans2 += f"    "
            ans3 += f"    "
            ans4 += f"    "

    if answers == False:
        return f"{ans1}\n{ans2}\n{ans3}"

    if answers == True:
        return f"{ans1}\n{ans2}\n{ans3}\n{ans4}"