# Program to define DNA, RNA and Protein classes and perform basic operations on their sequences without using Biopython

import random
class DNA:
    nature = "DNA"
    alphabet = ["A", "T", "G", "C"]
    sequence = ""
    size = 0

    def __init__(self, seq):
        self.sequence = seq.upper()
        self.size = len (self.sequence)
    
    def complement(self): # returns the complementary DNA strand
        cDNA = ""
        for i in range(0, self.size):
            if (self.sequence[i] == "A"): 
                cDNA = cDNA + "T"
            elif (self.sequence[i] == "T"):
                cDNA = cDNA + "A"
            elif (self.sequence[i] == "C"):
                cDNA = cDNA + "G"
            else:
                cDNA = cDNA + "C"
        return(cDNA)
        
    def transcribe(self): # transcribes DNA into RNA
        RNA = self.sequence.replace ("T","U")
        return(RNA)
        
class RNA: 
    nature = "RNA"
    alphabet = ["A","U","G","C"]
    sequence = ""
    size = 0

    def __init__(self, seq):
        self.sequence = seq.upper()
        self.size = len(self.sequence)

    def translate (self): # translates RNA into Protein
        protein = ""
        for i in range(0, self.size, 3):
            if (self.sequence[i]=="U"):
                if (self.sequence[i+1]=="U"):
                    if (self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "F"
                    else:
                        protein = protein + "L"
                elif(self.sequence[i+1]=="C"):
                    protein = protein + "S"
                elif(self.sequence[i+1]=="A"):
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "Y"
                    else:
                        break
                else:    
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "C"
                    elif(self.sequence[i+2]=="A"):
                        break
                    else:
                        protein = protein + "W"
                    
            elif(self.sequence[i]=="C"):
                if(self.sequence[i+1]=="U"):
                    protein = protein + "L"
                elif(self.sequence[i+1]=="C"):
                    protein = protein + "P"
                elif(self.sequence[i+1]=="A"):
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein +"H"
                    else:
                        protein = protein + "Q"
                else:
                    protein = protein + "R"
            
            elif(self.sequence[i]=="A"):
                if(self.sequence[i+1]=="U"):
                    if(self.sequence[i+2]=="G"):
                        protein = protein + "M"
                    else:
                        protein = protein + "I"
                elif(self.sequence[i+1]=="C"):
                    protein = protein + "T"
                elif(self.sequence[i+1]=="A"):
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "N"
                    else:
                        protein = protein + "K"
                else:
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "S"
                    else:
                        protein = protein + "R"
                    
            else:
                if(self.sequence[i+1]=="U"):
                    protein = protein + "V"
                elif(self.sequence[i+1]=="C"):
                    protein = protein + "A"
                elif(self.sequence[i+1]=="A"):
                    if(self.sequence[i+2]=="U") or (self.sequence[i+2]=="C"):
                        protein = protein + "D"
                    else:
                        protein = protein + "E"
                else:
                    protein = protein + "G"
        return(protein)
        
class Protein :
        nature="Protein"
        alphabet=['A','R','N','D','C','E','Q','G','H','I','W','L','M','K','F','P','S','T','Y','V']
        sequence = ""
        size = 0
        def __init__(self, seq):
            self.sequence = seq.upper()
            self.size = len(self.sequence)

        def mutation(self): # inserts a random mutation in the protein sequence (substitutes one amino acid by another)
            n = random.randint(0, self.size - 1) # chooses a random position in the sequence
            p = random.randint(0, len(self.alphabet) - 1) # chooses a random amino acid from the alphabet
            l = list(self.sequence) # converts the sequence into a list to allow mutation
            l[n] = self.alphabet[p] # performs the mutation
            return "".join(l) # converts the list back to a string and returns it
            


if __name__== '__main__' :
             # requests the user to input a sequence and choose an operation
             sequence = input ("Enter your DNA, RNA or protein sequence : ")

             print ("What do you want to do ?")
             print ("1 : Complement")
             print ("2 : Transcribe the sequence")
             print ("3 : Translate the sequence")
             print ("4 : Insert a random mutation in the protein sequence")
             print ("5 : Quit")

             choice = int(input("Enter the number of your choice : "))

             if choice == 1 : # complement DNA
                 dna1 = DNA (sequence)
                 comp = dna1.complement()
                 print("The complement sequence is : ",  comp)

             elif choice == 2 : # transcribes DNA into RNA
                 dna2 = DNA (sequence)
                 transcribed_strand = dna2.transcribe()
                 print("Your resulting RNA (transcribed DNA) is : ", transcribed_strand)

             elif choice == 3 : # translates RNA into Protein
                 # checks if the length of the sequence is a multiple of 3
                 if (len(sequence)%3!=0):
                     print ("ERROR IN READING FRAME!")
                 else: # proceeds with the translation
                     rna1 = RNA (sequence)
                     translated_rna = rna1.translate()
                     print("The protein sequence obtained is : ", translated_rna)

             elif choice == 4: # inserts a random mutation in the protein sequence
                 prot = Protein (sequence)
                 mutated_prot = prot.mutation().upper()
                 print("The mutated protein sequence is : ", mutated_prot)

             elif choice == 5: # quits the program
                 print("See you soon")

             else:
                print("Invalid Choice!")
                 
                 
                
                