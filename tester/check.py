import sys
from permuta import *
from itertools import permutations
from subprocess import Popen, PIPE
import time

def doit(n1,n2,k1,k2):

    for n in range(n1,n2+1):
        for patt in permutations(list(range(1,n+1))):

            p = Popen('python ../generate_machine.py ' + ''.join(map(str, patt)), shell=True, stdout=PIPE, stdin=PIPE)
            contains = p.stdout.read().decode('utf-8')
            p.wait()

            with open('template.cpp', 'r') as f:
                template = f.read()

            with open('tmp.cpp', 'w') as f:
                f.write(template % {'contains': contains})

            p = Popen('g++ -Wall -O3 tmp.cpp -o tmp', shell=True)
            p.wait()

            for k in range(k1,k2+1):

                start = time.time()

                arr = []
                q = Perm([ x-1 for x in patt ])
                for p in permutations(list(range(k))):
                    if Perm(p).avoids(q):
                        arr.append(' '.join([ str(y+1) for y in p ]))

                end = time.time()
                pu = end - start

                start = time.time()
                p = Popen('./tmp %d' % k, shell=True, stdout=PIPE, stdin=PIPE)
                p.stdin.write(('%d\n' % k).encode('utf-8'))
                p.stdin.close()
                out = p.stdout.read().decode('utf-8')
                end = time.time()

                me = end - start
                print('%0.3f %0.3f %d %s' % (pu, me, k, patt))

                out2 = ''.join([ '%s\n' % x for x in arr ])
                assert out == out2

print('# patterns of length 1-4, validity')
doit(1,4,0,8)
print('# patterns of length 1-4, benchmark')
doit(1,4,9,9)

print('# patterns of length 5, validity')
doit(5,5,0,8)
print('# patterns of length 5, benchmark')
doit(5,5,9,9)

