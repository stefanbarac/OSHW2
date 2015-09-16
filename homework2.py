__author__ = 'Stefane'

import csv
import collections

#prints neighborhood : percent of housing crowded

with open('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv') as csvfile:
    CensusReader = csv.reader(csvfile, delimiter = ',')
    CrowdedHousing = {}
    for row in CensusReader:
        k = row[1]
        v = row[2]
        CrowdedHousing[k] = v
print (CrowdedHousing)

#returns vacant properties neighborhoods

def VacantPropery():
    with open('City-Owned_Land_Inventory.csv') as csvfile:
        propertyReader = csv.reader(csvfile, delimiter = ',')
        VacantPropery = []
        for row in propertyReader:
            VacantPropery.append(row[7])
        del VacantPropery[0]
        return VacantPropery

def main():

#counts hte number of times a neighborhood appears and prints the neighborhood: number of vacant properties that are stored in a list

    vacantPropertyAmount = []

    vacantPropertyAmount.append(collections.Counter(VacantPropery()))


    print ("neighborhood: amount of vacant property ", vacantPropertyAmount)


main()