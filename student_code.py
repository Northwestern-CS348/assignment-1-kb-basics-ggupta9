import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        isFact = isinstance(fact, Fact)
        if isFact == True and fact not in self.facts:
            self.facts.append(fact)
            print("Asserting {!r}".format(fact))
        else:
            print("Could not assert")

    def kb_ask(self, fact):
        print("Asking {!r}".format(fact))
        bindings_list = ListOfBindings()
        for i in self.facts:
            j = match(fact.statement, i.statement)
            if isinstance(j, Bindings):
                bindings_list.add_bindings(j)
        return bindings_list
