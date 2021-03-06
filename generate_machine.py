import sys

def indent(depth):
    sys.stdout.write('    ' * depth)

def generate(patt):

    sys.stdout.write('''
// Given a permutation, determine if it contains an occurrence of the pattern %s
bool contains(int n, int *perm) {
''' % (''.join(map(str,patt)), ))

    if patt[0] == 1:
        indent(1)
        sys.stdout.write('int mn = n+1;\n')

    for at in range(len(patt)):
        idx = 0
        while patt[idx] != at+1:
            idx += 1

        l = idx-1
        while l >= 0 and patt[l] > patt[idx]:
            l -= 1

        r = idx+1
        while r < len(patt) and patt[r] > patt[idx]:
            r += 1

        indent(1)
        sys.stdout.write('for (int a%(i)d = %(l)s; a%(i)d <= %(r)s; ++a%(i)d)\n' % {
            'i': at,
            'l': (str(idx) if l == -1 else 'a%d+%d' % (patt[l]-1, idx-l)),
            'r': ('n-%d' % (len(patt)-idx) if r == len(patt) else 'a%d-%d' % (patt[r]-1,r-idx)),
        })

        if at == 0 and patt[at] == 1:
            indent(1)
            sys.stdout.write('if (perm[a%d] < mn && (mn = perm[a%d]))\n' % (at, at)) # The lazy assignment at the end assumes perm[i] > 0, which is true because our permutations are 1-based

        if at > 0:
            indent(1)
            sys.stdout.write('if (perm[a%d] < perm[a%d])\n' % (at-1,at))

    indent(2)
    sys.stdout.write('return true;\n')

    indent(1)
    sys.stdout.write('return false;\n')
    sys.stdout.write('}\n')

def main(argv):
    if len(argv) != 2:
        sys.stderr.write('usage: %s pattern\n' % (argv[0]))
        return 1

    # TODO: support patterns of length > 9
    patt = argv[1]
    n = len(patt)

    if list(sorted(patt)) != list(map(str, range(1,n+1))):
        sys.stderr.write('"%s" is not a valid pattern\n' % (patt,))
        return 1

    patt = list(map(int, patt))
    generate(patt)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

