"""

Word Count UNIX

"""

def wc(*filenames):
    results = {}
    for filename in filenames:
        chars = 0
        words = 0
        lines = 0
        try:
            with open(filename) as fh:
                for line in fh:
                    lines += 1
                    words += len(line.split())
                    chars += len(line)
            results[filename] = {
                'lines': lines,
                'words': words,
                'chars': chars,
            }
        except Exception as err:
            print(err)
    return results
 
 
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        exit("Usage: {} FILENAMEs".format(sys.argv[0]))
    results = wc(*sys.argv[1:])
    totals = {
        'lines': 0,
        'words': 0,
        'chars': 0,
    }
    for filename in results:
        res = results[filename]
        print("{} {} {} {}".format(res['lines'], res['words'], res['chars'], filename))
        for k in res:
            totals[k] += res[k]
    print("{} {} {} {}".format(totals['lines'], totals['words'], totals['chars'], 'total'))