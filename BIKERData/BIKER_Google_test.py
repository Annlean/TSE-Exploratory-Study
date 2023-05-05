from algorithm import recommendation
from preprocess import read_data
from lxml import etree
from nltk.stem import SnowballStemmer
from algorithm import similarity
from nltk.tokenize import WordPunctTokenizer
import gensim
import pickle as pickle
from bs4 import BeautifulSoup
import util
import time

#python2 由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换。
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

#python3 有了明确的str和byte类型区别，从一种类型转换成另一种类型要显式指定encoding。
import importlib,sys
importlib.reload(sys)

w2v = gensim.models.Word2Vec.load('../data/w2v_model_stemmed') # pre-trained word embedding
idf = pickle.load(open('../data/idf','rb')) # pre-trained idf value of all words in the w2v dictionary
questions = pickle.load(open('../data/api_questions_pickle_new', 'rb')) # the pre-trained knowledge base of api-related questions (about 120K questions)
questions = recommendation.preprocess_all_questions(questions, idf, w2v) # matrix transformation
javadoc = pickle.load(open('../data/javadoc_pickle_wordsegmented','rb')) # the pre-trained knowledge base of javadoc
javadoc_dict_classes = dict()
javadoc_dict_methods = dict()
recommendation.preprocess_javadoc(javadoc,javadoc_dict_classes,javadoc_dict_methods,idf,w2v) # matrix transformation
parent = pickle.load(open('../data/parent', 'rb')) # parent is a dict(), which stores the ids of each query's duplicate questions


querys = read_data.read_querys_from_file()
#querys = querys[:10]

print('loading data finished')
def main_test(querys):
    mrr = 0.0
    map = 0.0
    tot = 0

    from xlwt import Workbook
    # 创建一个工作簿
    w = Workbook()
    # 创建一个工作表
    ws = w.add_sheet('1',cell_overwrite_ok=True)
    # 行数
    link_nums = len(querys)
    for j in range(len(querys)):
        item=querys[j]
        query = item[0]
        true_apis = item[1]

        true_apis_str = ''
        for api in true_apis:
            true_apis_str = true_apis_str + api + ','
        true_apis_str = true_apis_str[:len(true_apis_str) - 1]

        query_words = WordPunctTokenizer().tokenize(query.lower())
        query_words = [SnowballStemmer('english').stem(word) for word in query_words]

        query_matrix = similarity.init_doc_matrix(query_words, w2v)
        query_idf_vector = similarity.init_doc_idf_vector(query_words, idf)
        top_questions = recommendation.get_topk_questions(query, query_matrix, query_idf_vector, questions, 50, parent)
        recommended_api = recommendation.recommend_api(query_matrix, query_idf_vector, top_questions, questions, javadoc,javadoc_dict_methods,-1)


        #recommended_api = recommendation.recommend_api_baseline(query_matrix,query_idf_vector,javadoc,-1)

        pos = -1
        tmp_map = 0.0
        hits = 0.0
        print('\n\n######  输入问题：' + query+'   推荐列表长度：'+str(len(recommended_api)))
        print(true_apis)
        all_true_api_rank=[]#推荐列表中所有正确推荐的结果Rank
        first_true_api_rank=0#第一个推荐正确的推荐结果Rank
        for i,api in enumerate(recommended_api):
            if api in true_apis and pos == -1:
                pos = i+1 #使分母不为0
            if api in true_apis:
                hits += 1
                tmp_map += hits/(i+1)
                print('Rank', i+1, ':', api)#输出真实API所在的推荐列表排名
                #推荐的真实API相关的补充信息
                recommendation.summarize_api_method(api, top_questions, questions, javadoc, javadoc_dict_methods)#
                all_true_api_rank.append(i+1)
            if i==9:#只搜索推荐列表前10个推荐结果
                break#

        if len(all_true_api_rank)>0:
            first_true_api_rank=all_true_api_rank[0]

        all_true_api_rank_str = ''
        if len(all_true_api_rank) > 0:
            for true_rank in all_true_api_rank:
                all_true_api_rank_str = all_true_api_rank_str + str(true_rank) + ','
            all_true_api_rank_str = all_true_api_rank_str[:len(all_true_api_rank_str) - 1]
        else:
            all_true_api_rank_str='0'

        ws.write(j , 0, j + 1)  # 第一列
        ws.write(j , 1, query)  # 第二列
        ws.write(j , 2, true_apis_str)
        ws.write(j , 3, first_true_api_rank)
        ws.write(j , 4, all_true_api_rank_str)
        tmp_map /= len(true_apis)
        tmp_mrr = 0.0
        if pos!=-1:
            tmp_mrr = 1.0/pos#第n个匹配分数为1/n

        map += tmp_map
        mrr += tmp_mrr
        print(tmp_mrr, tmp_map, hits)
        #若推荐API正确的个数>1,就输出推荐的前10个API
        # if hits>1:
        #     print(tmp_mrr,tmp_map,pos,query,true_apis,len(recommended_api),hits)
        #     print(tmp_mrr / len(querys), len(querys))
        #     print(tmp_map / len(querys))
        #     for i, api in enumerate(recommended_api):
        #         print('Rank', i + 1, ':', api)
        #         recommendation.summarize_api_method(api, top_questions, questions, javadoc, javadoc_dict_methods)  #
        #         if i == 9:
        #             break
    print('\n'+str(len(querys))+"个query的MRR、MAP值为：")
    print(mrr/len(querys))
    print (map/len(querys))
    w.save('test result.xls')


