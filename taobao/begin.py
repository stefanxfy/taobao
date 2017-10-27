from scrapy import cmdline
#cmdline.execute("scrapy crawl taobaoScrapy".split())#执行一个爬虫
#cmdline.execute("scrapy genspider taobaoScrapy  taobao.com".split())# 自动创建一个名为myItcast的爬虫，并且要给一个域名范围
cmdline.execute("scrapy crawl taobaoScrapy -o tmail1.csv".split())
#cmdline.execute("scrapy shell 'http://hr.tencent.com/position.php?&start=0#a'".split())
#cmdline.execute(r"scrapy startproject D:\mypython\tencent".split())
'''
scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，，命令如下：

# json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json

# json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonl

# csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv

# xml格式
scrapy crawl itcast -o teachers.xml

'''