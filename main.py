from butterfingers import errorcheck_engvocab
import eng_to_ipa as ipa


checker_eng_cocab=errorcheck_engvocab.SpellChecker(r"F:\sem 5\transliteration\dataset\eng_vocab.txt")
checker_pronouns=errorcheck_engvocab.SpellChecker(r"F:\sem 5\transliteration\dataset\indian_names.txt")



word=input("enter a name or word or pronouns\n")


candidate_eng_vocab=checker_eng_cocab.check(word)
candidate_pronouns=checker_pronouns.check(word)

potential=(candidate_eng_vocab+candidate_pronouns)
print(potential)

ipa_form=[]
for x in potential:
    ipa_form.append(ipa.convert(x[0]))

print(ipa_form)


file1 = open(r"F:\sem 5\transliteration\dataset\indian_names, "a") 
file1.write("\nword")
file1.close()