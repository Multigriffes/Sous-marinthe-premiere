def generation_liste():
    map_2_1=(('1011', '0110'), ('1011', '0101'))
    map_2_2=(('1010', '0111'), ('1001', '0101'))
    map_2=(map_2_1,map_2_2)
    map_3_1=(('1010', '0010', '0111'), ('1100', '1000', '0111'), ('1101', '1001', '0111'))
    map_3_2=(('1011', '0110', '1110'), ('1110', '1000', '0100'), ('1001', '0101', '1101'))
    map_3=(map_3_1,map_3_2)
    map_4_1=(('1010', '0010', '0110', '1110'), ('1000', '0101', '1000', '0100'), ('1100', '1011', '0100', '1100'), ('1001', '0111', '1001', '0101'))
    map_4_2=(('1010', '0011', '0010', '0110'), ('1101', '1010', '0101', '1100'), ('1110', '1100', '1010', '0100'), ('1001', '0001', '0101', '1101'))
    map_4=(map_4_1,map_4_2)
    map_5_1=(('1011', '0110', '1011', '0011', '0110'), ('1010', '0101', '1110', '1110', '1100'), ('1001', '0010', '0000', '0001', '0101'), ('1010', '0101', '1000', '0111', '1110'), ('1101', '1011', '0001', '0011', '0101'))
    map_5_2=(('1110', '1010', '0110', '1011', '0110'), ('1000', '0000', '0001', '0010', '0100'), ('1000', '0101', '1110', '1000', '0100'), ('1000', '0011', '0100', '1100', '1100'), ('1001', '0111', '1101', '1001', '0101'))
    map_5=(map_5_1,map_5_2)
    map_6_1=(('1110', '1110', '1011', '0010', '0111', '1110'), ('1100', '1001', '0010', '0101', '1010', '0101'), ('1000', '0010', '0100', '1010', '0000', '0110'), ('1000', '0101', '1000', '0000', '0101', '1100'), ('1100', '1011', '0001', '0100', '1011', '0101'), ('1001', '0011', '0111', '1001', '0011', '0111'))
    map_6_2=(('1010', '0110', '1010', '0010', '0110', '1110'), ('1000', '0000', '0000', '0001', '0101', '1100'), ('1100', '1000', '0100', '1010', '0011', '0101'), ('1100', '1001', '0000', '0000', '0011', '0110'), ('1000', '0110', '1000', '0000', '0110', '1100'), ('1001', '0101', '1001', '0001', '0101', '1101'))
    map_6=(map_6_1,map_6_2)
    map_7_1=(('1010', '0010', '0111', '1010', '0011', '0110', '1110'), ('1101', '1000', '0010', '0100', '1110', '1101', '1100'), ('1011', '0100', '1001', '0100', '1001', '0010', '0101'), ('1110', '1001', '0110', '1001', '0010', '0101', '1110'), ('1001', '0110', '1000', '0010', '0000', '0011', '0101'), ('1110', '1001', '0000', '0101', '1100', '1011', '0110'), ('1001', '0011', '0101', '1011', '0001', '0011', '0101'))
    map_7_2=(('1110', '1010', '0010', '0010', '0011', '0010', '0111'), ('1100', '1000', '0000', '0100', '1010', '0000', '0110'), ('1100', '1001', '0100', '1000', '0000', '0001', '0100'), ('1000', '0110', '1100', '1000', '0000', '0110', '1100'), ('1000', '0100', '1000', '0000', '0001', '0100', '1100'), ('1000', '0000', '0000', '0100', '1010', '0000', '0101'), ('1101', '1001', '0001', '0001', '0001', '0001', '0111'))
    map_7=(map_7_1,map_7_2)
    map_8_1=(('1010', '0010', '0010', '0111', '1010', '0010', '0010', '0110'), ('1001', '0000', '0001', '0010', '0000', '0100', '1001', '0100'), ('1110', '1000', '0010', '0000', '0001', '0001', '0010', '0100'), ('1100', '1001', '0100', '1101', '1011', '0110', '1000', '0100'), ('1000', '0010', '0000', '0111', '1110', '1100', '1000', '0100'), ('1001', '0000', '0001', '0010', '0001', '0100', '1000', '0100'), ('1010', '0100', '1110', '1000', '0010', '0101', '1000', '0100'), ('1001', '0101', '1001', '0001', '0101', '1011', '0001', '0101'))
    map_8_2=(('1010', '0111', '1110', '1010', '0010', '0010', '0011', '0110'), ('1100', '1010', '0001', '0001', '0101', '1000', '0110', '1100'), ('1100', '1001', '0011', '0010', '0010', '0101', '1000', '0101'), ('1000', '0011', '0010', '0100', '1100', '1010', '0000', '0110'), ('1000', '0110', '1001', '0100', '1001', '0101', '1100', '1100'), ('1100', '1100', '1010', '0001', '0110', '1010', '0100', '1100'), ('1100', '1100', '1000', '0011', '0100', '1001', '0000', '0100'), ('1101', '1001', '0101', '1011', '0001', '0111', '1001', '0101'))
    map_8=(map_8_1,map_8_2)
    map_9_1=(('1110', '1010', '0011', '0110', '1010', '0011', '0110', '1010', '0111'), ('1100', '1001', '0110', '1100', '1001', '0010', '0100', '1100', '1110'), ('1000', '0011', '0101', '1000', '0011', '0100', '1000', '0100', '1100'), ('1001', '0010', '0010', '0100', '1010', '0100', '1100', '1000', '0101'), ('1010', '0101', '1100', '1000', '0001', '0100', '1100', '1001', '0111'), ('1100', '1010', '0100', '1000', '0110', '1100', '1001', '0010', '0110'), ('1100', '1100', '1001', '0000', '0100', '1000', '0010', '0100', '1100'), ('1001', '0001', '0010', '0100', '1001', '0100', '1100', '1000', '0100'), ('1011', '0011', '0101', '1001', '0011', '0101', '1001', '0001', '0101'))
    map_9_2=(('1010', '0011', '0110', '1010', '0110', '1010', '0011', '0110', '1110'), ('1000', '0011', '0101', '1101', '1100', '1100', '1010', '0101', '1100'), ('1000', '0010', '0111', '1110', '1100', '1100', '1001', '0010', '0100'), ('1100', '1100', '1010', '0100', '1001', '0000', '0110', '1100', '1100'), ('1100', '1000', '0001', '0001', '0011', '0101', '1100', '1000', '0101'), ('1000', '0001', '0010', '0010', '0110', '1010', '0001', '0001', '0110'), ('1000', '0011', '0100', '1000', '0101', '1000', '0010', '0110', '1100'), ('1001', '0110', '1100', '1100', '1010', '0100', '1100', '1000', '0101'), ('1011', '0001', '0001', '0101', '1101', '1101', '1101', '1001', '0111'))
    map_9=(map_9_1,map_9_2)
    map_10_1=(('1010', '0011', '0010', '0110', '1010', '0010', '0011', '0110', '1010', '0110'), ('1100', '1010', '0101', '1101', '1000', '0001', '0110', '1001', '0100', '1100'), ('1000', '0101', '1010', '0110', '1001', '0111', '1100', '1110', '1100', '1101'), ('1000', '0011', '0100', '1000', '0010', '0010', '0100', '1100', '1001', '0110'), ('1100', '1010', '0101', '1100', '1100', '1100', '1100', '1000', '0110', '1100'), ('1000', '0100', '1010', '0100', '1100', '1001', '0101', '1100', '1100', '1100'), ('1100', '1001', '0100', '1100', '1000', '0011', '0111', '1101', '1100', '1100'), ('1000', '0011', '0101', '1100', '1000', '0011', '0010', '0011', '0000', '0101'), ('1000', '0011', '0010', '0100', '1100', '1110', '1000', '0110', '1100', '1110'), ('1101', '1011', '0101', '1001', '0101', '1001', '0101', '1101', '1001', '0101'))
    map_10_2=(('1011', '0011', '0110', '1010', '0110', '1010', '0010', '0011', '0010', '0110'), ('1110', '1010', '0001', '0001', '0100', '1100', '1000', '0010', '0101', '1100'), ('1100', '1000', '0011', '0010', '0100', '1001', '0100', '1000', '0010', '0101'), ('1001', '0101', '1110', '1001', '0000', '0110', '1100', '1100', '1000', '0110'), ('1010', '0011', '0000', '0110', '1000', '0100', '1001', '0101', '1100', '1101'), ('1100', '1010', '0001', '0100', '1000', '0101', '1010', '0010', '0000', '0111'), ('1100', '1000', '0111', '1101', '1000', '0011', '0001', '0100', '1101', '1110'), ('1001', '0100', '1110', '1011', '0000', '0010', '0110', '1000', '0011', '0101'), ('1011', '0100', '1000', '0011', '0100', '1000', '0101', '1001', '0010', '0110'), ('1011', '0001', '0101', '1011', '0101', '1001', '0011', '0111', '1101', '1101'))
    map_10=(map_10_1,map_10_2)
    map_11_1=(('1010', '0010', '0110', '1010', '0111', '1110', '1010', '0011', '0110', '1010', '0111'), ('1100', '1100', '1001', '0001', '0011', '0001', '0001', '0110', '1100', '1001', '0110'), ('1100', '1000', '0011', '0011', '0011', '0011', '0110', '1100', '1000', '0010', '0101'), ('1100', '1100', '1010', '0011', '0011', '0110', '1000', '0000', '0101', '1000', '0110'), ('1100', '1100', '1001', '0011', '0110', '1100', '1100', '1001', '0111', '1100', '1100'), ('1001', '0001', '0011', '0110', '1100', '1100', '1000', '0010', '0010', '0101', '1100'), ('1010', '0011', '0110', '1001', '0100', '1101', '1100', '1001', '0101', '1010', '0101'), ('1100', '1010', '0100', '1010', '0001', '0011', '0101', '1110', '1011', '0101', '1110'), ('1101', '1000', '0100', '1100', '1110', '1010', '0011', '0100', '1110', '1010', '0101'), ('1011', '0100', '1000', '0001', '0000', '0001', '0111', '1100', '1000', '0101', '1110'), ('1011', '0101', '1001', '0111', '1001', '0011', '0111', '1001', '0001', '0011', '0101'))
    map_11_2=(('1010', '0110', '1010', '0010', '0010', '0010', '0010', '0010', '0110', '1010', '0110'), ('1000', '0100', '1001', '0001', '0001', '0000', '0001', '0001', '0101', '1000', '0100'), ('1000', '0100', '1010', '0110', '1010', '0000', '0010', '0010', '0110', '1000', '0100'), ('1000', '0100', '1000', '0001', '0000', '0001', '0001', '0100', '1000', '0000', '0100'), ('1000', '0100', '1000', '0110', '1100', '1010', '0110', '1100', '1101', '1000', '0100'), ('1000', '0000', '0000', '0000', '0100', '1000', '0001', '0000', '0110', '1000', '0100'), ('1000', '0100', '1000', '0000', '0100', '1000', '0110', '1000', '0100', '1000', '0100'), ('1000', '0100', '1101', '1001', '0001', '0000', '0101', '1001', '0101', '1001', '0101'), ('1000', '0100', '1010', '0010', '0010', '0000', '0010', '0010', '0010', '0010', '0110'), ('1000', '0100', '1000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0100'), ('1001', '0101', '1001', '0001', '0001', '0001', '0001', '0001', '0001', '0001', '0101'))
    map_11=(map_11_1,map_11_2)
    map_12_1=(('1010', '0011', '0010', '0011', '0011', '0010', '0011', '0010', '0010', '0110', '1011', '0110'), ('1101', '1010', '0001', '0010', '0010', '0001', '0010', '0100', '1001', '0000', '0011', '0100'), ('1010', '0000', '0111', '1100', '1000', '0110', '1100', '1100', '1010', '0100', '1010', '0100'), ('1100', '1000', '0111', '1000', '0100', '1100', '1101', '1001', '0000', '0101', '1001', '0100'), ('1100', '1000', '0111', '1100', '1100', '1001', '0011', '0010', '0100', '1010', '0111', '1100'), ('1101', '1000', '0011', '0001', '0001', '0011', '0111', '1100', '1101', '1000', '0111', '1100'), ('1010', '0000', '0010', '0010', '0010', '0010', '0010', '0000', '0010', '0001', '0011', '0100'), ('1100', '1100', '1000', '0101', '1000', '0001', '0101', '1100', '1000', '0010', '0110', '1100'), ('1100', '1001', '0100', '1010', '0001', '0110', '1110', '1100', '1000', '0100', '1001', '0100'), ('1000', '0010', '0100', '1000', '0010', '0101', '1000', '0100', '1000', '0001', '0110', '1100'), ('1100', '1100', '1000', '0100', '1000', '0010', '0001', '0100', '1100', '1010', '0000', '0100'), ('1001', '0101', '1001', '0101', '1001', '0001', '0011', '0001', '0101', '1001', '0001', '0101'))
    map_12_2=(('1011', '0011', '0010', '0011', '0011', '0011', '0010', '0110', '1010', '0010', '0110', '1110'), ('1010', '0111', '1100', '1011', '0011', '0110', '1100', '1100', '1001', '0101', '1100', '1100'), ('1100', '1110', '1000', '0010', '0111', '1100', '1101', '1000', '0010', '0011', '0101', '1100'), ('1100', '1100', '1100', '1100', '1010', '0001', '0011', '0001', '0001', '0011', '0010', '0101'), ('1001', '0001', '0100', '1101', '1000', '0011', '0011', '0110', '1010', '0110', '1100', '1110'), ('1010', '0011', '0000', '0011', '0101', '1011', '0110', '1100', '1101', '1100', '1100', '1100'), ('1001', '0111', '1000', '0011', '0011', '0011', '0101', '1000', '0011', '0101', '1100', '1100'), ('1010', '0011', '0001', '0011', '0011', '0011', '0010', '0000', '0011', '0011', '0000', '0101'), ('1100', '1010', '0011', '0010', '0011', '0111', '1100', '1100', '1011', '0110', '1100', '1110'), ('1100', '1001', '0111', '1000', '0011', '0011', '0100', '1001', '0110', '1100', '1001', '0100'), ('1001', '0011', '0011', '0101', '1011', '0011', '0001', '0111', '1100', '1001', '0011', '0100'), ('1011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0001', '0011', '0011', '0101'))
    map_12=(map_12_1,map_12_2)
    map_13_1= (('1011', '0010', '0110', '1010', '0011', '0010', '0110', '1110', '1010', '0011', '0010', '0110', '1110'), ('1011', '0101', '1000', '0101', '1011', '0101', '1000', '0001', '0100', '1011', '0101', '1101', '1100'), ('1010', '0011', '0001', '0110', '1010', '0011', '0001', '0110', '1001', '0010', '0011', '0011', '0100'), ('1101', '1010', '0110', '1100', '1101', '1010', '0011', '0000', '0110', '1100', '1010', '0011', '0101'), ('1010', '0100', '1001', '0000', '0111', '1001', '0111', '1100', '1001', '0101', '1100', '1010', '0110'), ('1001', '0100', '1010', '0001', '0010', '0110', '1011', '0100', '1010', '0011', '0001', '0100', '1101'), ('1110', '1100', '1000', '0011', '0101', '1000', '0011', '0101', '1100', '1010', '0011', '0001', '0110'), ('1001', '0100', '1101', '1110', '1011', '0101', '1011', '0011', '0101', '1001', '0110', '1010', '0101'), ('1010', '0001', '0011', '0100', '1010', '0010', '0010', '0110', '1011', '0011', '0100', '1101', '1110'), ('1000', '0011', '0111', '1000', '0101', '1100', '1100', '1001', '0010', '0111', '1000', '0011', '0101'), ('1100', '1110', '1010', '0101', '1010', '0100', '1001', '0110', '1001', '0110', '1100', '1011', '0110'), ('1001', '0100', '1000', '0011', '0001', '0001', '0110', '1001', '0110', '1100', '1001', '0010', '0100'), ('1011', '0101', '1001', '0011', '0011', '0011', '0001', '0011', '0101', '1001', '0011', '0101', '1101'))
    map_13_2= (('1110', '1110', '1010', '0110', '1011', '0110', '1010', '0010', '0010', '0011', '0010', '0110', '1110'), ('1100', '1100', '1001', '0000', '0010', '0100', '1101', '1100', '1000', '0110', '1100', '1000', '0100'), ('1100', '1000', '0010', '0001', '0000', '0001', '0011', '0100', '1001', '0000', '0100', '1001', '0101'), ('1100', '1001', '0000', '0010', '0100', '1010', '0010', '0100', '1010', '0000', '0000', '0010', '0110'), ('1000', '0010', '0000', '0101', '1100', '1000', '0000', '0000', '0000', '0001', '0001', '0000', '0101'), ('1001', '0101', '1000', '0010', '0000', '0001', '0100', '1100', '1000', '0010', '0110', '1000', '0110'), ('1010', '0010', '0100', '1000', '0100', '1110', '1100', '1000', '0000', '0001', '0100', '1000', '0101'), ('1001', '0001', '0101', '1100', '1000', '0100', '1100', '1000', '0000', '0110', '1001', '0000', '0110'), ('1010', '0010', '0010', '0100', '1000', '0101', '1100', '1001', '0100', '1000', '0110', '1001', '0100'), ('1001', '0001', '0001', '0101', '1000', '0010', '0000', '0010', '0100', '1000', '0000', '0010', '0100'), ('1010', '0110', '1010', '0011', '0000', '0100', '1001', '0001', '0100', '1001', '0000', '0101', '1100'), ('1000', '0100', '1000', '0010', '0000', '0000', '0011', '0010', '0100', '1011', '0100', '1110', '1100'), ('1001', '0001', '0001', '0101', '1001', '0001', '0111', '1001', '0001', '0011', '0001', '0101', '1101'))
    map_13=(map_13_1, map_13_2)
    map_14_1=(('1010', '0110', '1010', '0110', '1011', '0010', '0010', '0010', '0010', '0010', '0110', '1011', '0010', '0110'), ('1000', '0100', '1001', '0000', '0110', '1000', '0001', '0001', '0100', '1000', '0001', '0110', '1000', '0101'), ('1000', '0000', '0110', '1000', '0000', '0100', '1010', '0110', '1101', '1000', '0010', '0101', '1000', '0110'), ('1001', '0000', '0000', '0100', '1000', '0001', '0000', '0000', '0010', '0000', '0101', '1010', '0001', '0101'), ('1010', '0000', '0001', '0101', '1000', '0010', '0100', '1000', '0001', '0000', '0010', '0100', '1010', '0110'), ('1000', '0100', '1110', '1110', '1001', '0100', '1001', '0100', '1010', '0001', '0100', '1000', '0000', '0100'), ('1000', '0100', '1001', '0000', '0110', '1001', '0110', '1101', '1100', '1110', '1000', '0100', '1001', '0101'), ('1100', '1001', '0110', '1000', '0001', '0110', '1101', '1010', '0000', '0101', '1001', '0000', '0010', '0110'), ('1000', '0010', '0000', '0100', '1110', '1100', '1010', '0001', '0101', '1010', '0111', '1000', '0100', '1100'), ('1000', '0100', '1000', '0000', '0000', '0101', '1000', '0010', '0111', '1000', '0010', '0000', '0000', '0100'), ('1100', '1000', '0100', '1001', '0101', '1010', '0001', '0101', '1010', '0000', '0000', '0101', '1000', '0100'), ('1100', '1001', '0000', '0010', '0010', '0100', '1011', '0010', '0101', '1100', '1100', '1011', '0000', '0101'), ('1000', '0111', '1000', '0100', '1000', '0000', '0110', '1100', '1010', '0100', '1000', '0010', '0100', '1110'), ('1001', '0111', '1001', '0101', '1001', '0001', '0101', '1001', '0001', '0101', '1001', '0001', '0001', '0101'))
    map_14_2=(('1010', '0010', '0011', '0011', '0010', '0010', '0011', '0010', '0010', '0110', '1010', '0010', '0010', '0110'), ('1101', '1101', '1010', '0010', '0001', '0100', '1010', '0001', '0001', '0000', '0000', '0000', '0001', '0101'), ('1010', '0010', '0000', '0001', '0010', '0000', '0101', '1010', '0111', '1000', '0000', '0101', '1010', '0110'), ('1001', '0001', '0100', '1010', '0000', '0001', '0010', '0000', '0111', '1001', '0001', '0010', '0000', '0101'), ('1010', '0010', '0100', '1001', '0000', '0111', '1000', '0101', '1010', '0010', '0010', '0000', '0101', '1110'), ('1000', '0000', '0001', '0110', '1001', '0011', '0101', '1010', '0001', '0100', '1000', '0001', '0010', '0100'), ('1001', '0101', '1110', '1000', '0010', '0110', '1011', '0101', '1010', '0001', '0000', '0110', '1000', '0100'), ('1010', '0011', '0100', '1001', '0100', '1000', '0110', '1011', '0001', '0010', '0000', '0101', '1000', '0100'), ('1000', '0110', '1001', '0110', '1101', '1001', '0000', '0011', '0110', '1000', '0100', '1011', '0001', '0100'), ('1001', '0001', '0011', '0000', '0010', '0110', '1001', '0111', '1000', '0000', '0000', '0010', '0010', '0100'), ('1010', '0010', '0011', '0000', '0100', '1101', '1010', '0010', '0001', '0100', '1001', '0100', '1000', '0101'), ('1000', '0100', '1110', '1001', '0000', '0010', '0000', '0001', '0010', '0001', '0110', '1001', '0101', '1110'), ('1000', '0001', '0000', '0010', '0000', '0001', '0100', '1010', '0000', '0110', '1000', '0010', '0010', '0100'), ('1001', '0111', '1001', '0001', '0001', '0011', '0101', '1001', '0001', '0101', '1001', '0101', '1001', '0101'))
    map_14=(map_14_1, map_14_2)
    map_15_1=(('1011', '0110', '1011', '0011', '0110', '1010', '0110', '1010', '0110', '1010', '0011', '0011', '0011', '0011', '0110'), ('1110', '1001', '0010', '0011', '0101', '1100', '1100', '1100', '1100', '1100', '1010', '0011', '0011', '0111', '1100'), ('1000', '0111', '1100', '1011', '0011', '0101', '1100', '1101', '1100', '1100', '1100', '1010', '0110', '1010', '0100'), ('1100', '1010', '0001', '0011', '0011', '0010', '0101', '1010', '0001', '0100', '1001', '0101', '1001', '0101', '1100'), ('1100', '1101', '1010', '0011', '0111', '1100', '1010', '0100', '1110', '1100', '1011', '0011', '0011', '0011', '0101'), ('1001', '0011', '0001', '0011', '0011', '0100', '1101', '1100', '1100', '1001', '0010', '0011', '0011', '0011', '0110'), ('1010', '0011', '0010', '0010', '0011', '0000', '0011', '0101', '1000', '0111', '1100', '1010', '0011', '0110', '1100'), ('1100', '1110', '1100', '1001', '0110', '1100', '1011', '0110', '1100', '1011', '0100', '1100', '1110', '1001', '0101'), ('1100', '1100', '1000', '0111', '1100', '1000', '0011', '0101', '1000', '0010', '0101', '1100', '1000', '0011', '0110'), ('1100', '1100', '1100', '1011', '0101', '1100', '1010', '0110', '1100', '1000', '0011', '0101', '1100', '1110', '1100'), ('1001', '0101', '1001', '0011', '0011', '0100', '1101', '1100', '1100', '1001', '0011', '0111', '1000', '0101', '1100'), ('1010', '0110', '1010', '0011', '0110', '1001', '0011', '0101', '1001', '0011', '0011', '0011', '0101', '1010', '0101'), ('1100', '1100', '1100', '1110', '1001', '0111', '1010', '0011', '0110', '1010', '0011', '0011', '0011', '0100', '1110'), ('1100', '1100', '1001', '0001', '0011', '0011', '0100', '1011', '0101', '1100', '1011', '0011', '0110', '1100', '1100'), ('1101', '1001', '0011', '0011', '0011', '0011', '0001', '0011', '0011', '0001', '0011', '0011', '0101', '1001', '0101'))
    map_15_2=(('1010', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0110'), ('1000', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0110', '1100'), ('1100', '1010', '0010', '0010', '0010', '0010', '0010', '0010', '0010', '0010', '0010', '0010', '0110', '1100', '1100'), ('1100', '1000', '0001', '0001', '0001', '0001', '0001', '0001', '0001', '0001', '0001', '0001', '0100', '1100', '1100'), ('1100', '1100', '1010', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0110', '1100', '1100', '1100'), ('1100', '1100', '1100', '1010', '0011', '0011', '0011', '0011', '0011', '0011', '0110', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1100', '1010', '0011', '0011', '0011', '0011', '0110', '1100', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1100', '1100', '1010', '0011', '0011', '0110', '1100', '1100', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1100', '1100', '1100', '1011', '0011', '0101', '1100', '1100', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1100', '1100', '1001', '0011', '0011', '0011', '0101', '1100', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1100', '1001', '0011', '0011', '0011', '0011', '0011', '0101', '1100', '1100', '1100', '1100'), ('1100', '1100', '1100', '1001', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0101', '1100', '1100', '1100'), ('1100', '1100', '1001', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0101', '1100', '1100'), ('1100', '1001', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0101', '1100'), ('1001', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0011', '0101'))
    map_15=(map_15_1, map_15_2)
    liste_maps=(map_2,map_3,map_4,map_5,map_6,map_7,map_8,map_9,map_10,map_11,map_12,map_13,map_14,map_15)
    return liste_maps

