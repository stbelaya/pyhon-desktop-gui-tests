from comtypes.client import CreateObject
import os
import getopt
import sys
import random
import string

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
#    getopt.usage()
    sys.exit(2)

n = 10
f = "data/groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = (string.ascii_letters + string.digits + " "*10 + string.punctuation)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [random_string("group", 10) for i in range(n)]


# project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = CreateObject("Excel.Application")
xl.Visible = 0
wb = xl.Workbooks.Add()
for i in range(n):
    xl.Range[f"A{i+1}"].Value[()] = testdata[i]
wb.SaveAs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f))
xl.Quit()
