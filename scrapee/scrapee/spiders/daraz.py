import scrapy

class DarazSpider(scrapy.Spider):
    name= 'daraz'
    
    start_urls = [
        'https://www.sastodeal.com/sastodeal/cta-mobiles-28?flag='
    ]
    
    def parse(self, response):
        print ('hello', self, response)
        for product in response.xpath("//section[@class='categoryProduct category-product categorytDetailDiv  ']"):
            yield {
                'mobile-img': product.xpath(".//div[@class='thumbImg']").extract_first()
                # 'mobile': product.xpath(".//div[@class='thumbImg']").extract_first()
                # 'mobile-title': product.xpath(".//div/a/img/@src").extract_second()

                # 'mobile_title': product.xpath(".//div[@class='c16H9d']/title").extract_first()
                # #'mobile_info': product.xpath(".//div[@class='seller-name__detail']").extract_first()
                # 'mobile_price': product.xpath(".//div[@class='c3gUW0']/div").extract_first()
            }
            # yield {
            #     'mobile-detail': product.xpath(".//div/a/img/@src").second_first()

            # }

        next_page= response.xpath("//li[@class=' ant-pagination-next']/a/@data-spm-anchor-id").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page) 
            yield scrapy.Request(url=next_page_link, callback=self.parse)