from fractions import Fraction


def getNumAndOp(formula):
    numList = list()
    opList = list()
    for item in formula:
        if isinstance(item, int) or isinstance(item, Fraction):
            numList.append(item)
        elif item == ' ＋ ':
            opList.append(item)
        elif item == ' － ':
            opList.append(item)
        elif item == ' × ':
            opList.append(item)
        elif item == ' ÷ ':
            opList.append(item)
    return numList, opList


def check(formula, form):
    formulaNewList, formulaOldList = getNumAndOp(formula)
    if ' ＋ ' in formulaOldList or ' × ' in formulaOldList:
        newList, oldList = getNumAndOp(form)
        if formulaNewList.sort() == newList.sort():
            return True
    else:
        return False