def old_creation_maps(taille:int):
    generated_one=((input() for i in range(taille)) for j in range(taille))
    return generated_one

def murs_convert(gauche,droite,haut,bas):
    murs_locaux=""
    if gauche:
        murs_locaux=murs_locaux+'1'
    else:
        murs_locaux=murs_locaux+'0'
    if droite:
        murs_locaux=murs_locaux+'1'
    else:
        murs_locaux=murs_locaux+'0'
    if haut:
        murs_locaux=murs_locaux+'1'
    else:
        murs_locaux=murs_locaux+'0'
    if bas:
        murs_locaux=murs_locaux+'1'
    else:
        murs_locaux=murs_locaux+'0'
    return murs_locaux

def affichage_grille(grille):
    print("=====================================")
    for a in grille:
        print(a)
    print("=====================================")

def murs_cotes(taille,grille_murs):
    for i in range(taille):
        grille_murs[0][i]=grille_murs[0][i][0]+grille_murs[0][i][1]+"1"+grille_murs[0][i][3]
        grille_murs[taille-1][i]=grille_murs[taille-1][i][0]+grille_murs[taille-1][i][1]+grille_murs[taille-1][i][2]+"1"
        grille_murs[i][0]="1"+grille_murs[i][0][1]+grille_murs[i][0][2]+grille_murs[i][0][3]
        grille_murs[i][taille-1]=grille_murs[i][taille-1][0]+"1"+grille_murs[i][taille-1][2]+grille_murs[i][taille-1][3]
    return grille_murs

