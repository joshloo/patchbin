import sys

print("IFWI to patch  : " , sys.argv[1])

with open(sys.argv[1], 'r+b') as fh:
    fh.seek(0x2b1)  #offset for TSN 0 and TSN 1 config

    config = 0 # both 1G
    # config = 1 # TSN 0 1 G, TSN 1 2.5G 
    # config = 2 # TSN 0 2.5G, TSN 1 1G
    # config = 3 # TSN 0 2.5G, TSN 1 2.5G
    fh.write(((config << 4) + 1).to_bytes(1, byteorder='big'))