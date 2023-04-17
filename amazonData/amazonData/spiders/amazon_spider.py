import scrapy
from ..items import AmazondataItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    page_number  = 2
    start_urls = [
       "https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&qid=1681708995&rnid=9141481031&ref=sr_pg_2"
        ]

    def parse(self, response):
        items = AmazondataItem()
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items 

        next_page = "https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&page="+ str(AmazonSpiderSpider.page_number) +"&qid=1681703018&rnid=9141481031&ref=sr_pg_2"
        if AmazonSpiderSpider.page_number <= 75:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback = self.parse)
