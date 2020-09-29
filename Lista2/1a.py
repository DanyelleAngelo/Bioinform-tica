import re
from Crypto.PublicKey.DSA import generate
#^[\w\n]*$

def generateMold(sequence):
    print("oii")
    dict ={"A":"T","T":"A","C":"G","G":"C"}
    regeX = re.compile("[ACTG\n]*")
    #match =  regeX.search(sequence)
    for match in regeX.finditer(sequence):
        start = match.start()
        end = match.end()
        mold = sequence[start:end]
        print(mold)
    #if mold:
    #    #for i in mold:
    #    #    print(i)
    return 3

def readFile():
    filename= "toxinsNCBI.fna"
    result = []
    regeX = re.compile("^[ACTG\n]*$")
    with open(filename, 'r') as fp:
        txt = fp.readlines()
        txt = "".join(txt)
        setSequences = re.split(regeX,txt)
        #for sequence in setSequences:
        #    mold = generateMold(sequence)
        for match in regeX.finditer(txt):
            start = match.start()
            end = match.end()
            mold = txt[start:end]
            print(start)
            print(end)
            #complementary = generateComplement(mold)
            #result.append(complementary)
    return result

def gravar(a):
    print(a)
#    filename = "toxins_3-5.fna"
#    with open(filename,"w") as fp:
#        for i  in a:
#            fp.write("%s \n" %(i))

def main():
    a = readFile()
    gravar(a)
    
if __name__ == "__main__":
    main()