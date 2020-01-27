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
        for c_num in range(self.cnf):
            if not self.test_valuable(c_num):
                self.fix_clause(c_num)

    def test_valuable(self, c_num):
        for v in self.cnf[c_num]:
            if self.value[v.ident] and not v.negation \
                    or not self.value[v.ident] and v.negation:
                return True
        return False

    def fix_clause(self, c_num):
        # fix clause
        while not self.test_valuable(c_num):
            changed = set()
            for v in self.cnf[c_num]:
                base = self.value[v.ident]
                # rand values
                self.value[v.ident] = bool(random.getrandbits(1))
                if base != self.value[v.ident]:
                    changed.add(v.ident)
        for c_num, clause in enumerate(self.cnf):
            # if changed is in clause fix clause
            pass


if __name__ == '__main__':
    sat = [
        [Variable(0), Variable(2, True), Variable(3)],
        [Variable(1), Variable(3, True), Variable(0, True)]
    ]

    agent = Solver(sat)

    print(agent.test_valuable(0))
    print(agent.test_valuable(1))