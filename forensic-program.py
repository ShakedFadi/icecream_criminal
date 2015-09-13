__author__ = 'knedlus'

import copy
#import collections

# DNA Features Database ################################################################################

dna = {
    "hairColor": {"blackHair": "CCAGCAATCGC", "brownHair": "GCCAGTGCCG", "orangeHair": "TTAGCTATCGC"},
    "faceShape": {"squareFace": "GCCACGG", "circleFace": "ACCACAA", "ovalFace": "AGGCCTCA"},
    "eyeColor": {"blueEyes": "TTGTGGTGGC", "greenEyes": "GGGAGGTGGC", "brownEyes": "AAGTAGTGAC"},
    "sex": {"male": "TGCAGGAACTTC", "female": "TGAAGGACCTTC"},
    "race": {"whiteRace": "AAAACCTCA", "blackRace": "CGACTACAG", "asianRace": "CGCGGGCCG"}
}

# Suspects ################################################################################

suspects = {
    "ziga": {"sex": "male",
             "race": "whiteRace",
             "hairColor": "orangeHair",
             "eyeColor": "brownEyes",
             "faceShape": "circleFace"
             },

    "matej": {"sex": "male",
             "race": "whiteRace",
             "hairColor": "blackHair",
             "eyeColor": "blueEyes",
             "faceShape": "ovalFace"
             },

    "miha": {"sex": "male",
             "race": "whiteRace",
             "hairColor": "brownHair",
             "eyeColor": "greenEyes",
             "faceShape": "squareFace"
             }
}

# DNA Found on the Crime Scene ################################################################################

f = open("DNA_CrimeScene.txt", "r")
dna_csi = f.read()
f.close()
# print dna_csi
# print type(dna_csi)

# CSI Program ################################################################################

suspects_dna = copy.deepcopy(suspects)


def suspects_add_dna(d, s, s_d): # dictionaries --> dna, suspects, suspects_dna; Adding DNA to suscpects, from our DNA pool
    for key, value in s.iteritems():
        for k, v in value.iteritems():
            if v in d[k]:
                #print v, d[k][v]
                s_d[key][k] = d[k][v]

suspects_add_dna(dna, suspects, suspects_dna)

criminal = []
#cnt = collections.Counter(criminal)

def find_icecream_criminal(s_d, dcs, cr):
    for a, b in s_d.iteritems():
        for c, d in b.iteritems():
            #print a, dcs.find(j)
            if dcs.find(d) > -1:
                cr.append(a)

    the_criminal = max(set(cr), key=cr.count)
    print "\n", "*"*35
    print "Our icecream crimnal is %s!!! :)" %the_criminal.capitalize()
    print "*"*35, "\n"

find_icecream_criminal(suspects_dna, dna_csi, criminal)




