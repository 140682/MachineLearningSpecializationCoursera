import scrapy

# to run:
# scrapy crawl comments -o comments.json
class CommentsSpider(scrapy.Spider):
    name = "comments"
    
    start_urls = ['https://market.yandex.ru/catalog/54726/list?how=opinions&deliveryincluded=0&onstock=1']    
    
    def __init__(self):
        self.count = 0
        self.LIMIT = 15
    
    def parse(self, response):
        # follow links to phone pages
        for href in response.css('a.snippet-card__header-link::attr(href)').extract():
            link = href[:href.index('?')] + '/reviews'
            yield scrapy.Request(response.urljoin(link),
                                 callback=self.parse_phone)
        
        # follow link to the next review page
        next_page = response.css('a.n-pager__button-next::attr(href)').extract_first()
        if self.count < self.LIMIT and next_page is not None:
            next_page = response.urljoin(next_page)
            self.count += 1
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_phone(self, response):
        for review in response.css('div.product-review-item'):            
            
            yield {
                'text': ' '.join(review.css('.product-review-item__stat:nth-child(6) .product-review-item__text::text').extract()),       
                'rating': review.css('div.rating::text').extract_first(),              
            }
            
        # follow link to the next review page
        next_page = response.css('a.n-pager__button-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_phone)