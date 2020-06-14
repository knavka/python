def countChar (string, char):
    count=0
    for i in range(0, len(string)):
        if string[i]==char:
            count += 1
    return count

print ("This is symbol frequency counter")
print ("String:")
string=input()
print ("Symbol:")
char=input()
print ("There are "+str(countChar (string, char))+" \""+char+"\"")



