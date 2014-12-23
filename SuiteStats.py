__author__ = 'Prasad'

__author__ = 'Prasad'


from robot.result.executionresult import Result
from robot.result.visitor import ResultVisitor
from robot.result import ExecutionResult
import getopt
import sys

class ResVisitor(ResultVisitor):

    def visit_suite_statistics(self, stats):
        opStr=stats.stat.name+" PASSED : "+str(stats.stat.passed)+" FAILED : "+str(stats.stat.failed)
        print '{:<10}'.format(opStr)

opFile=None
usage = """
    SuiteStats.py -o <path to output.xml>
    SuiteStats.py -h
"""

def main():
    global opFile
    opts,args=getopt.getopt(sys.argv[1:],"o:h")
    for o,a in opts:
        if o=="-o":
            opFile=a
        if o=="-h":
            print usage
            exit(0)

main()
res=ExecutionResult(opFile)
statistics=res.statistics
retSuites=statistics.suite.suites
for st in retSuites:
    st.visit(ResVisitor())
