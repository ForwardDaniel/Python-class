class Firefox:
    pass
tables1 = Firefox()
tables1.computer1 = "Lenovo"
tables1.computer2 = "Sumsung"
tables1.computer3 = "Probook"


table2 = Firefox()
table2.computer1 = "Dell"
table2.computer2 = "Dell Inspiron"
table2.computer3 = "Dell Inspiron Mini"

print (tables1.computer1)
print (table2.computer3)
print (tables1.computer3 + " "+table2.computer3)