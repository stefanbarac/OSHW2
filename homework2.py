
import csv
import sqLite3

#DB connection--------------------------------------

conn = sqLite3.connect(':memory:')

# cursor--------------------------------------------

c = conn.cursor()

# executing the table--------------------------------
def main():

#make table for vacant city owned properties

    c.execute('''CREATE TABLE city_owned
            (14_Digit_PIN_#,Street_Number,Dir,Street_Name,Type,Sq_Ft,Ward,
            Community_Area,Zoning_Classification,TIF_District,Location
    )''' )

#make table for census data

    c.execute('''CREATE TABLE census
            (Community_Area_Number,
            COMMUNITY_AREA_NAME,PERCENT_OF_HOUSING_CROWDED,PERCENT_HOUSEHOLDS_BELOW_POVERTY,
            PERCENT_AGED_16+_UNEMPLOYED,
            PERCENT_AGED_25+_WITHOUT_HIGH_SCHOOL_DIPLOMA,
            PERCENT_AGED_UNDER_18_OR_OVER_64,PER_CAPITA_INCOME,HARDSHIP_INDEX
    )''')


with open('City-Owned_Land_Inventory.csv', 'rb') as cityCSV:
    dr = csv.DictReader(cityCSV, delimiter=',')
    to_db = [(i['14_Digit_PIN_#'], i['Street_Number'], i['Dir'], i['Street_Name'], i['Type'],
              i['Sq_Ft'], i['Ward'], i['Community_Area'], i['Zoning_Classification'],
              i['TIF_District'], i['Location']) for i in dr]

c.executemany('''INSERT INTO cityCSV
(14_Digit_PIN_#, Street_Number, Dir, Street_Name,
Type, Sq_Ft, Ward, Community_Area, Zoning_Classification, TIF_District, Location)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', to_db)
conn.commit()

for row in dr:
    print (row())