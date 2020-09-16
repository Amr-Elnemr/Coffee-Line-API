# This file is used to fill the database from the the sample input given
# run >>exec(open('fillDB.py').read()) in shell

from coffeeApi.models import Product
input="CM001,small,base#CM002,small,premium#CM003,small,deluxe,waterlinecompatible#CM101,large,base#CM102,large,premium,waterlinecompatible#CM103,large,deluxe,waterlinecompatible#EM001,espresso,base#EM002,espresso,premium#EM003,espresso,deluxe,waterlinecompatible#CP001,small,1,vanilla#CP003,small,3,vanilla#CP011,small,1,caramel#CP013,small,3,caramel#CP021,small,1,psl#CP023,small,3,psl#CP031,small,1,mocha#CP033,small,3,mocha#CP041,small,1,hazelnut#CP043,small,3,hazelnut#CP101,large,1,vanilla#CP103,large,3,vanilla#CP111,large,1,caramel#CP113,large,3,caramel#CP121,large,1,psl#CP123,large,3,psl#CP131,large,1,mocha#CP133,large,3,mocha#CP141,large,1,hazelnut#CP143,large,3,hazelnut#EP003,espresso,3,vanilla#EP005,espresso,5,vanilla#EP007,espresso,7,vanilla#EP013,espresso,3,caramel#EP015,espresso,5,caramel#EP017,espresso,7,caramel"

for p in input.split('#'):
    line = p.split(',')
    sku=line[0]
    size=line[1]
    if "M" in sku: #Machine
        type="machine"
        model=line[2]
        water_line_compatible = True if 'waterlinecompatible' in p else False
        prod=Product(sku=sku, type=type, size=size, model=model, water_line_compatible=water_line_compatible)
    else: #Pod
        type="pod"
        pack_size = line[2]
        flavor=line[3]
        prod=Product(sku=sku, type=type, size=size, pack_size=int(pack_size), flavor=flavor)
    try:
        prod.save()
    except Exception as e:
        print("exception: "+ str(e))