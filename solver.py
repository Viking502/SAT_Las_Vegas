import random
import time
from sat_variable import Variable

from sat_generator import generate_random_sat


class Solver:

    def __init__(self, problem, time_limit):
        self.cnf = problem
        self.begin_time = 0
        self.time_limit = time_limit
        #  IT WILL BE GOOD SOLUTION IN CASE WE DON'T WANT TO INDEX VARIABLES
        # self.variable = set()
        # for clause in self.cnf:
        #     for v in clause:
        #         self.variable.add(v.ident)

        max_id = 0
        for clause in self.cnf:
            for v in clause:
                max_id = max(v.ident, max_id)

        # initialize random
        self.value = [bool(random.getrandbits(1)) for _ in range(max_id + 1)]
        self.print_cnf()

    def solve(self):
        self.begin_time = time.time()
        for c_num in range(len(self.cnf)):
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

        changed = set()
        while not self.test_valuable(c_num):
            changed.clear()
            for v in self.cnf[c_num]:
                base = self.value[v.ident]
                # rand values
                self.value[v.ident] = bool(random.getrandbits(1))
                if base != self.value[v.ident]:
                    changed.add(v.ident)
        for c_num, clause in enumerate(self.cnf):
            # if changed is in clause fix clause
            for v in clause:
                for s in changed:
                    if v.ident == s:
                        # print(time.time() - self.begin_time)
                        if time.time() - self.begin_time > 100:
                            return
                        self.fix_clause(c_num)

    def validate_result(self):
        is_valid = True
        c_num = 0
        while c_num < len(self.cnf) and is_valid:
            is_valid = self.test_valuable(c_num)
            c_num += 1
        return is_valid

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
        print()

    def print_result(self):
        print('[', end='')
        first_flag = True
        for id, val in enumerate(self.value):
            if first_flag:
                first_flag = False
            else:
                print(', ', end='')
            print(id, '-', val, end='')
        print(']')


if __name__ == '__main__':
    sample1 = [
        [Variable(0), Variable(2, True), Variable(3)],
        [Variable(4), Variable(3, True), Variable(0, True)],
        [Variable(1, True), Variable(4), Variable(3, True)],
        [Variable(4, True), Variable(2), Variable(1)]
    ]

    sample2 = generate_random_sat(102, 8, 5)

    sample3 = [
        [Variable(0)],
        [Variable(0, True)]
    ]

    agent = Solver(sample2, 100)
    agent.solve()
    if agent.validate_result():
        agent.print_result()
    else:
        print('Wrong answer')
