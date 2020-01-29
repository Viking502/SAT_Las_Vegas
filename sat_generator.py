from sat_variable import Variable
import random


def convert_hamilton_to_sat(self):
    cnf = list()
    # let every variable in sat have unique id
    # created with vertice.ident and step in time
    mult = len(self.vertice)

    for t in range(len(self.vertice)):
        cnf.append()
        new_c = len(cnf)
        for v in self.vertice:
            cnf[new_c].append(Variable(v.ident * mult + t))


def generate_random_sat(clause_num, var_num, var_per_clause_num):
    cnf = [[Variable(random.randint(0, var_num), bool(random.getrandbits(1))) for _ in range(var_per_clause_num)]
           for _ in range(clause_num)]

    return cnf
