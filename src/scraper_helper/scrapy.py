def run_spider(spider):
    import time
    start_time = time.time()
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(spider)
    process.start()
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))
