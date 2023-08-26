import random

def probability(file, questions):
    f = [int(i) for i in open(file, "r").read().splitlines()]
    q = [i+1 for i in range(len(f))]
    if not all(occurence ==0 for occurence in f):
        # Bubble sort f
        for i in range(len(f)):
            for n in range(len(f)-1):
                if f[i] < f[n]:
                    f[i], f[n] = f[n], f[i]
                    q[i], q[n] = q[n], q[i]
        revf = f[::-1]
        r = []
        for i in range(len(q)):
            for n in range(revf[i]):
                r.append(q[i])
        qnum = []
        for i in range(questions):
            chosen = random.choice(r)
            qnum.append(chosen)
            f[q.index(chosen)] += 1
        with open(file, "w") as file:
            for i in range(len(q)):
                file.write(f"{f[q.index(i+1)]}\n")
    else:
        #Select randomly
        qnum = []
        for i in range(questions):
            chosen = random.randint(1, len(f))
            qnum.append(chosen)
            f[q.index(chosen)] += 1
        with open(file, "w") as file:
            for i in range(len(q)):
                file.write(f"{f[q.index(i+1)]}\n")
    return ', '.join(str(i) for i in qnum)