from sat_variable import Variable


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
