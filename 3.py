input = open('/usr/share/licenses/python/LICENSE', 'r')
line = input.readline()
L={}
while line!=' ': #Fixme:зацикливается на одной строке
    line=list(line) #Fixme:не делит на слова, сделать буквы маленькими
    for i in range (len(line)):
        if (line[i]=="." or line[i]=="," or line[i]=="/n" or line[i]=="!" or line[i]=="?"):
            line[i]=' '
            line = ''.join(line)
            if i not in L:
                L[line[i]]=1
            else:
                L[line[i]]+=1
            max=0
            for key in L:
                if L[key]>max:
                    max=L[key]
print (max)
