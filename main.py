from crawler import crawler
import threading

print("Main------------------------------------------------------------------------------------------------------")

main_urls = []

infile = input("Enter absolute path for a infile directory. Example of acceptable path - (C:\\\\Users\\\\admin\\\\Desktop\\\\input.txt)\n")
f = open(infile, 'r')
for line in f:
    main_urls.append(line.replace("\n", ''))
f.close()
#main_urls.append("https://www.ebay.com/")
print(main_urls)

while(len(main_urls)):
    crawler.to_crawl = []
    crawler.crawled = []

    outfile = input("Please enter an absolute path of outfile directory. Example of acceptable path - (C:\\\\Users\\\\admin\\\\Desktop\\\\input.txt)\n")

    main_url = main_urls.pop(0)
    TOTAL_THREADS = 10

    c = crawler(main_url)
    c.crawl()

    while(crawler.to_crawl):
        threads = []
        to_crawl_length = len(crawler.to_crawl)
        if(to_crawl_length > 10):
            TOTAL_THREADS = 10
        else:
            TOTAL_THREADS = to_crawl_length
        
        print("Pages left to_crawl = ", end ='')
        print(to_crawl_length)   
        for _ in range(TOTAL_THREADS):
            t = threading.Thread(target = c.crawl)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()


    print("to crawl: ", end='')
    print(len(crawler.to_crawl))
    print("crawled: ", end='')
    print(len(crawler.crawled))

    f = open(outfile, 'w')
    for i in crawler.crawled:
        f.write(str(i) + '\n')
    
    print("Completed crawling for " + main_url)
    prompt = input("Do you want to crawl the next available link? (Y/N)\n")
    if(prompt == 'Y' or prompt == 'Yes' or prompt == 'y'):
        continue
    else:
        break