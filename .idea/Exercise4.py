def list_benefits():
 return benefit_list


benefit_list = ["More organized code", "More readable code", "Easier code reuse",
                "Allowing programmers to share and connect code together"]
print(benefit_list)


def build_sentence(benefit):
 return benefit + " is a benefit of functions!"
list_of_benefits = list_benefits()

print(build_sentence(list_of_benefits[0]))
print(build_sentence(list_of_benefits[1]))
print(build_sentence(list_of_benefits[2]))
print(build_sentence(list_of_benefits[3]))

