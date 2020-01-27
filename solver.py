import random


class Variable:

    def __init__(self, id, neg=False):
        self.ident = id
        self.negation = neg
        self.value = False

    def print(self):
        if self.negation:
            print('~', end='')
        print(self.ident, end=' ')


class Solver:

    def __init__(self, problem):
        self.cnf = problem

        self.variable = set()
        for clause in self.cnf:
            for v in clause:
                self.variable.add(v.ident)

        # initialize random
        self.value = [bool(random.getrandbits(1)) for _ in self.variable]
        self.print_cnf()

        print()
        print(self.value)

    def print_cnf(self):

        first_clause_flag = True
        for clause in self.cnf:
            if first_clause_flag:
                first_clause_flag = False
            else:
                print(' and ', end='')
            print('(', end='')
            first_var_flag = True
            for v in clause:
                if first_var_flag:
                    first_var_flag = False
                else:
                    print(' or ', end='')
                v.print()
            print(')', end='')

    def solve(self):
        for c_num, clause in enumerate(self.cnf):
            clause_value = False
            for v in clause:
                if self.value[v.ident] and not v.negation \
                        or not self.value[v.ident] and v.negation:
                    clause_value = True
            if not clause_value:
                self.fix_clause(c_num)

    def fix_clause(self, c_num):
        # fix clause
        pass


if __name__ == '__main__':
    sat = [
        [Variable(1), Variable(2, True), Variable(3)],
        [Variable(1), Variable(3, True), Variable(4)]
    ]

    agent = Solver(sat)
