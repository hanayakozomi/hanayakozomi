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
    
    parser = argparse.ArgumentParser(description="四则运算")
    parser.add_argument('-n', dest='number', type=int, required=True, help='生成题目的个数')
    parser.add_argument('-r', dest='range', type=int, required=True, help='数字范围')
    parser.add_argument('-e', dest='exercise', type=str, help='给定题目文件')
    parser.add_argument('-a', dest='answer', type=str, help='给定答案文件')
    parser.add_argument('-g', dest='grade', type=str, help='输出答案文件')
    args = parser.parse_args()
    #必须输入-r -n参数
    if args.exercise is None:
        args.exercise = os.path.join(os.getcwd(), 'Exercises.txt')
    if args.answer is None:
        args.answer = os.path.join(os.getcwd(), 'Answers.txt')
    if args.grade is None:
        args.grade = os.path.join(os.getcwd(), 'Grade.txt')
    print("Enter 'exit' to exit)")

    t = cal.Tree()
    u_answer = list()
    formula, s_answer = t.generateFoumula(args.range, args.number)
    filePutContent(formula, s_answer, args.exercise, args.answer)
    for i in range(args.number):
        print(formula[i], end='')
        answer = input()
        if answer == 'exit':
            sys.exit()
        u_answer.append(answer)

    correct, wrong = cal.Cal.judgeAnswer(u_answer, s_answer)
    print('Right index：', correct)
    print('Wrong index：', wrong)

    with open(args.grade, 'w+', encoding='utf-8') as f:
        f.write("{:<9}".format("Correct:") + str(len(correct)) + str(correct) + '\n')
        f.write("{:<9}".format("Wrong:") + str(len(wrong)) + str(wrong) + '\n')
