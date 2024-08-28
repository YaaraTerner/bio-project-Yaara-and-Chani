from itertools import product


def is_monotonic(regulation_condition):
    """
    This function checks whether a regulation_condition is monotonic
    :param regulation_condition: a list of the values
    :return: True or False
    """
    # go through the regulation conditions
    for i in range(9):
        reg_i = regulation_condition[i]

        if reg_i[0] == 'ON':
            for j in range(9):
                reg_j = regulation_condition[j]
                # check if the num of activators is bigger from the num of activators in the current reg ('ON')
                # and the num of repressors is smaller from the num of repressors in the current reg ('ON')
                if reg_j[1] >= reg_i[1] and reg_j[2] <= reg_i[2]:
                    if reg_j[0] == 'OFF':  # monotonic is broken
                        return False

        if reg_i[0] == 'OFF':
            for j in range(9):
                reg_j = regulation_condition[j]
                # check if the num of activators is smaller from the num of activators in the current reg ('OFF')
                # and the num of repressors is bigger from the num of repressors in the current reg ('OFF')
                if reg_j[1] <= reg_i[1] and reg_j[2] >= reg_i[2]:
                    if reg_j[0] == 'ON':  # monotonic is broken
                        return False
    return True


def main():
    regulation_condition = []
    states = ['ON', 'OFF']
    combinations = list(product(states, repeat=9))  # creates all the 2^9 possibilities for a function
    # generating all possible functions
    for comb in combinations:
        index = 0
        line = []
        for i in range(3):
            for j in range(3):
                line.append([comb[index], j, i])
                index += 1
        regulation_condition.append(line)
    # remove functions where all activators are turned on and all repressors are turned off and the function is 'OFF'
    # and functions where all activators are turned off and all repressors are turned on and the function is 'ON'
    for reg in regulation_condition.copy():
        if reg[2][0] != 'ON':
            regulation_condition.remove(reg)
        elif reg[6][0] != 'OFF':
            regulation_condition.remove(reg)

    # find the monotonic conditions
    monotonic_conditions = []
    for condition in regulation_condition:
        if is_monotonic(condition):
            monotonic_conditions.append(condition)

    print("Number of monotonic conditions: ", len(monotonic_conditions))
    print("The monotonic conditions:")
    for m in monotonic_conditions:
        print(m)


if __name__ == '__main__':
    main()
