#Sheet1 is the latest data
import xlrd

def read_Google_data_from_excel(path):
    Google_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,4)
            Google_All_Results_Rank = str(sheet.cell_value(i, 7))
            # print("第"+str(i)+"个："+query)

            if Google_All_Results_Rank !=' -':
                rank_list = []
                for rank in Google_All_Results_Rank.split(','):
                    rank_list.append(int(float(rank)))
                # print(rank_list)
                temp_list=[]
                temp_list.append(rank_list)
                temp_list.append(len(ground_truth.split(',')))
                Google_All_Results_Rank_list.append(tuple(temp_list))
    # print(len(Google_All_Results_Rank_list))

    return Google_All_Results_Rank_list

def read_Bing_data_from_excel(path):
    Bing_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,4)
            Bing_All_Results_Rank = str(sheet.cell_value(i, 8))
            # print("第" + str(i) + "个：" + query)

            if Bing_All_Results_Rank != ' -':
                rank_list = []
                for rank in Bing_All_Results_Rank.split(','):
                    rank_list.append(int(float(rank)))
                # print(rank_list)
                temp_list=[]
                temp_list.append(rank_list)
                temp_list.append(len(ground_truth.split(',')))
                Bing_All_Results_Rank_list.append(tuple(temp_list))
    # print(len(Bing_All_Results_Rank_list))

    return Bing_All_Results_Rank_list

def read_BIKER_data_from_excel(path):
    BIKER_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,4)
            BIKER_All_Results_Rank = str(sheet.cell_value(i, 9))
            # print("第" + str(i) + "个：" + query)

            if BIKER_All_Results_Rank != ' -':
                rank_list = []
                for rank in BIKER_All_Results_Rank.split(','):
                    rank_list.append(int(float(rank)))
                # print(rank_list)
                temp_list=[]
                temp_list.append(rank_list)
                temp_list.append(len(ground_truth.split(',')))
                BIKER_All_Results_Rank_list.append(tuple(temp_list))

    # print(len(BIKER_All_Results_Rank_list))
    return BIKER_All_Results_Rank_list

# def read_CROKAGE_data_from_excel(path):
#     CROKAGE_All_Results_Rank_list=[]
#     readbook = xlrd.open_workbook(path)
#     sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
#     #获取sheet的最大行数和列数
#     nrows = sheet.nrows  # 行
#     ncols = sheet.ncols  # 列
#     #获取某个单元格的值
#     for i in range(nrows):
#         # print("------------------" + str(i + 1) + "-------------------")
#         if i>0:#第一行为表头，数据从第二行开始（i+1）
#             query =sheet.cell_value(i,1)
#             ground_truth=sheet.cell_value(i,4)
#             CROKAGE_All_Results_Rank = str(sheet.cell_value(i, 10))
#             # print("第" + str(i) + "个：" + query)
#
#             if CROKAGE_All_Results_Rank != ' -':
#                 rank_list = []
#                 for rank in CROKAGE_All_Results_Rank.split(','):
#                     rank_list.append(int(float(rank)))
#                 # print(rank_list)
#                 temp_list=[]
#                 temp_list.append(rank_list)
#                 temp_list.append(len(ground_truth.split(',')))
#                 CROKAGE_All_Results_Rank_list.append(tuple(temp_list))
#     # print(len(CROKAGE_All_Results_Rank_list))
#     return CROKAGE_All_Results_Rank_list

def read_CROKAGE_data_from_excel(path):
    CROKAGE_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,4)
            CROKAGE_All_Results_Rank = str(sheet.cell_value(i, 10))
            # print("第" + str(i) + "个：" + query)

            if CROKAGE_All_Results_Rank != ' -':
                rank_list = []
                for rank in CROKAGE_All_Results_Rank.split(','):
                    rank_list.append(int(float(rank)))
                # print(rank_list)
                temp_list=[]
                temp_list.append(rank_list)
                temp_list.append(len(ground_truth.split(',')))
                CROKAGE_All_Results_Rank_list.append(tuple(temp_list))
    # print(len(CROKAGE_All_Results_Rank_list))
    return CROKAGE_All_Results_Rank_list
