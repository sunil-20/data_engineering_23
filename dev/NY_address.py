import pandas as pd
# List of addresses
addresses = [
    "14 Winding Way Drive, New York, NY 10003",
    "7758 Saxton Dr., Brooklyn, NY 11220",
    "7935 Stonybrook Ave., New York, NY 10027",
    "7645 Bayberry Ave., Corona, NY 11368",
    "63 River St., West Babylon, NY 11704",
    "571 Tarkiln Hill Road, Bronx, NY 10473",
    "637 Thorne St., Brooklyn, NY 11207",
    "8172 Glen Ridge Drive, Brentwood, NY 11717",
    "177 Locust Ave., Brooklyn, NY 11237",
    "62 Old Ridgewood Ave., Bronx, NY 10468",
    "426 East Oak Meadow Ave., Brooklyn, NY 11218",
    "428 North Lake Forest St., Brooklyn, NY 11230",
    "9700 Front Dr., Brooklyn, NY 11236",
    "8393 N. Union Street, Ithaca, NY 14850",
    "9249 Westminster Drive, Fairport, NY 14450",
    "240 Marsh Drive, Ridgewood, NY 11385",
    "184 Carriage Dr., Brooklyn, NY 11216",
    "530 Leatherwood Ave., Bronx, NY 10451",
    "5 Ocean Lane, Astoria, NY 11105",
    "796 Golden Star Lane, Bronx, NY 10462",
    "5 Bowman Street, Huntington, NY 11743",
    "3 Rockville Rd., Brooklyn, NY 11229",
    "919 San Carlos St., South Richmond Hill, NY 11419",
    "349 Riverside Drive, Apt 8, Far Rockaway, NY 11691",
    "776 N. Court Street, Yonkers, NY 10701",
    "7735 E. Lakewood Court, Spring Valley, NY 10977",
    "473 Hillcrest St., Bay Shore, NY 11706",
    "758 East Devonshire St., Massapequa, NY 11758",
    "7456 Helen Street, Bronx, NY 10461",
    "7996 Harvey Road, Brooklyn, NY 11238",
    "7432 Ivy Rd., New York, NY 10025",
    "9471 Prince Drive, Brooklyn, NY 11234",
    "9 Vermont Court, Jamaica, NY 11432",
    "8824 Cherry Hill Lane, East Elmhurst, NY 11370",
    "8518 Galvin St., Poughkeepsie, NY 12603",
    "2 Shipley Street, New York, NY 10034",
    "9350 St Louis Street, New York, NY 10024",
    "7770 Tailwater St., Staten Island, NY 10312",
    "2 Center Dr., Forest Hills, NY 11375",
    "7096 Lees Creek Ave., Brooklyn, NY 11204",
    "12 Gainsway Lane, Astoria, NY 11106",
    "426 Nichols St., Staten Island, NY 10306",
    "1 Piper Lane, Brooklyn, NY 11211",
    "9421 Windsor Ave., New York, NY 10029",
    "9302 South John St., Endicott, NY 13760",
    "90 Woodland Rd., Flushing, NY 11354",
    "408 Manhattan St., Staten Island, NY 10314",
    "9097 E. Foxrun Street, Troy, NY 12180",
    "84 Glenholme Ave., Auburn, NY 13021",
    "92 Eagle Drive, Brooklyn, NY 11224",
    "116 E. Queen Dr., Rome, NY 13440",
    "110 Elm St., Brooklyn, NY 11225",
    "997 Lakewood Ave., Lockport, NY 14094",
    "7981 Vermont Drive, Bronx, NY 10466",
    "80 Canal St., Brooklyn, NY 11235",
    "140 East Smith Store St., North Tonawanda, NY 14120",
    "862 S. Pierce Street, Brooklyn, NY 11228",
    "490 East Longbranch Circle, New York, NY 10128",
    "1 Lafayette St., Levittown, NY 11756",
    "7686 Chestnut Lane, Buffalo, NY 14215",
    "9127 Devon Drive, Newburgh, NY 12550",
    "5 South Dogwood Dr., Bronx, NY 10463",
    "9899 East Middle River St., Bronx, NY 10465",
    "9 Lexington Court, Patchogue, NY 11772",
    "127 Essex Street, Bronx, NY 10467",
    "447 Coffee Avenue, Flushing, NY 11355",
    "52 Elizabeth Ave., Middletown, NY 10940",
    "890 Newport St., Huntington Station, NY 11746",
    "86 Philmont Street, New York, NY 10031",
    "8223 N. Piper St., Buffalo, NY 14221",
    "423 Fairground Street, Bronx, NY"
    ]
