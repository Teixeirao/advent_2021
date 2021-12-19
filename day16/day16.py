import numpy as np
real_input = "420D50000B318100415919B24E72D6509AE67F87195A3CCC518CC01197D538C3E00BC9A349A09802D258CC16FC016100660DC4283200087C6485F1C8C015A00A5A5FB19C363F2FD8CE1B1B99DE81D00C9D3002100B58002AB5400D50038008DA2020A9C00F300248065A4016B4C00810028003D9600CA4C0084007B8400A0002AA6F68440274080331D20C4300004323CC32830200D42A85D1BE4F1C1440072E4630F2CCD624206008CC5B3E3AB00580010E8710862F0803D06E10C65000946442A631EC2EC30926A600D2A583653BE2D98BFE3820975787C600A680252AC9354FFE8CD23BE1E180253548D057002429794BD4759794BD4709AEDAFF0530043003511006E24C4685A00087C428811EE7FD8BBC1805D28C73C93262526CB36AC600DCB9649334A23900AA9257963FEF17D8028200DC608A71B80010A8D50C23E9802B37AA40EA801CD96EDA25B39593BB002A33F72D9AD959802525BCD6D36CC00D580010A86D1761F080311AE32C73500224E3BCD6D0AE5600024F92F654E5F6132B49979802129DC6593401591389CA62A4840101C9064A34499E4A1B180276008CDEFA0D37BE834F6F11B13900923E008CF6611BC65BCB2CB46B3A779D4C998A848DED30F0014288010A8451062B980311C21BC7C20042A2846782A400834916CFA5B8013374F6A33973C532F071000B565F47F15A526273BB129B6D9985680680111C728FD339BDBD8F03980230A6C0119774999A09001093E34600A60052B2B1D7EF60C958EBF7B074D7AF4928CD6BA5A40208E002F935E855AE68EE56F3ED271E6B44460084AB55002572F3289B78600A6647D1E5F6871BE5E598099006512207600BCDCBCFD23CE463678100467680D27BAE920804119DBFA96E05F00431269D255DDA528D83A577285B91BCCB4802AB95A5C9B001299793FCD24C5D600BC652523D82D3FCB56EF737F045008E0FCDC7DAE40B64F7F799F3981F2490"

def parse_operator(packet, start, typeid, version):
    #print("operator")
    length_id = packet[start+6]
    op = {
        "typeid" : typeid,
        "type" : "operator",
        "children" : [],
        "version" : version
    }
    sub_start = start+7+15
    is_length_nb = True
    if length_id == "0": #15bits
        length = int(packet[start+7:start+7+15],2)
    else: # 11 bits
        is_length_nb = False
        length = int(packet[start+7:start+7+11],2)
        sub_start = start + 7 + 11 
    #print("op length {0}".format(length))
    done = False
    new_start = sub_start
    nb_subpacket = 0
    while not done:
        new_start, is_literal, value, rversion = parse_packet(packet,new_start)
        #if is_literal:
        #    op["children"].append({
        #        "type" : "literal",
        #        "value": value,
        #        "version": rversion
        #    })
        #else:
        #    op["children"].append({
        #        "type" : "operator",
        #        "value": value
        #    })
        op["children"].append(value)
        nb_subpacket += 1
        if is_length_nb:
            if new_start - sub_start == length:
                done = True
            if new_start - sub_start > length:
                assert(0)
        elif nb_subpacket == length:
            done = True
    return new_start, op 

def parse_literal(packet,start):
    #print("literal")
    done = False
    res = ""
    pos = start + 6 
    while not done:
        #print(packet[pos_hex:pos_hex+3])
        lbin = packet[pos:pos+5]
        #print(lbin)
        if lbin[0] == "0":
            done = True
        res += lbin[1:5]
        pos += 5

    #print(int(res,2))
    return pos,int(res,2)

def parse_packet(packet, start):
    #print("LL")
    #print(start)
    #print(packet[start:-1])
    res = []
    version = int(packet[start:start+3],2)
    typeid = int(packet[start+3:start+6],2)

    #print("v : {0} - tid : {1}".format(version,typeid))

    is_literal = False
    if typeid == 4:
        is_literal = True
        new_start, value = parse_literal(packet,start)
    else:
        new_start, op = parse_operator(packet,start,typeid,version)

    return new_start, is_literal, { "typeid": typeid, "version": version, "type":"literal", "value": value } if is_literal else op, version

def get_all_version(op_dict):
    s = 0
    s += op_dict["version"]
    if "children" in op_dict:
        for c in op_dict["children"]:
            s += get_all_version(c)
    return s

test_str_1 = "D2FE28"
test_str_2 = "38006F45291200"
test_str_3 = "8A004A801A8002F478"
test_str_4 = "620080001611562C8802118E34"
test_str_5 = "A0016C880162017C3686B18A3D4780"
test_str_6 = "C0015000016115A2E0802F182340"
test_string = test_str_6
sum_all_version = 0
ns, islit, dict_tree, v = parse_packet(format(int(test_string,16),"{0}b".format(len(test_string)*4)),0)
print(dict_tree)
print(get_all_version(dict_tree))

def interpret_tree(op_dict):
    values = []
    if "children" in op_dict:
        for c in op_dict["children"]:
            values.append(interpret_tree(c))
    else:
        assert (op_dict["typeid"] == 4)
        values.append(op_dict["value"])
    print("op : {0} - values : {1}".format( op_dict["typeid"], values))
    if op_dict["typeid"] == 0:
        return np.sum(values, dtype=np.uint64)
    elif op_dict["typeid"] == 1:
        return np.prod(values, dtype=np.uint64) # BY DEFAULT np is signed!!!
    elif op_dict["typeid"] == 2:
        return np.min(values)
    elif op_dict["typeid"] == 3:
        return np.max(values)
    elif op_dict["typeid"] == 4:
        return values[0]
    elif op_dict["typeid"] == 5:
        assert(len(values)==2)
        return 1 if values[0] > values[1] else 0
    elif op_dict["typeid"] == 6:
        assert(len(values)==2)
        return 1 if values[0] < values[1] else 0
    elif op_dict["typeid"] == 7:
        assert(len(values)==2)
        return 1 if values[0] == values[1] else 0
    else:
        assert(False)
#return value

test_str_1 = "C200B40A82"
test_str_2 = "880086C3E88112"
test_str_3 = "CE00C43D881120"
test_str_4 = "F600BC2D8F"
test_str_5 = "9C0141080250320F1802104A08"
test_str_6 = "04005AC33890"
test_str_7 = "D8005AC2A8F0"
test_str_8 = "9C005AC2F8F0"
test_str_9 = "D2FE28"
test_str_10 = "EE00D40C823060"
test_string = real_input
print("#########################")
print(len(test_string))
ns, islit, dict_tree, v = parse_packet(format(int(test_string,16),"0{0}b".format(len(test_string)*4)),0)
print(dict_tree)
print("RES")
print(interpret_tree(dict_tree))

print(np.prod([316, 837226, 11313038, 1359, 2124], dtype=np.uint64))