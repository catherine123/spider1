from datetime import datetime
from scrapy.http import Request
#from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.utils import response
from datetime import datetime, timedelta
from yhd2.items import Yhd2Item
from scrapy.item import Item
import re
from scrapy.spider import Spider
from scrapy.selector import Selector
#import json
from bs4 import BeautifulSoup
#from scrapy.selector import Selector
# from scrapy import log
from scrapy.spider import Spider
import json
import sys
import urllib2
from twisted.python.log import PythonLoggingObserver
from scrapy import log, Request
import requests

class MySpider(Spider):
    name = "yhd2"
    def __init__(self, name=None, **kwargs):
    # TODO: configure logging: e.g. logging.config.fileConfig("logging.conf")
        observer = PythonLoggingObserver()
        observer.start()


    allowed_domains = ["yhd.com"]
    start_urls = [


# Dec 17 2014
# fruits, most imported,
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=66995&provinceId=1&productid=3029&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8197029&provinceId=1&productid=4177547&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=36758723&provinceId=1&productid=31353523&merchantId=1",
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2511107&provinceId=1&productid=2317870&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13210279&provinceId=1&productid=11809527&merchantId=1",
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8597063&provinceId=1&productid=7465868&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23287558&merchantId=62090&subProductId=23287558&category=0&currSiteId=1&pmid=27371021&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=40558505&provinceId=1&productid=34758600&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=104806&provinceId=1&productid=38927&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=37292836&provinceId=1&productid=31838950&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27891613&merchantId=118701&subProductId=27891613&category=0&currSiteId=1&pmid=32790605&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15509492&merchantId=5033&subProductId=15509492&category=0&currSiteId=1&pmid=17751657&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27923621&merchantId=118701&subProductId=27923621&category=0&currSiteId=1&pmid=32830098&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34300772&merchantId=23922&subProductId=34300772&category=0&currSiteId=1&pmid=40032806&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34981215&merchantId=23922&subProductId=34981215&category=0&currSiteId=1&pmid=40846875&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34601325&merchantId=118701&subProductId=34601325&category=0&currSiteId=1&pmid=40381888&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32439627&merchantId=101126&subProductId=32439627&category=0&currSiteId=1&pmid=37948653&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=20913410&merchantId=86844&subProductId=20913410&category=0&currSiteId=1&pmid=24662085&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8426550&merchantId=12733&subProductId=8426550&category=0&currSiteId=1&pmid=9592777&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35825426&merchantId=80172&subProductId=35825426&category=0&currSiteId=1&pmid=41867605&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35862749&merchantId=80172&subProductId=35862749&category=0&currSiteId=1&pmid=41913198&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=36042816&merchantId=23922&subProductId=36042816&category=0&currSiteId=1&pmid=42136042&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33791200&merchantId=965&subProductId=33791200&category=0&currSiteId=1&pmid=39454752&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16628236&merchantId=6586&subProductId=16628236&category=0&currSiteId=1&pmid=19264535&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25476524&merchantId=74451&subProductId=25476524&category=0&currSiteId=1&pmid=29906104&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31333623&merchantId=105364&subProductId=31333623&category=0&currSiteId=1&pmid=36734802&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31248029&merchantId=128900&subProductId=31248029&category=0&currSiteId=1&pmid=36639728&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28295598&merchantId=99807&subProductId=28295598&category=0&currSiteId=1&pmid=33280763&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32345186&merchantId=85740&subProductId=32345186&category=0&currSiteId=1&pmid=37844456&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31396864&merchantId=134362&subProductId=31396864&category=0&currSiteId=1&pmid=36805657&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35535865&merchantId=15135&subProductId=35535865&category=0&currSiteId=1&pmid=41526380&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16935134&merchantId=55311&subProductId=16935134&category=0&currSiteId=1&pmid=19663052&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32860607&merchantId=105364&subProductId=32860607&category=0&currSiteId=1&pmid=38400068&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34957390&merchantId=105364&subProductId=34957390&category=0&currSiteId=1&pmid=40812319&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35206964&merchantId=134457&subProductId=35206964&category=0&currSiteId=1&pmid=41127352&showNum=20",

# end of part 1 on Dec17 2014
# part2 Dec17 2014
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16303025&merchantId=39489&subProductId=16303025&category=0&currSiteId=1&pmid=18826393&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=11970420&merchantId=39489&subProductId=11970420&category=0&currSiteId=1&pmid=13379550&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1094888&merchantId=1&subProductId=1094888&category=0&currSiteId=1&pmid=1442523&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25483&merchantId=1&subProductId=25483&category=0&currSiteId=1&pmid=97814&showNum=20",


"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=12137115&merchantId=3801&subProductId=12137115&category=0&currSiteId=1&pmid=13556534&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=2391721&merchantId=5296&subProductId=2391721&category=0&currSiteId=1&pmid=2585380&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=16259152&merchantId=1&currSiteId=1&pmid=18771013",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=18771013&provinceId=1&productid=16259152&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16259152&merchantId=1&subProductId=16259152&category=0&currSiteId=1&pmid=18771013&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=2260969&merchantId=1&subProductId=2260969&category=0&currSiteId=1&pmid=2459230&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=2260969&merchantId=1&currSiteId=1&pmid=2459230",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2459230&provinceId=1&productid=2260969&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1194463&merchantId=1&subProductId=1194463&category=0&currSiteId=1&pmid=1414116&showNum=20",

#deleted Dec 19

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1414116&provinceId=1&productid=1194463&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27874505&merchantId=73363&subProductId=27874505&category=0&currSiteId=1&pmid=32769818&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24403684&merchantId=1571&subProductId=24403684&category=0&currSiteId=1&pmid=28658180&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=19340518&merchantId=21937&subProductId=19340518&category=0&currSiteId=1&pmid=22819031&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24951222&merchantId=1&subProductId=24951222&category=0&currSiteId=1&pmid=29290456&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=24951222&merchantId=1&currSiteId=1&pmid=29290456",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=29290456&provinceId=1&productid=24951222&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32179603&merchantId=133647&subProductId=32179603&category=0&currSiteId=1&pmid=37659637",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17234604&merchantId=60833&subProductId=17234604&category=0&currSiteId=1&pmid=20056833&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=6831137&merchantId=11971&subProductId=6831137&category=0&currSiteId=1&pmid=7915685&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32409641&merchantId=112530&subProductId=32409641&category=0&currSiteId=1&pmid=37916866&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=14097440&merchantId=17727&subProductId=14097440&category=0&currSiteId=1&pmid=15969021&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35167051&merchantId=4763&subProductId=35167051&category=0&currSiteId=1&pmid=41080057&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4076769&merchantId=1&currSiteId=1&pmid=4930600",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4930600&provinceId=1&productid=4076769&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4076769&merchantId=1&subProductId=4076769&category=0&currSiteId=1&pmid=4930600&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7100682&merchantId=10684&subProductId=7100682&category=0&currSiteId=1&pmid=8202350&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35880713&merchantId=116615&subProductId=35880713&category=0&currSiteId=1&pmid=41934220&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=34104016&merchantId=1&currSiteId=1&pmid=39861501",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=39861501&provinceId=1&productid=34104016&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=7216297&merchantId=1&currSiteId=1&pmid=8322965",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8322965&provinceId=1&productid=7216297&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=900150&merchantId=1&currSiteId=1&pmid=961268",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=961268&provinceId=1&productid=900150&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=900150&merchantId=1&subProductId=900150&category=0&currSiteId=1&pmid=961268&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=14668&merchantId=1&currSiteId=1&pmid=89900",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=89900&provinceId=1&productid=14668&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=14668&merchantId=1&subProductId=14668&category=0&currSiteId=1&pmid=89900&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10504&merchantId=1&currSiteId=1&pmid=74133",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=74133&provinceId=1&productid=10504&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10504&merchantId=1&subProductId=10504&category=0&currSiteId=1&pmid=74133&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30946336&merchantId=1&subProductId=30946336&category=0&currSiteId=1&pmid=36299778&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=30946336&merchantId=1&currSiteId=1&pmid=36299778",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=36299778&provinceId=1&productid=30946336&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4054485&merchantId=1756&subProductId=4054485&category=0&currSiteId=1&pmid=4179445&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=25899639&provinceId=1&productid=21998132&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=21998132&merchantId=1&currSiteId=1&pmid=25899639",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=21998132&merchantId=1&subProductId=21998132&category=0&currSiteId=1&pmid=25899639&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4146597&merchantId=1&currSiteId=1&pmid=4266371",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4266371&provinceId=1&productid=4146597&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4146597&merchantId=1&subProductId=4146597&category=0&currSiteId=1&pmid=4266371&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=5586928&merchantId=1&currSiteId=1&pmid=6611371",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=6611371&provinceId=1&productid=5586928&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27100202&merchantId=1&subProductId=27100202&category=0&currSiteId=1&pmid=31836768&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=27100202&merchantId=1&currSiteId=1&pmid=31836768",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31836768&provinceId=1&productid=27100202&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10063184&merchantId=1&currSiteId=1&pmid=11348578",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11348578&provinceId=1&productid=10063184&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10063184&merchantId=1&subProductId=10063184&category=0&currSiteId=1&pmid=11348578&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16227481&merchantId=53454&subProductId=16227481&category=0&currSiteId=1&pmid=18729767&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=72796&provinceId=1&productid=8967&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8967&merchantId=1&currSiteId=1&pmid=72796",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34270481&merchantId=113581&subProductId=34270481&category=0&currSiteId=1&pmid=39998634&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34996233&merchantId=1&subProductId=34996233&category=0&currSiteId=1&pmid=40865564&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=40865564&provinceId=1&productid=34996233&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=40865564&provinceId=1&productid=34996233&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=20650&merchantId=1&subProductId=20650&category=0&currSiteId=1&pmid=94310&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=20650&merchantId=1&currSiteId=1&pmid=94310",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=94310&provinceId=1&productid=20650&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1172487&merchantId=1&subProductId=1172487&category=0&currSiteId=1&pmid=1354683&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1172487&merchantId=1&currSiteId=1&pmid=1354683",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1354683&provinceId=1&productid=1172487&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5608284&merchantId=15889&subProductId=5608284&category=0&currSiteId=1&pmid=6634496&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=26690811&merchantId=107561&subProductId=26690811&category=0&currSiteId=1&pmid=31353425&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=12368137&merchantId=21630&subProductId=12368137&category=0&currSiteId=1&pmid=13796902&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4942014&merchantId=1&currSiteId=1&pmid=5004727",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=5004727&provinceId=1&productid=4942014&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1105039&merchantId=1&currSiteId=1&pmid=1271338",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1271338&provinceId=1&productid=1105039&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24553223&merchantId=1&subProductId=24553223&category=0&currSiteId=1&pmid=28830922&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=24553223&merchantId=1&currSiteId=1&pmid=28830922",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=28830922&provinceId=1&productid=24553223&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=6641253&merchantId=5710&subProductId=6641253&category=0&currSiteId=1&pmid=7718024&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=17477&merchantId=1&currSiteId=1&pmid=91988",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=91988&provinceId=1&productid=17477&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31425723&provinceId=1&productid=26749285&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=26749285&merchantId=1&currSiteId=1&pmid=31425723",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=26749285&merchantId=1&subProductId=26749285&category=0&currSiteId=1&pmid=31425723&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=964840&merchantId=1&subProductId=964840&category=0&currSiteId=1&pmid=995689&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=964840&merchantId=1&currSiteId=1&pmid=995689",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=995689&provinceId=1&productid=964840&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4836642&merchantId=11919&subProductId=4836642&category=0&currSiteId=1&pmid=4907504&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17793538&merchantId=64664&subProductId=17793538&category=0&currSiteId=1&pmid=20972332&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17079882&merchantId=21630&subProductId=17079882&category=0&currSiteId=1&pmid=19853491&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10641734&merchantId=1&currSiteId=1&pmid=12004395",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=12004395&provinceId=1&productid=10641734&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10641734&merchantId=1&subProductId=10641734&category=0&currSiteId=1&pmid=12004395&showNum=20",


# Dec 17 2014 20:03 pm
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33870801&merchantId=106744&subProductId=33870804&category=0&currSiteId=1&pmid=39545687&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35094726&merchantId=13336&subProductId=35094809&category=0&currSiteId=1&pmid=40992701&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34951684&merchantId=79366&subProductId=34951687&category=0&currSiteId=1&pmid=40805172&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30004780&merchantId=25567&subProductId=30004788&category=0&currSiteId=1&pmid=35213589&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4628733&merchantId=4885&subProductId=4628734&category=0&currSiteId=1&pmid=4715441&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=14255400&merchantId=1749&subProductId=14255401&category=0&currSiteId=1&pmid=16169923&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34573296&merchantId=3281&subProductId=34573299&category=0&currSiteId=1&pmid=40348113&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31625703&merchantId=91425&subProductId=31625718&category=0&currSiteId=1&pmid=37063130&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30490986&merchantId=120728&subProductId=30491009&category=0&currSiteId=1&pmid=35781143&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32121266&merchantId=91425&subProductId=32121269&category=0&currSiteId=1&pmid=37594320&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35762592&merchantId=94143&subProductId=35762596&category=0&currSiteId=1&pmid=41789000&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31700849&merchantId=94494&subProductId=31700854&category=0&currSiteId=1&pmid=37145190&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33983066&merchantId=13336&subProductId=33983075&category=0&currSiteId=1&pmid=39669174&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31917223&merchantId=7469&subProductId=31917228&category=0&currSiteId=1&pmid=37374357&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34141477&merchantId=99082&subProductId=34141480&category=0&currSiteId=1&pmid=39851894&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35635560&merchantId=131093&subProductId=35635563&category=0&currSiteId=1&pmid=41640626&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32845411&merchantId=2132&subProductId=32845415&category=0&currSiteId=1&pmid=38383324&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=14827655&merchantId=66613&subProductId=14827657&category=0&currSiteId=1&pmid=16894448&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31378303&merchantId=8610&subProductId=31378307&category=0&currSiteId=1&pmid=36785964&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32342175&merchantId=87047&subProductId=32342183&category=0&currSiteId=1&pmid=37841234&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34156635&merchantId=73416&subProductId=34156642&category=0&currSiteId=1&pmid=39868659&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16354874&merchantId=71912&subProductId=16354879&category=0&currSiteId=1&pmid=18890692&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7071210&merchantId=19258&subProductId=7071214&category=0&currSiteId=1&pmid=8171957&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30226631&merchantId=5206&subProductId=30226634&category=0&currSiteId=1&pmid=35463534&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15683164&merchantId=48944&subProductId=15683175&category=0&currSiteId=1&pmid=17973155&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30073680&merchantId=33565&subProductId=30073686&category=0&currSiteId=1&pmid=35291391&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33116827&merchantId=122512&subProductId=33116831&category=0&currSiteId=1&pmid=38688112&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13984911&merchantId=39126&subProductId=13984913&category=0&currSiteId=1&pmid=15830425&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34265427&merchantId=32503&subProductId=34265447&category=0&currSiteId=1&pmid=39992154&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31674783&merchantId=128537&subProductId=31674790&category=0&currSiteId=1&pmid=37116890&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35209918&merchantId=85898&subProductId=35209922&category=0&currSiteId=1&pmid=41130662&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=21460888&merchantId=45482&subProductId=21460901&category=0&currSiteId=1&pmid=25297591&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29413262&merchantId=85257&subProductId=29413268&category=0&currSiteId=1&pmid=34558197&showNum=20",

## 2015_01_04 end
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33765150&merchantId=75590&subProductId=33765166&category=0&currSiteId=1&pmid=39423388&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30468240&merchantId=87575&subProductId=30468248&category=0&currSiteId=1&pmid=35754307&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28150107&merchantId=121702&subProductId=28150118&category=0&currSiteId=1&pmid=33103626&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13869416&merchantId=59772&subProductId=33428062&category=0&currSiteId=1&pmid=39041982&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30405739&merchantId=25422&subProductId=30405743&category=0&currSiteId=1&pmid=35685021&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16172779&merchantId=59772&subProductId=34523937&category=0&currSiteId=1&pmid=40291243&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33251100&merchantId=5702&subProductId=33251117&category=0&currSiteId=1&pmid=38842228&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5353395&merchantId=5584&subProductId=5353410&category=0&currSiteId=1&pmid=6359741&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7358943&merchantId=24186&subProductId=11696862&category=0&currSiteId=1&pmid=13094988&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17867290&merchantId=1371&subProductId=17867299&category=0&currSiteId=1&pmid=21069023&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31525489&merchantId=5916&subProductId=31525507&category=0&currSiteId=1&pmid=36950901&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32734032&merchantId=82878&subProductId=32734033&category=0&currSiteId=1&pmid=38263100&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31562021&merchantId=82878&subProductId=31562042&category=0&currSiteId=1&pmid=36994363&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33193957&merchantId=81455&subProductId=33193960&category=0&currSiteId=1&pmid=38775100&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34051580&merchantId=81455&subProductId=34051587&category=0&currSiteId=1&pmid=39747253&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30972101&merchantId=81455&subProductId=30972102&category=0&currSiteId=1&pmid=36328480&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31074013&merchantId=100731&subProductId=31074024&category=0&currSiteId=1&pmid=36445661&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16614939&merchantId=9149&subProductId=16614941&category=0&currSiteId=1&pmid=19249023&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10171488&merchantId=48704&subProductId=10171505&category=0&currSiteId=1&pmid=11446865&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16045679&merchantId=70865&subProductId=16045696&category=0&currSiteId=1&pmid=18492040&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16612534&merchantId=39620&subProductId=16612535&category=0&currSiteId=1&pmid=19246123&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23742317&merchantId=74289&subProductId=26017267&category=0&currSiteId=1&pmid=30548402&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=36075220&merchantId=98779&subProductId=36075222&category=0&currSiteId=1&pmid=42174429&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16862804&merchantId=25713&subProductId=16862813&category=0&currSiteId=1&pmid=19565511&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30826763&merchantId=36544&subProductId=30826767&category=0&currSiteId=1&pmid=36159345&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35601166&merchantId=94494&subProductId=35601181&category=0&currSiteId=1&pmid=41606095&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34439953&merchantId=3301&subProductId=34439979&category=0&currSiteId=1&pmid=40192624&showNum=20",



"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16452620&merchantId=68416&subProductId=16749807&category=0&currSiteId=1&pmid=19424324&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13431970&merchantId=26806&subProductId=13431981&category=0&currSiteId=1&pmid=15016247&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5521556&merchantId=16595&subProductId=5521577&category=0&currSiteId=1&pmid=6544297&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32857216&merchantId=58952&subProductId=32857236&category=0&currSiteId=1&pmid=38396428&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33266751&merchantId=135402&subProductId=33266754&category=0&currSiteId=1&pmid=38861751&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=21665127&merchantId=13318&subProductId=21665132&category=0&currSiteId=1&pmid=25533353&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35325630&merchantId=115122&subProductId=35325633&category=0&currSiteId=1&pmid=41275474&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30109282&merchantId=33565&subProductId=30109300&category=0&currSiteId=1&pmid=35332283&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30665511&merchantId=48944&subProductId=30665515&category=0&currSiteId=1&pmid=35978356&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32411520&merchantId=31668&subProductId=32411526&category=0&currSiteId=1&pmid=37918919&showNum=20",

# Dec 17 20:50 pm ends baby clothes.
# Dec 18 12:00 am starts here.
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=18021543&merchantId=81924&subProductId=18021545&category=0&currSiteId=1&pmid=21281238&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4438694&merchantId=7352&subProductId=4438697&category=0&currSiteId=1&pmid=4533065&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33442027&merchantId=96480&subProductId=33442038&category=0&currSiteId=1&pmid=39056973&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32490873&merchantId=87974&subProductId=32490877&category=0&currSiteId=1&pmid=38005312&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17714158&merchantId=1271&subProductId=28061691&category=0&currSiteId=1&pmid=32997557&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28664728&merchantId=66698&subProductId=28664748&category=0&currSiteId=1&pmid=33713958&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29027705&merchantId=83626&subProductId=29027710&category=0&currSiteId=1&pmid=34126655&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=14497995&merchantId=59149&subProductId=27688231&category=0&currSiteId=1&pmid=32541610&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=36103041&merchantId=25833&subProductId=36103047&category=0&currSiteId=1&pmid=42208499&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34439953&merchantId=3301&subProductId=34439979&category=0&currSiteId=1&pmid=40192624&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33903105&merchantId=78199&subProductId=33903113&category=0&currSiteId=1&pmid=39580801&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33581863&merchantId=68338&subProductId=33581910&category=0&currSiteId=1&pmid=39213494&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29300212&merchantId=4750&subProductId=34387457&category=0&currSiteId=1&pmid=40129761&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17940899&merchantId=2373&subProductId=17940900&category=0&currSiteId=1&pmid=21173213&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34308859&merchantId=73025&subProductId=34308864&category=0&currSiteId=1&pmid=40041264&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1718043&merchantId=2373&subProductId=1718048&category=0&currSiteId=1&pmid=1909839&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27305496&merchantId=70865&subProductId=27305499&category=0&currSiteId=1&pmid=32072360&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13551851&merchantId=7352&subProductId=13551866&category=0&currSiteId=1&pmid=15268040&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16835979&merchantId=70865&subProductId=31434071&category=0&currSiteId=1&pmid=36848855&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34324362&merchantId=80948&subProductId=34324363&category=0&currSiteId=1&pmid=40057875&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5158429&merchantId=5169&subProductId=16946586&category=0&currSiteId=1&pmid=19676898&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10719687&merchantId=9149&subProductId=10719694&category=0&currSiteId=1&pmid=12084203&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16019223&merchantId=51556&subProductId=16019224&category=0&currSiteId=1&pmid=18460074&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34199693&merchantId=81455&subProductId=34199695&category=0&currSiteId=1&pmid=39917038&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34727346&merchantId=111014&subProductId=34727349&category=0&currSiteId=1&pmid=40522657&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34479348&merchantId=101073&subProductId=34479351&category=0&currSiteId=1&pmid=40241746&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34727346&merchantId=111014&subProductId=34727349&category=0&currSiteId=1&pmid=40522657&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34770392&merchantId=111014&subProductId=34770394&category=0&currSiteId=1&pmid=40571286&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33334392&merchantId=111435&subProductId=33334415&category=0&currSiteId=1&pmid=38938458&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=21395992&merchantId=66189&subProductId=23525513&category=0&currSiteId=1&pmid=27639656&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16030134&merchantId=55392&subProductId=16030136&category=0&currSiteId=1&pmid=18472845&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7091517&merchantId=5187&subProductId=7091518&category=0&currSiteId=1&pmid=8193094&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=12000514&merchantId=38849&subProductId=12000516&category=0&currSiteId=1&pmid=13409882&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=3292715&merchantId=5187&subProductId=3292716&category=0&currSiteId=1&pmid=3451726&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17241669&merchantId=72787&subProductId=17241670&category=0&currSiteId=1&pmid=20069564&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28818169&merchantId=2156&subProductId=28818174&category=0&currSiteId=1&pmid=33889600&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30283003&merchantId=1531&subProductId=30283009&category=0&currSiteId=1&pmid=35526811&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=3752666&merchantId=8011&subProductId=3752667&category=0&currSiteId=1&pmid=3898162&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8458511&merchantId=1&currSiteId=1&pmid=9626757",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=9626757&provinceId=1&productid=8458511&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8458511&merchantId=1&subProductId=8458511&category=0&currSiteId=1&pmid=9626757&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13897700&merchantId=11060&subProductId=13897701&category=0&currSiteId=1&pmid=15712848&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34325855&merchantId=7486&subProductId=34325862&category=0&currSiteId=1&pmid=40059556&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33378285&merchantId=74512&subProductId=33378293&category=0&currSiteId=1&pmid=38986414&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5988990&merchantId=3821&subProductId=5988991&category=0&currSiteId=1&pmid=7028031&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=19581988&merchantId=85379&subProductId=19581991&category=0&currSiteId=1&pmid=23096456&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24872255&merchantId=95147&subProductId=24872256&category=0&currSiteId=1&pmid=29199611&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34186699&merchantId=37579&subProductId=34186701&category=0&currSiteId=1&pmid=39902508&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35204193&merchantId=142062&subProductId=35204202&category=0&currSiteId=1&pmid=41124135&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9251084&merchantId=26996&subProductId=9251085&category=0&currSiteId=1&pmid=10462881&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24798872&merchantId=37579&subProductId=24798879&category=0&currSiteId=1&pmid=29112339&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=2430717&merchantId=1531&subProductId=27518134&category=0&currSiteId=1&pmid=32326099&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=11509751&merchantId=49583&subProductId=11509752&category=0&currSiteId=1&pmid=12896314&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4059640&merchantId=6166&subProductId=23513754&category=0&currSiteId=1&pmid=27626679&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30426368&merchantId=86866&subProductId=30426374&category=0&currSiteId=1&pmid=35708086&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17867290&merchantId=1371&subProductId=17867299&category=0&currSiteId=1&pmid=21069023&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16584563&merchantId=72133&subProductId=16584565&category=0&currSiteId=1&pmid=19210723&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=20448178&merchantId=1531&subProductId=20448179&category=0&currSiteId=1&pmid=24123375&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29627564&merchantId=74782&subProductId=29627567&category=0&currSiteId=1&pmid=34794104&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10222250&merchantId=2373&subProductId=10222251&category=0&currSiteId=1&pmid=11500378&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31120149&merchantId=67421&subProductId=31120150&category=0&currSiteId=1&pmid=36498196&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34357061&merchantId=54515&subProductId=34357084&category=0&currSiteId=1&pmid=40096389&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=17926408&merchantId=1&currSiteId=1&pmid=13367897",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=24361076&merchantId=1&currSiteId=1&pmid=28606069",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24361076&merchantId=1&subProductId=24361076&category=0&currSiteId=1&pmid=28606069&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=28606069&provinceId=1&productid=24361076&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8794946&merchantId=1&currSiteId=1&pmid=9977914",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=9977914&provinceId=1&productid=8794946&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8794946&merchantId=1&subProductId=8794946&category=0&currSiteId=1&pmid=9977914&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=999909&merchantId=1&currSiteId=1&pmid=1046158",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1046158&provinceId=1&productid=999909&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=999909&merchantId=1&subProductId=999909&category=0&currSiteId=1&pmid=1046158&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=38467&merchantId=1&subProductId=38467&category=0&currSiteId=1&pmid=104304&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=38467&merchantId=1&currSiteId=1&pmid=104304",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=104304&provinceId=1&productid=38467&merchantId=1",

# Dec 18 ends here. 2014

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5051529&merchantId=1&subProductId=5051529&category=0&currSiteId=1&pmid=8143957&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=5051529&merchantId=1&currSiteId=1&pmid=8143957",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8143957&provinceId=1&productid=5051529&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25225630&merchantId=84558&subProductId=25225630&category=0&currSiteId=1&pmid=29607213&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30967676&merchantId=1&subProductId=30967676&category=0&currSiteId=1&pmid=36323575&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=36323575&provinceId=1&productid=30967676&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=30967676&merchantId=1&currSiteId=1&pmid=36323575",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=49090&merchantId=1&currSiteId=1&pmid=110171",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=110171&provinceId=1&productid=49090&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=43389&merchantId=1&currSiteId=1&pmid=106376",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=106376&provinceId=1&productid=43389&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=43389&merchantId=1&subProductId=43389&category=0&currSiteId=1&pmid=106376&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24565938&merchantId=6599&subProductId=24565938&category=0&currSiteId=1&pmid=28845492&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32295790&merchantId=91259&subProductId=32295790&category=0&currSiteId=1&pmid=37789177&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=10079900&provinceId=1&productid=8893048&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8893048&merchantId=1&currSiteId=1&pmid=10079900",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8893048&merchantId=1&subProductId=8893048&category=0&currSiteId=1&pmid=10079900&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10174214&merchantId=1&subProductId=10174214&category=0&currSiteId=1&pmid=11450010&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10174214&merchantId=1&currSiteId=1&pmid=11450010",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11450010&provinceId=1&productid=10174214&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=950082&merchantId=1&currSiteId=1&pmid=962370",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=962370&provinceId=1&productid=950082&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=950082&merchantId=1&subProductId=950082&category=0&currSiteId=1&pmid=962370&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=6488390&merchantId=405&subProductId=6488390&category=0&currSiteId=1&pmid=7555538&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17169403&merchantId=14133&subProductId=17169403&category=0&currSiteId=1&pmid=19968209&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=953126&merchantId=1&currSiteId=1&pmid=959205",

#"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=959205&provinceId=1&productid=953126&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=953126&merchantId=1&subProductId=953126&category=0&currSiteId=1&pmid=959205&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1169646&provinceId=1&productid=1044416&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1044416&merchantId=1&currSiteId=1&pmid=1169646",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1044416&merchantId=1&subProductId=1044416&category=0&currSiteId=1&pmid=1169646&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4866950&merchantId=1&currSiteId=1&pmid=4935563",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4935563&provinceId=1&productid=4866950&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23178747&merchantId=88819&subProductId=23178747&category=0&currSiteId=1&pmid=27248807&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9474436&merchantId=42869&subProductId=9474436&category=0&currSiteId=1&pmid=10703788&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33562602&merchantId=96865&subProductId=33562602&category=0&currSiteId=1&pmid=39192261&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29610550&merchantId=22196&subProductId=29610550&category=0&currSiteId=1&pmid=34775594&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28117404&merchantId=106728&subProductId=28117404&category=0&currSiteId=1&pmid=33063708&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34248&merchantId=1&subProductId=34248&category=0&currSiteId=1&pmid=102447&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=34248&merchantId=1&currSiteId=1&pmid=102447",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=102447&provinceId=1&productid=34248&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9476&merchantId=1&subProductId=9476&category=0&currSiteId=1&pmid=73265&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=9476&merchantId=1&currSiteId=1&pmid=73265",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=73265&provinceId=1&productid=9476&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=900221&merchantId=1&currSiteId=1&pmid=10009258",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=10009258&provinceId=1&productid=900221&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1828263&merchantId=1&subProductId=1828263&category=0&currSiteId=1&pmid=2015345&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1828263&merchantId=1&currSiteId=1&pmid=2015345",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2015345&provinceId=1&productid=1828263&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4038800&merchantId=1&subProductId=4038800&category=0&currSiteId=1&pmid=8969423&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4038800&merchantId=1&currSiteId=1&pmid=8969423",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8969423&provinceId=1&productid=4038800&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=23466110&merchantId=1&currSiteId=1&pmid=27578351",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=27578351&provinceId=1&productid=23466110&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23466110&merchantId=1&subProductId=23466110&category=0&currSiteId=1&pmid=27578351&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31357882&merchantId=110723&subProductId=31357882&category=0&currSiteId=1&pmid=36763566&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=37917560&provinceId=1&productid=32410272&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=32410272&merchantId=1&currSiteId=1&pmid=37917560",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32410272&merchantId=1&subProductId=32410272&category=0&currSiteId=1&pmid=37917560&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16254937&merchantId=60770&subProductId=16254937&category=0&currSiteId=1&pmid=18766051&showNum=20",

# end of category 3 in yhd.com

# Dec 17 2014



"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=30742441&merchantId=81455&subProductId=30742445&category=0&currSiteId=1&pmid=36064005&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=17522869&merchantId=71212&subProductId=32479963&category=0&currSiteId=1&pmid=37994005&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=29874337&merchantId=61644&subProductId=29874364&category=0&currSiteId=1&pmid=35068301&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=33672772&merchantId=81455&subProductId=33672779&category=0&currSiteId=1&pmid=39319914&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=25807990&merchantId=85333&subProductId=25807998&category=0&currSiteId=1&pmid=30294329&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=16052612&merchantId=54493&subProductId=16052619&category=0&currSiteId=1&pmid=18502643&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=30988667&merchantId=83521&subProductId=30988673&category=0&currSiteId=1&pmid=36347338&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=14853357&merchantId=21666&subProductId=31888410&category=0&currSiteId=1&pmid=37345035&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=13654457&merchantId=4905&subProductId=13654458&category=0&currSiteId=1&pmid=15397621&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=26936220&merchantId=1&subProductId=26936220&category=0&currSiteId=1&pmid=31643781&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=16851140&merchantId=1&subProductId=16851140&category=0&currSiteId=1&pmid=19551518&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=9932919&merchantId=1&subProductId=9932919&category=0&currSiteId=1&pmid=11192956&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=20633163&merchantId=12564&subProductId=20633163&category=0&currSiteId=1&pmid=24345160&showNum=20",

#"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=27243182&merchantId=81875&subProductId=27243184&category=0&currSiteId=1&pmid=32001636&showNum=20",

# "http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=7181365&merchantId=17591&subProductId=7181365&category=0&currSiteId=1&pmid=8286246&showNum=20",

# "http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4457705&merchantId=1&currSiteId=1&pmid=4550842",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=9796366&merchantId=1&subProductId=9796366&category=0&currSiteId=1&pmid=11046258&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11046258&provinceId=1&productid=9796366&merchantId=1",


"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16856911&merchantId=4905&subProductId=16856911&category=0&currSiteId=1&pmid=19558564&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4312962&merchantId=4905&subProductId=30409978&category=0&currSiteId=1&pmid=35689452&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=36961328&provinceId=1&productid=31534768",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11046258&provinceId=1&productid=9796366&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=35867135&provinceId=1&productid=30566706",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=36770026&provinceId=1&productid=31363985",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=28935350&provinceId=1&productid=24642989",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=35117981&provinceId=1&productid=29918820",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=30294327&provinceId=1&productid=25807996",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=28066583&provinceId=1&productid=23895233",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=31240946&provinceId=1&productid=26596518",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=18019719&provinceId=1&productid=15711825",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=38703774&provinceId=1&productid=33130696",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=24295589&provinceId=1&productid=20591481",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?pmid=18502699&provinceId=1&productid=16052674",
# Dec 3 9:49 until here.
"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=27154865&merchantId=1&currSiteId=1&pmid=31903448",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=10005&merchantId=1&subProductId=10005&category=0&currSiteId=1&pmid=73802&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=13037798&merchantId=1&currSiteId=1&pmid=14494521",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=17735532&merchantId=1&currSiteId=1&pmid=20899154",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2426482&provinceId=1&productid=2224414&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8248999&merchantId=1&currSiteId=1&pmid=9407783",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=10932598&provinceId=1&productid=9690066&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33406882&merchantId=20093&subProductId=33406886&category=0&currSiteId=1&pmid=39019334&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=26963712&merchantId=1&subProductId=26963712&category=0&currSiteId=1&pmid=31674809&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=106551&provinceId=1&productid=43452&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=43452&merchantId=1&currSiteId=1&pmid=106551",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=43452&merchantId=1&subProductId=43452&category=0&currSiteId=1&pmid=106551&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=9461470&provinceId=1&productid=8300854&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8300854&merchantId=1&currSiteId=1&pmid=9461470",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8300854&merchantId=1&subProductId=8300854&category=0&currSiteId=1&pmid=9461470&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=95242&provinceId=1&productid=21546&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=21546&merchantId=1&currSiteId=1&pmid=95242",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=24354925&merchantId=1&currSiteId=1&pmid=28599201",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=28599201&provinceId=1&productid=24354925&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24354925&merchantId=1&subProductId=24354925&category=0&currSiteId=1&pmid=28599201&showNum=20",

# 10:37 am here
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=20257585&provinceId=1&productid=17362085&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=17362085&merchantId=1&currSiteId=1&pmid=20257585",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17362085&merchantId=1&subProductId=17362085&category=0&currSiteId=1&pmid=20257585&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27154865&merchantId=1&subProductId=27154865&category=0&currSiteId=1&pmid=31903448&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31903448&provinceId=1&productid=27154865&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=27154865&merchantId=1&currSiteId=1&pmid=31903448",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8247096&merchantId=1&subProductId=8247096&category=0&currSiteId=1&pmid=9405857&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=8247096&merchantId=1&currSiteId=1&pmid=9405857",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=9405857&provinceId=1&productid=8247096&merchantId=1",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=99190&provinceId=1&productid=28731&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=28731&merchantId=1&currSiteId=1&pmid=99190",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28731&merchantId=1&subProductId=28731&category=0&currSiteId=1&pmid=99190&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9334324&merchantId=5044&subProductId=9334324&category=0&currSiteId=1&pmid=10553465&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16856911&merchantId=4905&subProductId=16856911&category=0&currSiteId=1&pmid=19558564&showNum=20",

# baby mother staff stops here. Dec 3th 10:45.

# children shoes

# children shoes
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=13880643&merchantId=7352&subProductId=13880680&category=0&currSiteId=1&pmid=15687233&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=28984489&merchantId=67227&subProductId=28984519&category=0&currSiteId=1&pmid=34079264&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=29439315&merchantId=90479&subProductId=29439331&category=0&currSiteId=1&pmid=34587708&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=31423920&merchantId=25833&subProductId=31423925&category=0&currSiteId=1&pmid=36837860&showNum=20",

# baby relevant
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=16619094&merchantId=72281&subProductId=19516474&category=0&currSiteId=1&pmid=23020584&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=16719683&merchantId=69343&subProductId=16719686&category=0&currSiteId=1&pmid=19382871&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=14647962&merchantId=5167&subProductId=14647968&category=0&currSiteId=1&pmid=16668709&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=20236141&merchantId=72281&subProductId=23186815&category=0&currSiteId=1&pmid=27257570&showNum=20",

# toy
"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=9004348&merchantId=1&subProductId=9004348&category=0&currSiteId=1&pmid=10196440&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=33919647&merchantId=1&subProductId=33919647&category=0&currSiteId=1&pmid=39601590&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=31565446&merchantId=125341&subProductId=31565449&category=0&currSiteId=1&pmid=36997875&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=4091638&merchantId=1&subProductId=4091638&category=0&currSiteId=1&pmid=4214484&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=16844484&merchantId=1&subProductId=16844484&category=0&currSiteId=1&pmid=19543044&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=27427842&merchantId=1&subProductId=27427842&category=0&currSiteId=1&pmid=32218817&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=984946&merchantId=1&subProductId=984946&category=0&currSiteId=1&pmid=1023610&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=9447894&merchantId=1&subProductId=9447894&category=0&currSiteId=1&pmid=10675938&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?productid=12199029&merchantId=1&subProductId=12199029&category=0&currSiteId=1&pmid=13621242&showNum=20",

#added
# cut 1 here

#mobile phone
"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=33939679&merchantId=1&subProductId=32480117&category=0&currSiteId=1&pmid=37994182&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=27387126&merchantId=1&subProductId=25920896&category=0&currSiteId=1&pmid=30429922&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=26889161&merchantId=65500&subProductId=26889172&category=0&currSiteId=1&pmid=31588909&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=28921398&merchantId=103247&subProductId=28977566&category=0&currSiteId=1&pmid=34070532&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=12529719&merchantId=51479&subProductId=22865964&category=0&currSiteId=1&pmid=26897343&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=1086120&merchantId=1&subProductId=1086120&category=0&currSiteId=1&pmid=1240625&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=27512642&merchantId=116034&subProductId=27512642&category=0&currSiteId=1&pmid=32320284&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=27489254&merchantId=107777&subProductId=27489258&category=0&currSiteId=1&pmid=32293600&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=1784950&merchantId=1&subProductId=1784950&category=0&currSiteId=1&pmid=1973222&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=18199041&merchantId=74448&subProductId=18199041&category=0&currSiteId=1&pmid=21517770&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=20206216&merchantId=1&subProductId=20206216&category=0&currSiteId=1&pmid=23845661&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=19132106&merchantId=1&subProductId=19132106&category=0&currSiteId=1&pmid=22563665&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=12946746&merchantId=41685&subProductId=12946746&category=0&currSiteId=1&pmid=14398483&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=25147967&merchantId=86009&subProductId=25147968&category=0&currSiteId=1&pmid=29517413&showNum=20",
#Dec3 10:54 add more mobile phones
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=26181835&merchantId=52956&subProductId=33773885&category=0&currSiteId=1&pmid=39432739&showNum=20",
#Dec 26


"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=22306752&merchantId=1&subProductId=15592046&category=0&currSiteId=1&pmid=17857413&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=22306752&merchantId=1&currSiteId=1&pmid=17857413",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=17857413&provinceId=1&productid=22306752&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31306755&merchantId=115520&subProductId=31546894&category=0&currSiteId=1&pmid=36977093&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13584622&merchantId=46721&subProductId=13584624&category=0&currSiteId=1&pmid=15310827&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34392110&merchantId=1&subProductId=28084005&category=0&currSiteId=1&pmid=33025600&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=34392110&merchantId=1&currSiteId=1&pmid=33025600",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=33025600&provinceId=1&productid=34392110&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34703815&merchantId=119575&subProductId=34703817&category=0&currSiteId=1&pmid=40495696&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16601242&merchantId=54455&subProductId=16601243&category=0&currSiteId=1&pmid=19230107&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23269743&merchantId=1&subProductId=5445285&category=0&currSiteId=1&pmid=6461194&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=23269743&merchantId=1&currSiteId=1&pmid=6461194",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=6461194&provinceId=1&productid=23269743&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33806883&merchantId=1&subProductId=26600400&category=0&currSiteId=1&pmid=31245383&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31245383&provinceId=1&productid=33806883&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=33806883&merchantId=1&currSiteId=1&pmid=31245383",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33939842&merchantId=1&subProductId=32981162&category=0&currSiteId=1&pmid=38535870&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=33939842&merchantId=1&currSiteId=1&pmid=38535870",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=38535870&provinceId=1&productid=33939842&merchantId=1",


# 11:03 mobile phone ends here. Dec 3
#computer, internet cards again
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=26698675&merchantId=110442&subProductId=26698675&category=0&currSiteId=1&pmid=31362958&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16566058&merchantId=56682&subProductId=16566058&category=0&currSiteId=1&pmid=19183085&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33339673&merchantId=126288&subProductId=33339673&category=0&currSiteId=1&pmid=38944301&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31204554&merchantId=126288&subProductId=31204554&category=0&currSiteId=1&pmid=36591142&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15917728&merchantId=56682&subProductId=15917728&category=0&currSiteId=1&pmid=18319506&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25190377&merchantId=1&subProductId=25190377&category=0&currSiteId=1&pmid=29565243&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=25190377&merchantId=1&currSiteId=1&pmid=29565243",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=29565243&provinceId=1&productid=25190377&merchantId=1",

#11:11 digital cameras
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28681756&merchantId=1&subProductId=28681756&category=0&currSiteId=1&pmid=33732734&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=28681756&merchantId=1&currSiteId=1&pmid=33732734",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=33732734&provinceId=1&productid=28681756&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28790521&merchantId=116034&subProductId=28790521&category=0&currSiteId=1&pmid=33857757&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32250337&merchantId=50086&subProductId=32250346&category=0&currSiteId=1&pmid=37738246&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17956067&merchantId=1&subProductId=17956067&category=0&currSiteId=1&pmid=21194383&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=17956067&merchantId=1&currSiteId=1&pmid=21194383",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=21194383&provinceId=1&productid=17956067&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31018295&merchantId=116034&subProductId=31018296&category=0&currSiteId=1&pmid=36382199&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23228446&merchantId=47826&subProductId=23228482&category=0&currSiteId=1&pmid=27303182&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27892698&merchantId=1&subProductId=26885801&category=0&currSiteId=1&pmid=31585090&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=27892698&merchantId=1&currSiteId=1&pmid=31585090",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31585090&provinceId=1&productid=27892698&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=19691731&merchantId=1&subProductId=19691731&category=0&currSiteId=1&pmid=23242132&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=19691731&merchantId=1&currSiteId=1&pmid=23242132",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=23242132&provinceId=1&productid=19691731&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30720758&merchantId=1&subProductId=30720758&category=0&currSiteId=1&pmid=36040450&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=30720758&merchantId=1&currSiteId=1&pmid=36040450",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=36040450&provinceId=1&productid=30720758&merchantId=1",

#video camera
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17201323&merchantId=50086&subProductId=17201323&category=0&currSiteId=1&pmid=20010583&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24875176&merchantId=86337&subProductId=24875185&category=0&currSiteId=1&pmid=29202996&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9802183&merchantId=19986&subProductId=9802184&category=0&currSiteId=1&pmid=11052220&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31105223&merchantId=106041&subProductId=31105225&category=0&currSiteId=1&pmid=36479490&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25307687&merchantId=19986&subProductId=25307699&category=0&currSiteId=1&pmid=29708047&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23937624&merchantId=21998&subProductId=23937631&category=0&currSiteId=1&pmid=28113220&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35218912&merchantId=71188&subProductId=35218913&category=0&currSiteId=1&pmid=41141249&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=19711480&merchantId=71188&subProductId=19711480&category=0&currSiteId=1&pmid=23264167&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17012346&merchantId=70424&subProductId=19857273&category=0&currSiteId=1&pmid=23436699&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4566864&merchantId=1&subProductId=4566864&category=0&currSiteId=1&pmid=4652913&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4566864&merchantId=1&currSiteId=1&pmid=4652913",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4652913&provinceId=1&productid=4566864&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4566867&merchantId=1&subProductId=4566867&category=0&currSiteId=1&pmid=4652916&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28635341&merchantId=1&subProductId=28635341&category=0&currSiteId=1&pmid=33678308&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=28635341&merchantId=1&currSiteId=1&pmid=33678308",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=33678308&provinceId=1&productid=28635341&merchantId=1",

#end of mp3
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25874324&merchantId=1&subProductId=25874324&category=0&currSiteId=1&pmid=30374098&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=25874324&merchantId=1&currSiteId=1&pmid=30374098",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=30374098&provinceId=1&productid=25874324&merchantId=1",
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32191080&merchantId=73453&subProductId=32191081&category=0&currSiteId=1&pmid=37671632&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25307996&merchantId=1&subProductId=25307996&category=0&currSiteId=1&pmid=29708415&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=25307996&merchantId=1&currSiteId=1&pmid=29708415",

#tablet
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28949481&merchantId=113297&subProductId=28949482&category=0&currSiteId=1&pmid=34038633&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23252564&merchantId=85082&subProductId=23252564&category=0&currSiteId=1&pmid=27331493&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27529750&merchantId=73027&subProductId=28600431&category=0&currSiteId=1&pmid=33638375&showNum=20",

#education relevant electronic devices
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24348933&merchantId=1&subProductId=24348933&category=0&currSiteId=1&pmid=28592396&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=24348933&merchantId=1&currSiteId=1&pmid=28592396",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=28592396&provinceId=1&productid=24348933&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29455957&merchantId=1&subProductId=29455957&category=0&currSiteId=1&pmid=34606232&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=29455957&merchantId=1&currSiteId=1&pmid=34606232",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=34606232&provinceId=1&productid=29455957&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30258195&merchantId=1&subProductId=30258195&category=0&currSiteId=1&pmid=35499821&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=30258195&merchantId=1&currSiteId=1&pmid=35499821",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=35499821&provinceId=1&productid=30258195&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35205749&merchantId=143829&subProductId=35205751&category=0&currSiteId=1&pmid=41125888&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13538739&merchantId=58399&subProductId=13538739&category=0&currSiteId=1&pmid=15252173&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17243245&merchantId=70424&subProductId=22440457&category=0&currSiteId=1&pmid=26407145&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=6582736&merchantId=13364&subProductId=6582737&category=0&currSiteId=1&pmid=7658193&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1006139&merchantId=1&subProductId=1006139&category=0&currSiteId=1&pmid=1067812&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1006139&merchantId=1&currSiteId=1&pmid=1067812",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1067812&provinceId=1&productid=1006139&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8813091&merchantId=21113&subProductId=8813091&category=0&currSiteId=1&pmid=9996495&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15714897&merchantId=50086&subProductId=15714898&category=0&currSiteId=1&pmid=18023391&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10501919&merchantId=21113&subProductId=10501919&category=0&currSiteId=1&pmid=11861426&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17026648&merchantId=72018&subProductId=17026649&category=0&currSiteId=1&pmid=19787422&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30051706&merchantId=1&subProductId=30051706&category=0&currSiteId=1&pmid=35267100&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=30051706&merchantId=1&currSiteId=1&pmid=35267100",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=35267100&provinceId=1&productid=30051706&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16659151&merchantId=73920&subProductId=16659151&category=0&currSiteId=1&pmid=19303840&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=21188879&merchantId=46622&subProductId=21188880&category=0&currSiteId=1&pmid=24985621&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1092729&merchantId=1&subProductId=1092729&category=0&currSiteId=1&pmid=1248392&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1092729&merchantId=1&currSiteId=1&pmid=1248392",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1248392&provinceId=1&productid=1092729&merchantId=1",

#edifier 11:51 Dec3 ends here.
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29055717&merchantId=125368&subProductId=29055719&category=0&currSiteId=1&pmid=34159980&showNum=20",




# internet card
"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=12776297&merchantId=56682&subProductId=12776297&category=0&currSiteId=1&pmid=14220755&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=21977343&merchantId=87190&subProductId=21977343&category=0&currSiteId=1&pmid=25876269&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=25190377&merchantId=1&subProductId=25190377&category=0&currSiteId=1&pmid=29565243&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=27213283&merchantId=110893&subProductId=27213283&category=0&currSiteId=1&pmid=31968145&showNum=20",

#household staff
#paper
"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=14513253&merchantId=1&subProductId=14513253&category=0&currSiteId=1&pmid=16505578&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=961362&merchantId=1&subProductId=961362&category=0&currSiteId=1&pmid=992922&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=5647771&merchantId=1&subProductId=5647771&category=0&currSiteId=1&pmid=6675513&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=1391928&merchantId=1&subProductId=1391928&category=0&currSiteId=1&pmid=1583618&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=1460484&merchantId=1&subProductId=1460484&category=0&currSiteId=1&pmid=1652810&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=34503239&merchantId=1&subProductId=34503239&category=0&currSiteId=1&pmid=40268024&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=23926556&merchantId=1&subProductId=23926556&category=0&currSiteId=1&pmid=28101034&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=35210331&merchantId=21608&subProductId=35210332&category=0&currSiteId=1&pmid=41131080&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=33553692&merchantId=1&subProductId=33553692&category=0&currSiteId=1&pmid=39182703&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=1897513&merchantId=1&subProductId=1897513&category=0&currSiteId=1&pmid=2090665&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?productid=42165&merchantId=1&subProductId=42165&category=0&currSiteId=1&pmid=105875&showNum=20",
# Dec 9th, put it at the end 11:16
# 'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690172&provinceId=1&productid=12264155&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690180&provinceId=1&productid=12264159&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4530721&provinceId=1&productid=4436119&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=17761826&provinceId=1&productid=15517578&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690178&provinceId=1&productid=12264158&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690180&provinceId=1&productid=12264159&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690174&provinceId=1&productid=12264156&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690190&provinceId=1&productid=12264164&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690178&provinceId=1&productid=12264158&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690180&provinceId=1&productid=12264159&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31813184&provinceId=1&productid=27080601&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690182&provinceId=1&productid=12264160&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690192&provinceId=1&productid=12264165&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31813173&provinceId=1&productid=27080593&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=17761826&provinceId=1&productid=15517578&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690178&provinceId=1&productid=12264158&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690180&provinceId=1&productid=12264159&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690174&provinceId=1&productid=12264156&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690178&provinceId=1&productid=12264158&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690161&provinceId=1&productid=12264150&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690159&provinceId=1&productid=12264149&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690180&provinceId=1&productid=12264159&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31813184&provinceId=1&productid=27080601&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690184&provinceId=1&productid=12264161&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690192&provinceId=1&productid=12264165&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690186&provinceId=1&productid=12264162&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',
'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=13690188&provinceId=1&productid=12264163&merchantId=1',

'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31813173&provinceId=1&productid=27080593&merchantId=1',

# More Dec 22, 2014 add previous
# Dec 19 2014 More URLS. Today`s target: get 75 URLS. Baby mother stuff.
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=17726530&merchantId=72276&subProductId=17726530&category=0&currSiteId=1&pmid=20885318&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34822314&merchantId=133455&subProductId=34822314&category=0&currSiteId=1&pmid=40630733&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34318846&merchantId=81875&subProductId=34318846&category=0&currSiteId=1&pmid=40052004&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29832976&merchantId=122858&subProductId=29832976&category=0&currSiteId=1&pmid=35023607&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10792207&merchantId=8101&subProductId=10792207&category=0&currSiteId=1&pmid=12163587&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23007282&merchantId=94361&subProductId=23007282&category=0&currSiteId=1&pmid=27054423&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34476870&merchantId=20638&subProductId=34476870&category=0&currSiteId=1&pmid=40239084&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=24259580&merchantId=89054&subProductId=24259583&category=0&currSiteId=1&pmid=28482254&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=13732178&merchantId=13337&subProductId=13732182&category=0&currSiteId=1&pmid=15492895&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=7365454&merchantId=1&currSiteId=1&pmid=8480986",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8480986&provinceId=1&productid=7365454&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7365454&merchantId=1&subProductId=7365454&category=0&currSiteId=1&pmid=8480986&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1586251&merchantId=1&subProductId=1586251&category=0&currSiteId=1&pmid=1775040&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1775040&provinceId=1&productid=1586251&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1586251&merchantId=1&currSiteId=1&pmid=1775040",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1896937&merchantId=1&currSiteId=1&pmid=2090101",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2090101&provinceId=1&productid=1896937&merchantId=1",
"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1896937&merchantId=1&subProductId=1896937&category=0&currSiteId=1&pmid=2090101&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34318846&merchantId=81875&subProductId=34318846&category=0&currSiteId=1&pmid=40052004&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=12345756&merchantId=52593&subProductId=12345756&category=0&currSiteId=1&pmid=13773892&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=9979294&merchantId=39247&subProductId=9979294&category=0&currSiteId=1&pmid=11242917&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1080097&merchantId=1&subProductId=1080097&category=0&currSiteId=1&pmid=1231906&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=1080097&merchantId=1&currSiteId=1&pmid=1231906",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=1231906&provinceId=1&productid=1080097&merchantId=1",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=2656415&merchantId=1&currSiteId=1&pmid=2831291",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2831291&provinceId=1&productid=2656415&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=2656415&merchantId=1&subProductId=2656415&category=0&currSiteId=1&pmid=2831291&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=18238946&merchantId=72276&subProductId=18238946&category=0&currSiteId=1&pmid=21571932&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25262585&merchantId=91700&subProductId=25262585&category=0&currSiteId=1&pmid=29652371&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35239987&merchantId=130684&subProductId=35239987&category=0&currSiteId=1&pmid=41167224&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35159043&merchantId=130684&subProductId=35159043&category=0&currSiteId=1&pmid=41068933&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35239984&merchantId=130684&subProductId=35239984&category=0&currSiteId=1&pmid=41167221&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35161199&merchantId=130684&subProductId=35161199&category=0&currSiteId=1&pmid=41072118&showNum=20",


"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35157515&merchantId=130684&subProductId=35157515&category=0&currSiteId=1&pmid=41066836&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15143210&merchantId=1&subProductId=15143210&category=0&currSiteId=1&pmid=17282010&showNum=20",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=17282010",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=15143210&merchantId=1&currSiteId=1&pmid=17282010",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35159043&merchantId=130684&subProductId=35159043&category=0&currSiteId=1&pmid=41068933&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35690147&merchantId=130684&subProductId=35690147&category=0&currSiteId=1&pmid=41705055&showNum=20",


"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35239985&merchantId=130684&subProductId=35239985&category=0&currSiteId=1&pmid=41167222&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30697099&merchantId=72782&subProductId=30697099&category=0&currSiteId=1&pmid=36014132&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=35503186&merchantId=1&currSiteId=1&pmid=41137987",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=41137987&provinceId=1&productid=35503186&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35503186&merchantId=1&subProductId=35216141&category=0&currSiteId=1&pmid=41137987&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34392110&merchantId=1&subProductId=35006683&category=0&currSiteId=1&pmid=40880624&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=34392110&merchantId=1&currSiteId=1&pmid=40880624",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=40880624&provinceId=1&productid=34392110&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32354768&merchantId=1&subProductId=32354768&category=0&currSiteId=1&pmid=37855138&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=32354768&merchantId=1&currSiteId=1&pmid=37855138",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=37855138&provinceId=1&productid=32354768&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35288590&merchantId=121791&subProductId=35288591&category=0&currSiteId=1&pmid=41226211&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=22382070&merchantId=27277&subProductId=22382071&category=0&currSiteId=1&pmid=26341825&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27222367&merchantId=94407&subProductId=27222368&category=0&currSiteId=1&pmid=31978565&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10787075&merchantId=48191&subProductId=10787076&category=0&currSiteId=1&pmid=12158257&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=20056213&merchantId=85990&subProductId=20056215&category=0&currSiteId=1&pmid=23670970&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=30052795&merchantId=89990&subProductId=30052798&category=0&currSiteId=1&pmid=35268548&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33619961&merchantId=43903&subProductId=33619977&category=0&currSiteId=1&pmid=39257458&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=25710350&merchantId=45839&subProductId=26058661&category=0&currSiteId=1&pmid=30597745&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=28254005&merchantId=102335&subProductId=28254006&category=0&currSiteId=1&pmid=33229918&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=15090493&merchantId=1&subProductId=15090493&category=0&currSiteId=1&pmid=17217259&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=15090493&merchantId=1&currSiteId=1&pmid=17217259",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=17217259&provinceId=1&productid=15090493&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=1814681&merchantId=2007&subProductId=2441142&category=0&currSiteId=1&pmid=2631989&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=32188269&merchantId=1&currSiteId=1&pmid=35884441",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=35884441&provinceId=1&productid=32188269&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32188269&merchantId=1&subProductId=30582222&category=0&currSiteId=1&pmid=35884441&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4703727&merchantId=1&currSiteId=1&pmid=4785075",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4785075&provinceId=1&productid=4703727&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4703727&merchantId=1&subProductId=4703727&category=0&currSiteId=1&pmid=4785075&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=27235933&merchantId=1&currSiteId=1&pmid=31993724",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=31993724&provinceId=1&productid=27235933&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=27235933&merchantId=1&subProductId=27235933&category=0&currSiteId=1&pmid=31993724&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35548080&merchantId=121646&subProductId=35548082&category=0&currSiteId=1&pmid=41542687&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=2151149&merchantId=1&currSiteId=1&pmid=2455445",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=2455445&provinceId=1&productid=2151149&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=2151149&merchantId=1&subProductId=2151149&category=0&currSiteId=1&pmid=2455445&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=5464140&merchantId=1&currSiteId=1&pmid=6481415",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=6481415&provinceId=1&productid=5464140&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=5464140&merchantId=1&subProductId=5464140&category=0&currSiteId=1&pmid=6481415&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=22110426&merchantId=6756&subProductId=22110426&category=0&currSiteId=1&pmid=26031041&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8754028&merchantId=21998&subProductId=10429805&category=0&currSiteId=1&pmid=11788777&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=16125228&merchantId=62235&subProductId=16125228&category=0&currSiteId=1&pmid=18593766&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=35220755&merchantId=71188&subProductId=35220758&category=0&currSiteId=1&pmid=41143197&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=8862615&merchantId=21998&subProductId=10429809&category=0&currSiteId=1&pmid=11788781&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=19798370&merchantId=81855&subProductId=27521617&category=0&currSiteId=1&pmid=32330060&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=18238154&merchantId=1&subProductId=18238154&category=0&currSiteId=1&pmid=21570711&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=18238154&merchantId=1&currSiteId=1&pmid=21570711",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=21570711&provinceId=1&productid=18238154&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=4566867&merchantId=1&subProductId=4566867&category=0&currSiteId=1&pmid=4652916&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=4566867&merchantId=1&currSiteId=1&pmid=4652916",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=4652916&provinceId=1&productid=4566867&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=32418347&merchantId=108232&subProductId=32418347&category=0&currSiteId=1&pmid=37926018&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=33971230&merchantId=1&subProductId=33971230&category=0&currSiteId=1&pmid=39656247&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=33971230&merchantId=1&currSiteId=1&pmid=39656247",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=39656247&provinceId=1&productid=33971230&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=23247201&merchantId=94957&subProductId=23247209&category=0&currSiteId=1&pmid=27325005&showNum=20",



"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=31012253&merchantId=78192&subProductId=31012254&category=0&currSiteId=1&pmid=36375580&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34952651&merchantId=59763&subProductId=34952656&category=0&currSiteId=1&pmid=40806335&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=34431489&merchantId=74448&subProductId=34431489&category=0&currSiteId=1&pmid=40181476&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=36223177&merchantId=41508&subProductId=36223179&category=0&currSiteId=1&pmid=42350232&showNum=20",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10128786&merchantId=1&subProductId=10128786&category=0&currSiteId=1&pmid=11400251&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10128786&merchantId=1&currSiteId=1&pmid=11400251",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11400251&provinceId=1&productid=10128786&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=7038425&merchantId=1&subProductId=7038425&category=0&currSiteId=1&pmid=8136621&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=7038425&merchantId=1&currSiteId=1&pmid=8136621",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=8136621&provinceId=1&productid=7038425&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=10128789&merchantId=1&subProductId=10128789&category=0&currSiteId=1&pmid=11400256&showNum=20",

"http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?provinceId=1&productid=10128789&merchantId=1&currSiteId=1&pmid=11400256",

"http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?currSiteId=1&pmid=11400256&provinceId=1&productid=10128789&merchantId=1",

"http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=29265598&merchantId=85725&subProductId=29265601&category=0&currSiteId=1&pmid=34392067&showNum=20",
#end of Dec 19 20:57pm

]

    def start_requests(self):
        for url in self.start_urls:
            req = urllib2.Request(url)
            result2 = json.loads(urllib2.urlopen(req, timeout=1000).read())
                   # log(self, "in start_requests", level=log.DEBUG)
            if int(result2.get('success')) == 1:
                print 'Crawl successfully for <%s>' % url
                back = result2.get('value')
                for product in back:
                    item = Yhd2Item()
                    item['productID'] = int(product.get('productId'))
                    item['pmId'] = int(product.get('pmId'))
                    newurl3 = 'http://pms.yhd.com/pms/getLeftRelatedProductByProductIdByJson.do?'\
                             + 'pmid=%d&provinceId=1&productid=%d' % (item['pmId'], item['productID'])
                    newurl2 = 'http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?'\
                             +'currSiteId=1&pmid=%d&provinceId=1&productid=%d' % (item['pmId'], item['productID'])
                    newurl4 = 'http://pms.yhd.com/pms/'\
                                +'getUpRelatedProductsByProductIdByJson.do?'\
                            +'productid=%d&pmid=%d&showNum=20' % (item['productID'],item['pmId'] )
                    if newurl3:
               #     log(self, "in newURL 3", level=log.DEBUG)
                        yield self.make_requests_from_url(url = newurl3)
                    elif newurl2:
             #       log(self, "in newURL2", level=log.DEBUG)
                        yield self.make_requests_from_url(url = newurl2)
                    elif newurl4:
            #        log(self, "in newURL 4", level=log.DEBUG)
                        yield self.make_requests_from_url(url = newurl4)
                    else:
                        print(urllib2.URLError)

    def make_requests_from_url(self, url):
        return Request(url,dont_filter=True)

    def parse(self, response):
        result = json.loads(response.body)
      #  urllist = list()
        items = list()
        urlcount = 0
        for product in result.get('value'):
            item = Yhd2Item()
            item['productID'] = int(product.get('productId'))
            item['pmId'] = int(product.get('pmId'))
            item['marketPrice'] = int(product.get('marketPrice'))
            item['linkurl'] = str(product.get('linkUrl'))
            item['categoryId'] = int(product.get('categoryId'))
            item['salePrice'] = int(product.get('salePrice'))
            item['yhdprice'] = int(product.get('yhdPrice'))
            item['isYihaodian'] = str(product.get('isYihaodian'))
            item['name'] = product.get('cnName').encode('utf-8')
            item['productType'] = str(product.get('productType'))
            item['currentDate'] = str(datetime.today().date() + timedelta(days = 1))
            items.append(item)
            newurl3 = ('http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?pmid=%d') % (item['pmId'])
            newurl2 = ('http://pms.yhd.com/pms/getLeftRecommProductsByJson.do?'+'currSiteId=1&pmid=%d&provinceId=1&productid=%d') % (item['pmId'], item['productID'])
            newurl4 = ('http://pms.yhd.com/pms/getUpRelatedProductsByProductIdByJson.do?productid=%d&pmid=%d&showNum=20') % (item['productID'],item['pmId'])
            if newurl3:
                url = newurl3
            if newurl2:
                url = newurl2
            if newurl4:
                url = newurl4
            yield item

         #   item['categoryName'] = product.get('categoryName').encode('utf-8')
         #   item['promEndDate'] = str(product.get('promEndDate'))
         #   item['promotionPoint'] =str(product.get('promotionPoint'))
         #   item['rate'] = str(product.get('rate'))
          #  item['recommend'] = str(product.get('recommend'))
        #    item['recommendType']= product.get('recommendType')
        #    item['rule'] = str(product.get('rule'))
          #  item['shoppingCount'] = int(product.get('shoppingCount'))
         #   item['promotionId'] = int(product.get('promotionId'))







