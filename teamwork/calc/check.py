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
    f_nlist, f_olist = getNumAndOp(formula)
    if ' ＋ ' in f_olist or ' × ' in f_olist:
        n_list, o_list = getNumAndOp(form)
        if f_nlist.sort() == n_list.sort():
            return True
    else:
        return False



