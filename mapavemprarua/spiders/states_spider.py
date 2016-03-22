import scrapy

class StatesSpider(scrapy.Spider):
    name = 'states'
    start_urls = ['http://mapa.vemprarua.net/']
    
    def parse(self, response):
        with open('emails.txt', 'w') as f:
            f.write('')
        for link in response.xpath('//li/ul/li/a/@href'):
            yield scrapy.Request(response.urljoin(link.extract()), callback=self.parse_state)
            
    def parse_state(self, response):
        title = response.xpath('//title/text()').extract()[0].replace(' ', '_').replace('/', '')
        for link in response.css("#lista-favor-indeciso-contra > .container > * > div > .panel-yellow > .panel-body > ul > li > a::attr('href')"):
            yield scrapy.Request(response.urljoin(link.extract()), callback=self.parse_parlamentar)
    
    def parse_parlamentar(self, response):
        title_un = response.xpath('//title/text()').extract()[0]
        name = title_un.split('-')[0]
        title = title_un.replace(' ', '_').replace('/', '')
        with open('emails.txt', 'ab') as f:
            for link in response.css("#dados-parlamentar > .panel-body > .form-horizontal > div > div > p > a::attr('href')"):
                normalized = link.extract()
                if 'mailto:' in normalized:
                    email = normalized.replace('mailto:', '')
                    f.write((name + '=' + email + '\n').encode('utf8'))
