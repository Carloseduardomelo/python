
string1 = "abc"
string2 = "xyz"


nova_string1 = string1[0] + string1[1] + string2[-1]
nova_string2 = string2[0] + string2[1] + string1[-1]


print(nova_string1, nova_string2)