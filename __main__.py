import collect
import analyze
import visualize


if __name__ =='__main__':
    print('analysis_fd 프로젝트 __main__ 실행')
    items = [
        {'pageName': 'jtbcnews', 'since': '2018-01-01', 'until': '2018-06-14'},
        {'pageName': 'chosun', 'since': '2018-01-01', 'until': '2018-06-14'}
    ]
    #데이터 수집(collection)
    for item in items :
        resultfile = collect.crawling(**item, fetch= False)
        # *item은 튜블일 경우, **item은 딕셔너리일 경우
        item['resultfile'] = resultfile

    #데이터 분석
    for item in items:
        # print(item['resultfile'])
        data = analyze.json_to_str(item['resultfile'],'message')
        print(data)
        item['count_wordfreq']=analyze.count_wordfreq(data)
        print(item['count_wordfreq'])

    #데이터 시각화(visualize)

    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        filename = '%s_%s_%s' % (item['pageName'],item['since'],item['until'])
        visualize.wordcloud(filename,count_m50)
        visualize.graph_bar(
            title='%s 빈도 분석' % (item['pageName']),
            xlabel='단어',
            ylabel='빈도수',
            #딕셔너리 형태이므로 형변환 한다.
            values = list(count_m50.values()),   #value 값
            ticks = list(count_m50.keys()),     #축값을 key에서 받아옴
            showgrid = True,                    #그래프에 격자를 그릴지 여부
            filename=filename,
            showgraph = False                   #팝업윈도우를 띄울지 여부
        )