def test(querys):
    mrr = 0.0
    map = 0.0

    for j in range(len(querys)):
        item = querys[j]
        query = item[0]
        true_apis = item[1]

        true_apis_str = ''
        for api in true_apis:
            true_apis_str = true_apis_str + api + ','
        true_apis_str = true_apis_str[:len(true_apis_str) - 1]

        query_words = WordPunctTokenizer().tokenize(query.lower())
        query_words = [SnowballStemmer('english').stem(word) for word in query_words]

        query_matrix = similarity.init_doc_matrix(query_words, w2v)
        query_idf_vector = similarity.init_doc_idf_vector(query_words, idf)
        top_questions = recommendation.get_topk_questions(query, query_matrix, query_idf_vector, questions, 50, parent)
        recommended_api = recommendation.recommend_api(query_matrix, query_idf_vector, top_questions, questions,
                                                       javadoc, javadoc_dict_methods, -1)

        # recommended_api = recommendation.recommend_api_baseline(query_matrix,query_idf_vector,javadoc,-1)

        pos = -1
        tmp_map = 0.0
        hits = 0.0
        print('\n\n######  输入问题：' + query + '   推荐列表长度：' + str(len(recommended_api)))
        print(true_apis)
        print(len(true_apis))
        all_true_api_rank = []  # 推荐列表中所有正确推荐的结果Rank
        first_true_api_rank = 0  # 第一个推荐正确的推荐结果Rank
        for i, api in enumerate(recommended_api):
            if api in true_apis and pos == -1:
                pos = i + 1  # 使分母不为0
            if api in true_apis:
                hits += 1
                tmp_map += hits / (i + 1)
                print(hits,i+1)
                print('Rank', i + 1, ':', api)  # 输出真实API所在的推荐列表排名
                # 推荐的真实API相关的补充信息
                recommendation.summarize_api_method(api, top_questions, questions, javadoc, javadoc_dict_methods)  #
                all_true_api_rank.append(i + 1)
            if i == 9:  # 只搜索推荐列表前10个推荐结果
                break  #
        print(tmp_map)
        tmp_map /= len(true_apis)
        tmp_mrr = 0.0
        if pos != -1:
            tmp_mrr = 1.0 / pos  # 第n个匹配分数为1/n
        print(tmp_mrr, tmp_map, hits)

        map += tmp_map
        mrr += tmp_mrr

        # 若推荐API正确的个数>1,就输出推荐的前10个API
        # if hits>1:
        #     print(tmp_mrr,tmp_map,pos,query,true_apis,len(recommended_api),hits)
        #     print(tmp_mrr / len(querys), len(querys))
        #     print(tmp_map / len(querys))
        #     for i, api in enumerate(recommended_api):
        #         print('Rank', i + 1, ':', api)
        #         recommendation.summarize_api_method(api, top_questions, questions, javadoc, javadoc_dict_methods)  #
        #         if i == 9:
        #             break
    print('\n' + str(len(querys)) + "个query的MRR、MAP值为：")
    print(mrr / len(querys))
    print(map / len(querys))
if __name__ == '__main__':
    test(querys)
