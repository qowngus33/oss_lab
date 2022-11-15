import decimal
import random
import time
import glob
import fnmatch

if __name__ == "__main__":
    print("DECIMAL")
    print(decimal.getcontext()) # rounding=decimal.ROUND_HALF_EVEN
    print(decimal.Decimal(3.5).quantize(1, decimal.ROUND_HALF_UP))
    print(decimal.Decimal(4.5).quantize(1, decimal.ROUND_HALF_UP))

    print("\nRANDOM")
    round2 = lambda x: int(x + 0.5)
    print([round2(random.uniform(0, 10)) for i in range(10)])
    print([round2(random.gauss(5, 1)) for i in range(10)])

    print("\nTIME")
    print(time.time())
    print(time.process_time())
    print(time.thread_time())
    print(time.localtime())
    print(time.gmtime())
    print(time.ctime())
    start = time.time()
    time.sleep(0.5)
    elapse = time.time() - start
    print(elapse)

    print("\nGLOB")
    print(glob.glob('*.py'))
    print(glob.glob('line_fitting_*.py'))

    print("\nFNMATCH")
    profs = ['My name is Choi and my E-mail is sunglok@seoultech.ac.kr.',
             'My name is Kim and my e-mail address is jindae.kim@seoultech.ac.kr.']
    print([fnmatch.fnmatch(prof, 'e-mail') for prof in profs])
    print([fnmatch.fnmatch(prof, '*e-mail*') for prof in profs])
    print([fnmatch.fnmatchcase(prof, '*e-mail*') for prof in profs])
    print([fnmatch.fnmatchcase(prof, '*[Ee]-mail*') for prof in profs])
    print(fnmatch.filter(profs, '*e-mail*'))
    print(fnmatch.filter(profs, '*Ch?i*'))