def read_ADECK_data_from_excel(path):
    ADECK_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('Sheet1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,4)
            ADECK_All_Results_Rank = str(sheet.cell_value(i, 11))
            # print("第" + str(i) + "个：" + query+str(ADECK_All_Results_Rank))

            if ADECK_All_Results_Rank != ' -':
                rank_list = []
                for rank in ADECK_All_Results_Rank.split(','):
                    rank_list.append(int(float(rank)))
                # print(rank_list)
                temp_list=[]
                temp_list.append(rank_list)
                temp_list.append(len(ground_truth.split(',')))
                ADECK_All_Results_Rank_list.append(tuple(temp_list))
    # print(len(ADECK_All_Results_Rank_list))
    return ADECK_All_Results_Rank_list

def AP(true_ranked_list, ground_truth_len):
    temp_map = 0
    for n in range(len(true_ranked_list)):
        temp_map += (n+1) / true_ranked_list[n]
    if true_ranked_list[0] > 0:
        return (temp_map / ground_truth_len)
    else:
        return 0

def compute_MRR_MAP(data_list):
    all_map = 0.0
    all_mrr = 0.0
    all_fr = 0.0
    all_top_k = 0.0
    zero_first = 0
    for i in range(len(data_list)):
        # print("------------------"+str(i+1)+"-------------------")
        temp_result = data_list[i][0] #data_list[i]=<data,truth_len>
        ground_truth_len = data_list[i][1]
        temp_mrr = 0.0
        # print(temp_result,ground_truth_len)
        first=temp_result[0]
        if first>0:#若为0即为无相关结果
            temp_mrr = 1.0 / first # 第n个匹配分数为1/n
            all_fr += first
            temp_map = AP(temp_result, ground_truth_len)
            all_map += temp_map
            # print('第' + str(i + 1) + '个result的MAP、MRR：%.3f %.3f' % (temp_map, temp_mrr))
        else:
            temp_mrr = 1.0 / 11  # 无返回结果时，设置firstRank=11
            all_fr += 11
            zero_first+=1
        all_mrr += temp_mrr
    if len(data_list)>0:
        all_map = all_map / len(data_list)
        all_mrr = all_mrr / len(data_list)
        all_fr = all_fr / len(data_list)

        all_top_k = (len(data_list)-zero_first) / len(data_list)  #5个无法获取真实API的典型案例
    print(str(len(data_list))+'个典型案例的MAP、MRR、FR、Top@k：%.3f %.3f %.3f %.3f'%(all_map,all_mrr,all_fr,all_top_k))
    print("Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：%d %d  \n\n"%(len(data_list)-zero_first,zero_first))

if __name__ == '__main__':
    path = r'D:/StackOverflow1/DataEvaluation/classic_case/Classical.xls'

    Google_data_list = read_Google_data_from_excel(path)
    compute_MRR_MAP(Google_data_list)

    Bing_data_list = read_Bing_data_from_excel(path)
    compute_MRR_MAP(Bing_data_list)

    BIKER_data_list = read_BIKER_data_from_excel(path)
    compute_MRR_MAP(BIKER_data_list)

    CROKAGE_data_list = read_CROKAGE_data_from_excel(path)
    compute_MRR_MAP(CROKAGE_data_list)

    ADECK_data_list = read_ADECK_data_from_excel(path)
    compute_MRR_MAP(ADECK_data_list)

# 77个典型案例的MAP、MRR、FR、Top@k：5.520 0.975 1.156 0.987
# Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：76 1
#
# 77个典型案例的MAP、MRR、FR、Top@k：4.529 0.935 1.351 0.974
# Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：75 2
#
# 68个典型案例的MAP、MRR、FR、Top@k：0.446 0.419 6.382 0.529
# Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：36 32
#
# 68个典型案例的MAP、MRR、FR、Top@k：2.820 0.651 3.574 0.838
# Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：57 11
#
# 0个典型案例的MAP、MRR、FR、Top@k：0.000 0.000 0.000 0.000
# Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：0 0









