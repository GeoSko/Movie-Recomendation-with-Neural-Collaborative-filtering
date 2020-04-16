#	Το όνομα του αρχείου προς επεξεργασία δίνεται σαν παράμετρος από το terminal
#	Το script δημιουργεί	
#		~~ ένα αρχείο input.csv με τα one-hot διανύσματα των χρηστών
#		~~ ένα αρχείο output.csv με τις επιθυμητές βαθμολογίες έχοντας εφαρμόσει
#			centering και γέμισμα των ελλειπών με 0 (η μέση τιμή εφόσον κάναμε centering)

import pandas as pd
import sys

# Άνοιγμα του αρχείου

file = sys.argv[1]

try:
	df = pd.read_csv(file, sep = '\t')
except (FileNotFoundError, IOError):
   	print("Wrong files or file paths")
   	sys.exit()


# Μετατρέπω το αρχείο στη ζητούμενη μορμή

# Φέρνω το αρχείο εγγραφών σε μορφή πίνακα users-movies

df.columns = ['user','movie','rate','timestamp']
df = df.drop(['timestamp'], axis = 1)
df = df.pivot(index='user', columns='movie', values='rate')


# Κεντράρω τις τιμές των χρηστών αφαιρώντας τη μέση τιμή τους

df= df.sub(df.mean(axis=1),axis=0)


# Γεμιζω τις κενές τιμές με 0

df.fillna(value=0, inplace= True)


# Κάνω όλες τις τιμές θετικές (προσθέτω σε όλες την απόλυτη τιμή της ελάχιστης τιμής)

df = df.add(abs(df.min().min()))										


# Οne hot διανυσματα χρηστών

users_one_hot = pd.get_dummies(df.index)


# Αποθηκεύω τα ζητούμενα αρχεία

df.to_csv('output.csv', sep=',', index=False, header= False)
users_one_hot.to_csv('input.csv', sep=',', index=False, header= False)
print("Created csv files")