import re


"""
This file contains the class Variable, meant to encapsulate a given variable as configured.
variables can resolve values with variables in them
"""
__author__ = 'Sander Krause <sanderkrause@gmail.com>'
__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


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
        self.depends_name = Variable.get_dependency_list(self.name, self.value)

    @staticmethod
    def get_dependency_list(name, value):
        if value is not None:
            if value.count('%') % 2 != 0:
                raise RuntimeWarning("Variable \"{}\" has an uneven count of % chars! (counted {})"
                                     .format(name, value.count('%')))
            else:
                matches = re.findall(r"%([^%]+)%", value)
                if matches is not None:
                    # remove duplicates and store
                    return list(set(matches))
        return None

    @staticmethod
    def resolve_value(variables, value, name="(task)"):
        dependency_list = Variable.get_dependency_list(name, value)
        for dep_name in dependency_list:
            for variable in variables:
                if dep_name == variable.name:
                    value = value.replace("%{}%".format(variable.name), variable.value)
        return value

    def check_references(self, variables):
        for variable in variables:
            if self.name is not None and variable.depends_name is not None:
                if self.name in variable.depends_name:
                    self.depends_ref.append(variable)

    def resolve(self, variables, call_chain):
        if self.name in call_chain:
            raise RuntimeError("Cyclic reference detected!")

        # add this class to the call chain to prevent it from being called again this loop
        call_chain.append(self.name)

        # make copy so we can alter the original inside the loop
        depends_name_copy = self.depends_name

        if self.value is not None and depends_name_copy is not None:
            for dep_name in depends_name_copy:
                for variable in variables:
                    if dep_name == variable.name and len(variable.depends_name) == 0:
                        self.value = self.value.replace("%{}%".format(variable.name), variable.value)
                        self.depends_name.remove(dep_name)

        # if this variable is completely resolved, call all others that depend on this value
        if self.depends_name is not None and len(self.depends_name) == 0:
            call_chain.remove(self.name)
            for reference in self.depends_ref:
                reference.resolve(variables, call_chain)
                # self.depends_ref.clear()

    def __repr__(self):
        return "Variable {{\n  name:\"{}\",\n  value\"{}\",\n  depends_name: {},\n  refs: [{}]\n}}" \
            .format(self.name, self.value, self.depends_name, ",".join([x.name for x in self.depends_ref]))
