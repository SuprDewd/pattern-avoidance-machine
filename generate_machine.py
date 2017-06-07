import sys

def indent(depth):
    sys.stdout.write('    ' * depth)

def generate(patt):

    sys.stdout.write('''
// Given a permutation, determine if it contains an occurrence of the pattern %s
bool contains(int n, int *perm) {
''' % (''.join(map(str,patt)), ))

    # TODO: We can decide which order we fill in the inverse permutation, maybe we should build it from left to right?

    def rec(at, depth):
        if at == len(patt):
            indent(depth+1)
            sys.stdout.write('return true;\n')
            return

        idx = 0
        while patt[idx] != at+1:
            idx += 1

        l = idx-1
        while l >= 0 and patt[l] > patt[idx]:
            l -= 1

        r = idx+1
        while r < len(patt) and patt[r] > patt[idx]:
            r += 1

        indent(depth)
        sys.stdout.write('for (int a%(i)d = %(l)s; a%(i)d <= %(r)s; ++a%(i)d)\n' % {
            'i': at,
            'l': (str(idx) if l == -1 else 'a%d+%d' % (patt[l]-1, idx-l)),
            'r': ('n-%d' % (len(patt)-idx) if r == len(patt) else 'a%d-%d' % (patt[r]-1,r-idx)),
            })

        if at > 0:
            indent(depth)
            sys.stdout.write('if (perm[a%d] < perm[a%d])\n' % (at-1,at))

        rec(at+1, depth)

        # indent(depth)
        # sys.stdout.write('}\n')


    rec(0,1)

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


if __name__ == '__main__':
    sys.exit(main(sys.argv))