def murs_communs(taille,grille_murs):
    for i in range(taille):
        for j in range(taille):
            if i>0:
                if grille_murs[i][j][2]=="1":
                    grille_murs[i-1][j]=grille_murs[i-1][j][0]+grille_murs[i-1][j][1]+grille_murs[i-1][j][2]+"1"
            if i<taille-1:
                if grille_murs[i][j][3]=="1":
                    grille_murs[i+1][j]=grille_murs[i+1][j][0]+grille_murs[i+1][j][1]+"1"+grille_murs[i+1][j][3]
            if j>0:
                if grille_murs[i][j][0]=="1":
                    grille_murs[i][j-1]=grille_murs[i][j-1][0]+"1"+grille_murs[i][j-1][2]+grille_murs[i][j-1][3]
            if j<taille-1:
                if grille_murs[i][j][1]=="1":
                    grille_murs[i][j+1]="1"+grille_murs[i][j+1][1]+grille_murs[i][j+1][2]+grille_murs[i][j+1][3]
    return grille_murs
            
def traitement_commande(commande:str):
    gauche,droite,haut,bas=False,False,False,False
    for n in commande:
        if n=="z":     
            haut = not haut
        elif n=="q":
            gauche = not gauche
        elif n=="s":
            bas = not bas
        elif n=="d":
            droite = not droite
        else:
            print(n+': commande non reconnue')
    return gauche,droite,haut,bas

