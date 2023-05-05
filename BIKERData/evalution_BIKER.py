import xlrd

def read_BIKER_data_from_excel(path):
    BIKER_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,2)
            BIKER_All_Results_Rank = sheet.cell_value(i, 4)
            # print(query)
            # print(ground_truth)
            # print(str(BIKER_All_Results_Rank).split(','))
            rank_list=[]
            for rank in str(BIKER_All_Results_Rank).split(','):
                rank_list.append(int(float(rank)))
            temp_list=[]
            temp_list.append(rank_list)
            temp_list.append(len(ground_truth.split(' ')))
            BIKER_All_Results_Rank_list.append(tuple(temp_list))
    # print(nrows,ncols)
    print(BIKER_All_Results_Rank_list)

    return BIKER_All_Results_Rank_list

def read_Google_data_from_excel(path):
    Google_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,2)
            Google_All_Results_Rank = sheet.cell_value(i, ncols-2)
            # print(query)
            # print(ground_truth)
            # print(str(Google_All_Results_Rank).split(','))
            rank_list=[]
            for rank in str(Google_All_Results_Rank).split(','):
                rank_list.append(int(float(rank)))
            temp_list=[]
            temp_list.append(rank_list)
            temp_list.append(len(ground_truth.split(' ')))
            Google_All_Results_Rank_list.append(tuple(temp_list))
    # print(nrows,ncols)
    print(Google_All_Results_Rank_list)

    return Google_All_Results_Rank_list

def read_Bing_data_from_excel(path):
    Bing_All_Results_Rank_list=[]
    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_name('1')  # 获取读入的文件的sheet(名字的方式)
    #获取sheet的最大行数和列数
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    #获取某个单元格的值
    for i in range(nrows):
        # print("------------------" + str(i + 1) + "-------------------")
        if i>0:#第一行为表头，数据从第二行开始（i+1）
            query =sheet.cell_value(i,1)
            ground_truth=sheet.cell_value(i,2)
            Bing_All_Results_Rank = sheet.cell_value(i, ncols-1)
            # print(query)
            # print(ground_truth)
            # print(str(Bing_All_Results_Rank).split(','))
            rank_list=[]
            for rank in str(Bing_All_Results_Rank).split(','):
                rank_list.append(int(float(rank)))
            temp_list=[]
            temp_list.append(rank_list)
            temp_list.append(len(ground_truth.split(' ')))
            Bing_All_Results_Rank_list.append(tuple(temp_list))
    # print(nrows,ncols)
    print(Bing_All_Results_Rank_list)

    return Bing_All_Results_Rank_list

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
    all_ptop_k = 0.0
    all_top_k = 0.0
    zero_first = 0
    for i in range(len(data_list)):
        # print("------------------"+str(i+1)+"-------------------")
        temp_result = data_list[i][0] #data_list[i]=<data,truth_len>
        ground_truth_len = data_list[i][1]
        temp_mrr = 0.0
        temp_ptop_k = 0.0
        temp_ptop_k =len (temp_result)/10 #返回的是top-10
        all_ptop_k +=temp_ptop_k
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
    all_map = all_map / len(data_list)
    all_mrr = all_mrr / len(data_list)
    all_fr = all_fr / len(data_list)
    # all_ptop_k = all_ptop_k / len(data_list)
    all_top_k = (len(data_list)-zero_first) / len(data_list)
    print(str(len(data_list))+'个results的MAP、MRR、FR、Top@k：%.3f %.3f %.3f %.3f'%(all_map,all_mrr,all_fr,all_top_k))
    print("Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：%d %d"%(len(data_list)-zero_first,zero_first))

if __name__ == '__main__':
    path=r'D:/StackOverflow1/DataEvalation/BikerData/BIKER_data_results.xls'#413个results的MAP、MRR：3.305 0.915
    BIKER_data_list=read_BIKER_data_from_excel(path)
    compute_MRR_MAP(BIKER_data_list)
    #413个results的MAP、MRR、FR、Top@k：0.673 0.584 3.705 0.845
    # Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：349 64

    Google_data_list = read_Google_data_from_excel(path)
    compute_MRR_MAP(Google_data_list)
    #413个results的MAP、MRR、FR、Top@k：3.305 0.916 1.361 0.988
    #Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：408 5

    Bing_data_list = read_Bing_data_from_excel(path)
    compute_MRR_MAP(Bing_data_list)
    #413个results的MAP、MRR、FR、Top@k：3.177 0.861 1.584 0.969
    # Top-10个结果中能够返回查询的正确结果与返回失败的query个数分别为：400 13