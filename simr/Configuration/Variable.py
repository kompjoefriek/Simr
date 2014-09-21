"""
This file contains the class Variable, meant to encapsulate a given variable as configured.
variables can resolve values with variables in them
"""
__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

import re


class Variable:
    name = None
    value = None
    depends_name = []  # variable name this variable depends on
    depends_ref = []  # reference to all variables that depend on this variable

    def __init__(self, name, value):
        self.depends_name = []
        self.depends_ref = []
        if "%" in name:
            raise RuntimeError("Variable \"{}\" has % in its name!".format(name))
        else:
            self.name = name

        self.value = value

        if not self.value is None:
            if self.value.count('%') % 2 != 0:
                raise RuntimeWarning("Variable \"{}\" has an uneven count of % chars! (counted {})"
                                     .format(self.name, self.value.count('%')))
            else:
                matches = re.match(r".*%([^%]+)%.*", self.value)
                if not matches is None:
                    # remove duplicates and store
                    self.depends_name = list(set(matches.groups()))

    def check_references(self, variables):
        for variable in variables:
            if not self.name is None and not variable.depends_name is None:
                if self.name in variable.depends_name:
                    self.depends_ref.append(variable)

    def resolve(self, variables, call_chain):
        if self.name in call_chain:
            raise RuntimeError("Cyclic reference detected!")

        # add this class to the call chain to prevent it from being called again this loop0
        call_chain.append(self.name)

        # make copy so we can alter the original inside the loop
        depends_name_copy = self.depends_name

        if not self.value is None and not depends_name_copy is None:
            for dep_name in depends_name_copy:
                for variable in variables:
                    if dep_name == variable.name:
                        if len(variable.depends_name) == 0:
                            self.value = self.value.replace("%{}%".format(variable.name), variable.value)
                            self.depends_name.remove(dep_name)

        # if this variable is completely resolved, call all others that depend on this value
        if not self.depends_name is None and len(self.depends_name) == 0:
            for reference in self.depends_ref:
                reference.resolve(variables, call_chain)
                # self.depends_ref.clear()

    def __repr__(self):
        return "Variable {{\n  name:\"{}\",\n  value\"{}\",\n  depends_name: {},\n  refs: [{}]\n}}" \
            .format(self.name, self.value, self.depends_name, ",".join([x.name for x in self.depends_ref]))
