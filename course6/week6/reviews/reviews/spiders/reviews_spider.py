import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reviews"

    start_urls = ['https://market.yandex.ru/product/14206636/reviews']     

    def parse(self, response):
        for review in response.css('div.product-review-item'):            
            
            yield {
                'text': ' '.join(review.css('.product-review-item__stat:nth-child(6) .product-review-item__text::text').extract()),       
                'rating': review.css('div.rating::text').extract_first(),              
            }
            
        #next_page = response.css('li.next a::attr(href)').extract_first()
        next_page = response.css('a.n-pager__button-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)