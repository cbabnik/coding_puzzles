# String Formatting
print("%s %s" % (1, 2))

# Classes
class C:
    def __init__(self, param):
        self.param = param

    def f(self):
        print("hello world! %s" % self.param)

# Regular Expressions
import re
re.match(r"", "abcd")
re.search(r"", "abcd")
re.findall(r"", "abcd")
re.sub(r"", "replacement", "abcd")

pattern = r""
regex = re.compile(pattern)
regex.match("abcd")

re.split(r'\\n|\\r|\\t| ', '')

# String Methods
"".strip()
"".count("ab")
import string
table = "".maketrans("abc", "cba")
"".translate(table)

# Array methods
# * Note that string is just a string array of size 1 strings
sorted("")
[].count("a")
[].extend([])
[].remove("a")
[].sort() # in place
[].copy()

# Dict (notably diff between 2.7 and 3.5)
# NOTE: Dict's are implemented as hash tables and have O(1) insertion, lookup
d = {}
d.copy()
d.get("a")
d["a"] = "b"
d.keys()
d.values()
d.items() # (key, value) pairs

# Sets
A = set()
B = {1,2,3}
A | B
A & B
A - B
A ^ B
A <= B

# Get Prepped with search algorithms
#
# # ADD THESE
# # some efficient data structures and sorts
#     # collections.deque
#     # collections.OrderedDict
#     # collections.Counter
#     # collections.ChainMap
# # combinatorics
#     # math.factorial
#     # define own countPermutations & countCombinations functions
#     # itertools.permutations
#     # itertools.combinations
# # searching
#     # dijkstras
#     # astar
#     # DFS
#     # BFS
#
# # lookup conversions between: lists, maps, sets
# # some sort of pipeline for checking against t1 solutions

# source for primes https://primes.utm.edu/lists/small/small2.html
