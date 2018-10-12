
import urllib.request
import urllib.error
import urllib.parse
import socket
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
# POST请求的信息，填写你的用户名和密码
value = {'source': 'index_nav',
    'form_password': 'Bowen!0718',
    'form_email': 'hitbwzhang@gmail.com'
    }

'''代理ip'''
# 防爬机制的克服：代理IP
#为什么要使用代理IP？因为各种反爬机制会检测同一IP爬取网页的频率速度，如果速度过快，
# 就会被认定为机器人封掉你的IP。但是速度过慢又会影响爬取的速度，
# 因此，我们将使用代理IP取代我们自己的IP，这
# 样不断更换新的IP地址就可以达到快速爬取网页而降低被检测为机器人的目的了。
#同样利用urllib的request就可以完成代理IP的使用，但是与之前用到的urlopen不同，我们需要自己创建订制化的opener。什么意思呢？
#urlopen就好像是opener的通用版本，当我们需要特殊功能（例如代理IP）的时候，
# urlopen满足不了我们的需求，我们就不得不自己定义并创建特殊的opener了。
proxy = {'http': '106.75.164.15:3128'} # 代理ip# 代理IP信息为字典格式，key为'http'，value为'代理ip：端口号'
# 查询代理ip的网址
# http://www.xicidaili.com/
#http://www.66ip.cn/
#http://www.mimiip.com/gngao/
#http://www.kuaidaili.com/

'''超时'''
#设置超时的目的是为了防止爬取网站的时候，等待时间过长而导致效率的降低。有效的超时设置可以强制结束等待而进行下一次的爬取，下面来一段代码看如何使用。
# 设置超时为2秒，单位为秒
timeout = 2
try:
    #设置socket超时时间，如果不设置，则会使用默认时间。
    socket.setdefaulttimeout(timeout)
    
    #下面这句的意思是利用了urllib库的parse来对post内容解析，为什么要解析呢？
    #这是因为post内容需要进行一定的编码格式处理后才能发送，而编码的规则需要遵从RFC标准
    #而parse的urlencode方法是将一个字典或者有顺序的二元素元组转换成为URL的查询字符串
    #（说白了就是按照RFC标准转换了一下格式）。然后再将转换好的字符串按UTF-8的编码转换成为二进制格式才能使用。 
    data = urllib.parse.urlencode(value).encode('utf8')
    
    response = urllib.request.Request('https://www.douban.com/login', data=data, headers=headers)
    # 使用ProxyHandler方法生成处理器对象
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建代理IP的opener实例，参数为proxy处理器对象
    opener = urllib.request.build_opener(proxy_handler)
    # 将设置好的post信息和headers的response作为参数，# 用代理IP的opener打开指定状态的URL信息
    html = opener.open(response)
    result = html.read().decode('utf8')
    print(result)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误编码是' + str(e.code))
except socket.timeout:
    print('socket超时')
else:
    print('请求成功通过。')