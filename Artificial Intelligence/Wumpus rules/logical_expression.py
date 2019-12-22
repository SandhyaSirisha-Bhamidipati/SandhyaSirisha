import sys
from copy import copy

class logical_expression:
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    if expression == 0 or expression == None or expression == '':
        print('\nINVALID\n')
    elif expression.symbol[0]:
        sys.stdout.write('%s' % expression.symbol[0])
    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break
        if input_string[counter[0]] == ' ':
            counter[0] += 1
            continue
        elif input_string[counter[0]] == '(':
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break
        else:
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print(length)
            print(counter[0])
            print('\nUnexpected end of input.\n')
            return 0
        if input_string[counter[0]] == ' ':
            counter[0] += 1
            continue
        if input_string[counter[0]] == ')':
            counter[0] += 1
            return 1
        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    while True:
        if counter[0] >= len(input_string):
            break
        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1
        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break
        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])
    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0
    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0
    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0
    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    if not symbol:
        return 0
    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

import copy

def getSymbols(expression):
    symbols = []
    if expression.symbol[0]:
        symbols.append(expression.symbol[0])
    else:
        for subexpression in expression.subexpressions:
            for symbol in getSymbols(subexpression):
                if symbol not in symbols:
                    symbols.append(symbol)
    return symbols


def getModel(statement):
    model = {};
    for expression in statement.subexpressions:
        if expression.symbol[0]:
            model[expression.symbol[0]] = True
        elif expression.connective[0].lower() == 'not':
            if expression.subexpressions[0].symbol[0]:
                model[expression.subexpressions[0].symbol[0]] = False
    return model


def extendModel(model,symbol,value):
    newModel = copy.deepcopy(model)
    newModel[symbol] = value
    return newModel


def plTrue(statement,model):
    if statement.symbol[0]:
        return model[statement.symbol[0]]
    elif statement.connective[0].lower() == 'and':
        result = True
        for exp in statement.subexpressions:
            result = result and plTrue(exp,model)
        return result
    elif statement.connective[0].lower() == 'or':
        result = False
        for exp in statement.subexpressions:
            result = result or plTrue(exp,model)
        return result
    elif statement.connective[0].lower() == 'xor':
        result = False
        for exp in statement.subexpressions:
            isExpTrue = plTrue(exp,model)
            result = (result and not isExpTrue) or (not result and isExpTrue)
        return result
    elif statement.connective[0].lower() == 'if':
        left = statement.subexpressions[0]
        right = statement.subexpressions[1]
        isLeftTrue = plTrue(left,model)
        isRightTrue = plTrue(right,model)
        if( isLeftTrue and not isRightTrue ):
            return False
        else:
            return True
    elif statement.connective[0].lower() == 'iff':
        left = statement.subexpressions[0]
        right = statement.subexpressions[1]
        isLeftTrue = plTrue(left,model)
        isRightTrue = plTrue(right,model)
        if( isLeftTrue == isRightTrue ):
            return True
        else:
            return False
    elif statement.connective[0].lower() == 'not':
        return not plTrue(statement.subexpressions[0],model)


def check_true_false(knowledge_base, statement):
    model = getModel(knowledge_base)
    symbols = getSymbols(knowledge_base)
    for symbol in getSymbols(statement):
        symbols.append(symbol)
    for symbol in model:
        if symbol in symbols:
            symbols.remove(symbol)
    truthOfStatement = TTCheckAll(knowledge_base, statement, symbols, model)
    negation = logical_expression()
    negation.connective[0] = 'not'
    negation.subexpressions.append(statement)
    truthOfNegation = TTCheckAll(knowledge_base, negation, symbols, model)
    result = open("result.txt","w+")
    if truthOfStatement and not truthOfNegation:
        result.write("definitely true")
    elif not truthOfStatement and truthOfNegation:
        result.write("definitely false")
    elif not truthOfStatement and not truthOfNegation:
        result.write("possibly true, possibly false")
    elif truthOfStatement and truthOfNegation:
        result.write("both true and false")


def TTCheckAll(KB, statement, symbols, model):
    if not symbols:
        if plTrue(KB,model):
            return plTrue(statement, model)
        else:
            return True
    else:
        p = symbols.pop(0)
        return TTCheckAll(KB, statement, symbols, extend(model,p,True)) and TTCheckAll(KB, statement, symbols, extend(model,p,False))

def extend(model,symbol,value):
    model[symbol]=value
    return model