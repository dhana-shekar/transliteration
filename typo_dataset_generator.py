from butterfingers import butterfingers

with open(r"F:\sem 5\englishtokannada\proper nouns\names.txt") as f1:
    names = f1.read().splitlines() 
f=open(r"F:\sem 5\transliteration\dataset\names.txt",'w')

for x in names:
    
    count=50
    errors=[]
    while(count>0):
        errors.append(butterfingers.butterfinger(x))
        count-=1
    unique_errors=[*set(errors)]
    for i in unique_errors:
        f.write(i.lower()+","+x.upper()+"\n")
print("done")

f.close()
f1.close()