# Create a DataFrame
data = {"Address": addresses}
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv("addresses.csv", index=False)

print("CSV file created successfully.")

addresses = [
    {
        "Street": "531 Stevens Road",
        "Municipality": "Town of Edmeston",
        "State": "New York",
        "Zip": "13335",
        "Country": "United States"
    },
    {
        "Street": "43 Sterling Lane",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11050",
        "Country": "United States"
    },
    {
        "Street": "3529 Broadway",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14227",
        "Country": "United States"
    },
    {
        "Street": "28 Beach Lane",
        "County": "Suffolk County",
        "State": "New York",
        "Zip": "11727",
        "Country": "United States"
    },
    {
        "Street": "3998 Lockport Avenue",
        "Municipality": "Town of Wheatfield",
        "State": "New York",
        "Zip": "14120",
        "Country": "United States"
    },
    {
        "Street": "28 Margaretta Court",
        "City": "City of New York",
        "State": "New York",
        "Zip": "10314",
        "Country": "United States"
    },
    {
        "Street": "24 Campbell Avenue",
        "State": "New York",
        "Zip": "10901",
        "Country": "United States"
    },
    {
        "Street": "315 Seigel Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11206",
        "Country": "United States"
    },
    {
        "Street": "2502 Washington Boulevard",
        "Municipality": "Town of Hempstead",
        "State": "New York",
        "Zip": "11710",
        "Country": "United States"
    },
    {
        "Street": "550 Moseley Road",
        "Municipality": "Town of Perinton",
        "State": "New York",
        "Zip": "14450",
        "Country": "United States"
    },
    {
        "Street": "43 Sterling Lane",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11050",
        "Country": "United States"
    },
    {
        "Street": "350 Hampton Road",
        "City": "Oceanside",
        "Municipality": "Town of Hempstead",
        "State": "New York",
        "Zip": "11572",
        "Country": "United States"
    },
    {
        "Street": "665 Seneca Creek Road",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14224",
        "Country": "United States"
    },
    {
        "Street": "172-14 133rd Avenue",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11434",
        "Country": "United States"
    },
    {
        "Street": "245 Cleveland Drive",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14215",
        "Country": "United States"
    },
    {
        "Street": "760 French Road",
        "City": "Buffalo",
        "State": "New York",
        "Zip": "14227",
        "Country": "United States"
    },
    {
        "Street": "585 Crescent Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11208",
        "Country": "United States"
    },
    {
        "Street": "4 Birdsong Parkway",
        "State": "New York",
        "Zip": "14127",
        "Country": "United States"
    },
    {
        "Street": "7861 Quaker Road",
        "Municipality": "Town of Aurora",
        "State": "New York",
        "Zip": "14127",
        "Country": "United States"
    },
    {
        "Street": "Two Blue Slip",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11222",
        "Country": "United States"
    },
    {
        "Street": "795 Fort Hunter Road",
        "City": "City of Amsterdam",
        "State": "New York",
        "Zip": "12010",
        "Country": "United States"
    },
    {
        "Street": "962 73rd Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11228",
        "Country": "United States"
    },
    {
        "Street": "127 Gatto Lane",
        "State": "New York",
        "Zip": "10965",
        "Country": "United States"
    },
    {
        "Street": "9550 Maple Street",
        "State": "New York",
        "Zip": "14032",
        "Country": "United States"
    },
    {
        "Street": "336 Otto Mills Road",
        "County": "Oswego County",
        "State": "New York",
        "Zip": "13437",
        "Country": "United States"
    },
    {
        "Street": "1445 West Flagler Drive",
        "County": "Westchester County",
        "State": "New York",
        "Zip": "10543",
        "Country": "United States"
    },
    {
        "Street": "33 South Drive",
        "Municipality": "Town of North Hempstead",
        "State": "New York",
        "Zip": "11030",
        "Country": "United States"
    },
    {
        "Street": "1 Oak Bluff Avenue",
        "County": "Westchester County",
        "State": "New York",
        "Zip": "10538",
        "Country": "United States"
    },
    {
        "Street": "48 Woodruff Avenue",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11226",
        "Country": "United States"
    },
    {
        "Street": "195 Montague Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11201",
        "Country": "United States"
    },
    {
        "Street": "208 East 38th Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11203",
        "Country": "United States"
    },
    {
        "Street": "168 Hancock Street",
        "County": "Suffolk County",
        "State": "New York",
        "Zip": "11717",
        "Country": "United States"
    },
    {
        "Street": "902 45th Street",
        "City": "City of New York",
        "State": "New York",
        "Zip": "11219",
        "Country": "United States"
    },
]