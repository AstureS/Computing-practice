import Entry
import BioMenu
import DBAccess

def Run():
	reg = Entry.AskIsRegistered() #

	if reg:
		user = Entry.AskLoginPass() #			
	else: 
		user = Entry.Register() #

	print("Welcome, %s\n" % user) #

	userData = DBAccess.GetDateOfBirth(user) #
	recover = BioMenu.AskIsRecoverResults(userData[0])

	if recover:
		while 1:
			res = BioMenu.AskRecoverVersion(userData[0])
			BioMenu.RecoverVersion(res)
			if not BioMenu.AskIsRecoverResults(userData[0]):
				break
		if BioMenu.AskBuildNew():
			BioMenu.AskBiorhythms(userData) 
	else:
		BioMenu.AskBiorhythms(userData) #

	print("До свидания, %s" % user)
