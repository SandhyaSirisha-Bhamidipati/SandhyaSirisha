import sys
from logical_expression import *


def main(argv):
    if len(argv) != 4:
        print('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0])
        sys.exit(0)

    try:
        input_file = open(argv[1], 'r')
    except:
        print('failed to open file %s' % argv[1])
        sys.exit(0)

    print('\nLoading wumpus rules...')
    knowledge_base = logical_expression()
    knowledge_base.connective = ['and']
    for line in input_file:
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    try:
        input_file = open(argv[2], 'r')
    except:
        print('failed to open file %s' % argv[2])
        sys.exit(0)

    print('Loading additional knowledge...')
    for line in input_file:
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # a mutable counter
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    print_expression(knowledge_base, '\n')

    try:
        input_file = open(argv[3], 'r')
    except:
        print('failed to open file %s' % argv[3])
        sys.exit(0)
    print('Loading statement...')
    statement = input_file.readline().rstrip('\r\n')
    input_file.close()

    statement = read_expression(statement)
    if not valid_expression(statement):
        sys.exit('invalid statement')

    print('\nChecking statement: ')
    print_expression(statement, '')

    check_true_false(knowledge_base, statement)

    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)