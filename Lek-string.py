firstName = "Simon"
middleName = "William"
lastName = "östensson"
elevDomain = "@elev.ga.ntig.se"
nickName = "Bimert"

#för.efternamn
#simon.östensson
#firstname[3].lastname[3]


#print(firstName[0:3].lower() + "" + lastName[0:3].lower()+"19")


userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"
print(userName)



gmailName = firstName.lower()
gmailName += "."
gmailName += lastName.lower()
gmailName += elevDomain.lower()

print(gmailName)


print(lastName.capitalize())
print(firstName.upper())

gamertag = "BlYaTMaChInE"

print(gamertag.lower)





#tecken = """() paranteser
#[] hakparanteser
#{} måsvingar
#: kolon
#; semikolon
#, komma
#\" dubbelfnutt
#\' enkelfnutt"""

#print(tecken[13])