def testEqual(actual, expected):
    if actual == expected:
        print("Pass")
    else:
        print("Fail. Expected:", expected, "but got:", actual)

def sort_contacts(contact_dict):
    #turn the dictionary into a list (of, hmm, items?)
    listy = list(contact_dict.items())
    #create an empty list (that the tuples will go into)
    output = []
    #iterate over the items in the list  (ex: for something in something)
    for item in listy:
        (name, number, email) = (item[0], item[1][0], item[1][1])
        tuple1 = (name, number, email)
        output.append(tuple1)
    #we assign, as a tuple, the values in the dictionary list
        #note a tuple is like this `(val1, val2, etc...)`
        #a tuple is different from a list in that it's values cannot be modified, or that it is `"immutable"`
        #but, you can access values in a `tuple` the same way you can access a `list`.
        #ie `tuple[0], tuple[1]`
    #sort the list
    output.sort()
    #return the list
    return output

testEqual(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
       "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
       "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
       'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
testEqual(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
    "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}),
    [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
    ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])
testEqual(sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}),
    [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])
testEqual(sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
    ("1-333-555-9999", "kandinsky@painters.com")}), [('Almodovar, Pedro', '1-990-622-3892',
    'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
    ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
    '1-917-222-2222', 'tilda@greatActors.com')])
