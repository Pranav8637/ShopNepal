import scrapy

class ProductSpider(scrapy.Spider):
    name= 'darazproducts'

    starts_urls = [
        'https://www.sastodeal.com/sastodeal/cta-mobiles-28?flag='
    ]
    
    def parse(self, response):
        for product in  response.xpath("//div[@class='c2prKC']"):
            yield {
                'product_value': product.xpath(".//div[@class='c2prKC']/div").extract_first()
            }

            next_page= response.xpath("//li[@class=' ant-pagination-next']/a/@data-spm-anchor-id").extract_first()
            if next_page is not None:
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)