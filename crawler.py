from get_links import get_links

class crawler:
    to_crawl = []
    crawled = []
    def __init__(self, main_url) -> None:
        self.main_url = main_url
        crawler.to_crawl.append(main_url)
        self.get_link = get_links(main_url)

    def crawl(self):
        try:
            init_link = crawler.to_crawl.pop(0)
            crawler.crawled.append(init_link)
            print("Crawling link: ", end='')
            print(init_link)
            fresh_links = self.get_link.gather_links(init_link)
        
            for link in fresh_links:
                if link not in crawler.to_crawl and link not in crawler.crawled:
                    crawler.to_crawl.append(link)
        except:
            print("Error. Pls run the program again")