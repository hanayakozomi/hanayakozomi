import os
import sys
import argparse
import cal


def filePutContent(expr_set, ans_set, exp_file, ans_file):
    index = 0
    with open(exp_file, 'w+', encoding='utf-8') as ef, \
            open(ans_file, 'w+', encoding='utf-8') as af:
        ef.write('题号\n')
        af.write('题号    ' + '答案' + '\n')
        for ans, content in zip(ans_set, expr_set):
            index += 1
            ef.write(str(index) + '.  ' + content + '\n')
            af.write("{:<5d}".format(index) + '    ' + str(ans) + '\n')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="FourArithemetic")
    parser.add_argument('-n', dest='number', type=int, required=True, help='Number of generated questions') #-n的判断
    parser.add_argument('-r', dest='range', type=int, required=True, help='Digital range')  #-r的判断
    parser.add_argument('-e', dest='exercise', type=str, help='Given title file')
    parser.add_argument('-a', dest='answer', type=str, help='Given answers file')
    parser.add_argument('-g', dest='grade', type=str, help='Output answer file')
    args = parser.parse_args()

    if args.exercise is None:
        args.exercise = os.path.join(os.getcwd(), 'Exercises.txt')
    if args.answer is None:
        args.answer = os.path.join(os.getcwd(), 'Answers.txt')
    if args.grade is None:
        args.grade = os.path.join(os.getcwd(), 'Grade.txt')
    print("Enter 'exit' to exit)")

    t = cal.Tree()
    ans = list()
    formula, s_answer = t.generateFoumula(args.range, args.number)
    filePutContent(formula, s_answer, args.exercise, args.answer)
    for i in range(args.number):
        print(formula[i], end='')
        answer = input()
        if answer == 'exit':
            sys.exit()
        ans.append(answer)

    correct, wrong = cal.Cal.judgeAnswer(ans, s_answer)
    print('Right index：', correct)
    print('Wrong index：', wrong)

    with open(args.grade, 'w+', encoding='utf-8') as f:
        f.write("{:<9}".format("Correct:") + str(len(correct)) + str(correct) + '\n')
        f.write("{:<9}".format("Wrong:") + str(len(wrong)) + str(wrong) + '\n')
