

def main():
    listip = []
    list2ip = []
    for i in range(97,127):
        listip.append("202.229.44."+str(i))
    strip = ';'.join(listip)
    print(strip)
    for i in range(81,95):
        list2ip.append("210.150.25."+str(i))
    str2ip = ';'.join(list2ip)
    print(str2ip)

if __name__ == '__main__':
    main()


