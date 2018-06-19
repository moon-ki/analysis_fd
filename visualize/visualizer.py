import pytagcloud
import os
import matplotlib.pyplot as plt
import collections

# RESULT_DIRECTORY='__results__/visualization'
def wordcloud(filename, wordfreq,result_vidualization_dir):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (result_vidualization_dir,filename)

    pytagcloud.create_tag_image(taglist,save_filename,
                                size=(900,600),
                                fontname='Malgun',
                                rectangular=False,
                                background=(0, 0, 0) )

# if os.path.exists(RESULT_DIRECTORY) is False:
#     print('create directory')
#     os.makedirs(RESULT_DIRECTORY)

def graph_bar(title=None, xlabel=None, ylabel=None, showgrid=False,
              values=None, ticks=None, filename=None, showgraph=True,result_vidualization_dir=''):

    fig, subplots= plt.subplots(1,1)
    subplots.bar(range(len(values)),values, align='center')#x축, y축 잡아춤

    #ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))#눈금을 몇개로 하겠는가?
        subplots.set_xticklabels(ticks, rotation=70, fontsize='xx-small') #rotation은 x축 항목의 기울기

    #title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    #xlabel
    if xlabel is not None and isinstance(xlabel, str):
        subplots.set_xlabel(xlabel)

    #ylabel
    if ylabel is not None and isinstance(ylabel, str):
        subplots.set_ylabel(ylabel)
        
    # show_grid
    subplots.grid(showgrid)

    #데이터 저장
    if filename is not None and isinstance(filename, str):#filename이 String 형태여야 한다.
        save_filename = '%s/bar_%s.png' % (result_vidualization_dir, filename)
        plt.savefig(save_filename,
                    dpi=400,#해상도
                    bbox_inches='tight'#여백이 없다.
        )

    #show graph
    if showgraph:
        plt.show()
