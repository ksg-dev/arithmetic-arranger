def get_answers(probs):
  probs = " ".join(probs)
  probs = probs.split()
  top, op, bot = (int(probs[0]), probs[1], int(probs[2]))
  if op == '+':
    answer = top + bot
    return (answer)
  elif op == '-':
    answer = top - bot
    return (answer)


def error_check(list):
  ops = ['+', '-']
  if len(list) > 5:
    return ("Error: Too many problems.")
  for prob in list:
    prob1 = prob.split()
    for i in prob1:
      if len(i) > 4:
        return ("Error: Numbers cannot be more than four digits.")
      if prob1[1] not in ops:
        return ("Error: Operator must be '+' or '-'.")
      if prob1[0].isdigit() is False or prob1[2].isdigit() is False:
        return ("Error: Numbers must only contain digits.")
    else:
      return ("")

def demo(lst):
  new_list1 = []
  for i in lst:
    new = i.split(' ')
    new_list1.append(new)
  probs = new_list1
  return probs

def arithmetic_arranger(lst, answers=False):
  if error_check(lst) != "":
    return (error_check(lst))
  else:
    first_line = ""
    second_line = ""
    lines = ""
    solution = ""

    arr_lst = demo(lst)
    colWidths = [0] * len(arr_lst)
    for i in range(len(arr_lst)):
      for j in range(len(arr_lst[i])):
        if (len(arr_lst[i][j]) + 2) > colWidths[i]:
          colWidths[i] = len(arr_lst[i][j]) + 2
      solutions = str(get_answers(arr_lst[i]))
      arr_lst[i].append(str(solutions))
      

      first_aligned = str(arr_lst[i][0]).rjust(colWidths[i])
      sec_aligned = str(arr_lst[i][1]).ljust(1) + str(arr_lst[i][2]).rjust(colWidths[i]-1)
      sum_aligned = str(arr_lst[i][3]).rjust(colWidths[i])

      prob_no = len(arr_lst) -1

      line = '-' * colWidths[i]



      if i == prob_no:
        first_line += first_aligned
        second_line += sec_aligned
        lines += line
        solution += sum_aligned

      else:
        first_line += first_aligned + "    "
        second_line += sec_aligned + "    "
        lines += line + "    "
        solution += sum_aligned + "    "

  if answers is True:
    return(f'{first_line}\n{second_line}\n{lines}\n{solution}')

  else:
    return(f'{first_line}\n{second_line}\n{lines}')


