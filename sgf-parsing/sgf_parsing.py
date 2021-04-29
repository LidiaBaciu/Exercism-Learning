import re

class SgfTree:

    node_regex = re.compile(r"(;?([A-Z])(\[[a-zA-Z]{,2}\])+)")
    node_regex2 = re.compile(r"(;?([A-Z])\[[a-zA-Z\\\n\s\]\[]+\]+)")
    value_regex = re.compile(r"\[([a-zA-Z])\]")
    value_regex2 = re.compile(r"\[([a-zA-Z\\\n\s\]\[]+)\]")

    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if input_string == '(;)':
        return SgfTree()
    groups = SgfTree.node_regex.findall(input_string)
    if not groups:
        groups = SgfTree.node_regex2.findall(input_string)
        if not groups:
            raise ValueError("Malformed SGF Tree.")
    sgf_tree = SgfTree()
    for group in groups:
        vals = SgfTree.value_regex.findall(group[0])
        if not vals:
            vals = SgfTree.value_regex2.findall(group[0])
        vals = list(map(lambda val: val.replace('\\', '').replace('\t', ' '), vals))
        if group[0][0] == ';':
            if not sgf_tree.properties:
                sgf_tree.properties[group[1]] = vals
            else:
                sgf_tree.children.append(SgfTree(properties={group[1]: vals}))
        else:
            sgf_tree.properties[group[1]] = vals
    return sgf_tree