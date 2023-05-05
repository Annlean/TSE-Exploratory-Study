#读取API与ID
def getAPIid():
    import re
    APIid = []
    with open('API Info.txt', "r") as f:  # 设置文件对象
        data = f.readlines()
        for line in data:
            lineitem = line.strip('\n').split(", ")
            API = ''
            # INSERT INTO `apiInfo` VALUES ('1'
            id = re.findall(r'\d+', lineitem[0])[0]  # 1
            if lineitem[1] == "' '":
                API = lineitem[2] + '.' + lineitem[3]
            else:
                API = lineitem[1] + '.' + lineitem[2] + '.' + lineitem[3]
            API = API.replace("'", "").replace(".null", "")
            # print(id, API)

            temp=[]
            temp.append(id)
            temp.append(API)
            APIid.append(tuple(temp))
    f.close()
    return list(set(APIid))

def writeAPItoExcel():
    APIid = getAPIid()
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, 'Serial Num')  # 表头(行，列，写入的内容)
    worksheet.write(0, 1, 'API')
    worksheet.write(0, 2, 'Search Words')
    worksheet.write(0, 3, 'Ground Truth API')
    APIlist=[]
    for i in range(1,67):
        for item in APIid:
            idnum=item[0]
            API=item[1]
            if int(idnum)==i:
                if API not in APIlist:
                    print(idnum, API)
                    APIlist.append(API)
                    num=len(APIlist)
                    worksheet.write(num, 0, num)  # (行，列，写入的内容)
                    worksheet.write(num, 1, API)
                    worksheet.write(num, 2, API+" example in Java")
                    worksheet.write(num, 3, API)
    workbook.save('KG2CodeData.xls')

def readCodeInfo():
    APIid=getAPIid()
    fw = open("code.txt", 'a')
    for i in range(1,67):
        for item in APIid:
            idnum=item[0]
            API=item[1]
            if int(idnum)==i:
                print(idnum, API)
                fw.write(idnum+"   "+API+'\n')
                c=0
                with open('code Info.txt', "r") as f:  # 设置文件对象
                    data=f.readlines()
                    for line in data:
                        lineitem=line.strip('\n').split("', '")
                        code=lineitem[1].replace(r"\r\n","\n")
                        codeAPIid=lineitem[2]
                        if codeAPIid==idnum:
                            print(code)
                            c+=1
                            fw.write("---------------example"+str(c)+"---------------\n")
                            fw.write(code+'\n')
                f.close()
    fw.close()
if __name__ == '__main__':
    writeAPItoExcel()
    # readCodeInfo()