def creation_map_intereactive(taille:int):
    assert taille>1, "trop petite carte"
    grille_murs=[[" " for i in range(taille)] for j in range(taille)]
    for i in range(taille):
        for j in range(taille):
            gauche,droite,haut,bas,commande=False,False,False,False," "
            grille_murs[i][j]="X"
            affichage_grille(grille_murs)
            while commande==" ":
                commande=input("zqsd pour murs, c pour revenir de 1 : ").lower()

                #Cas d'une erreur sur l'entrée précèdente
                for b in commande:
                    if b=="c":
                        commande="c"
                if commande=="c":
                    commande=" "   
                    if j-1<0 and i-1<0:
                        print('Pas possible de revenir en arrière')
                    else:
                        grille_murs[i][j]=" "
                        if j-1<0:
                            grille_murs[i-1][taille-1]="X"
                        else:
                            grille_murs[i][j-1]="X"
                        affichage_grille(grille_murs)
                        commande_back=input("zqsd pour murs précèdent : ").lower()
                        _gauche,_droite,_haut,_bas=traitement_commande(commande_back)
                        if j-1<0:
                            grille_murs[i-1][taille-1]=murs_convert(_gauche,_droite,_haut,_bas)
                        else:
                            grille_murs[i][j-1]=murs_convert(_gauche,_droite,_haut,_bas)
                        grille_murs[i][j]="X"
                        affichage_grille(grille_murs)
                
            #Traitement de la commande
            gauche,droite,haut,bas=traitement_commande(commande)
            grille_murs[i][j]=murs_convert(gauche,droite,haut,bas)

    #Mise en place des murs obligatoires ou déduis
    grille_murs=murs_cotes(taille,grille_murs)
    grille_murs=murs_communs(taille,grille_murs)
    
    #Transformation en tuple
    for i in range(taille):
        grille_murs[i]=tuple(grille_murs[i]) # type: ignore
    grille_murs=tuple(grille_murs)
    
    affichage_grille(grille_murs)

    return grille_murs