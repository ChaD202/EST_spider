import scrapy
import csv
import os

n = 0


class scraper(scrapy.Spider):
    name = "est"

    start_urls = ["https://www.scottishepcregister.org.uk/"]

    custom_settings = {"FEEDS": {
                            "postcode_data1.csv": {"format": "csv",
                                                   "encoding": "utf-8-sig"}
                        },
                       "LOG_ENABLED": True,
                       "ROBOTSTXT_OBEY": False,
                       "DEFAULT_REQUEST_HEADERS": {
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                           'cookie': 'wrawrsatrsrweasrdxsfw2ewasjret=; wrawrsatrsrweasrdxsf=; captchaCookie=1; __ControllerTempData=AAEAAAD/////AQAAAAAAAAAEAQAAAOIBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuRGljdGlvbmFyeWAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAHVmVyc2lvbghDb21wYXJlcghIYXNoU2l6ZQ1LZXlWYWx1ZVBhaXJzAAMAAwgWU3lzdGVtLk9yZGluYWxDb21wYXJlcgjmAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXVtdBAAAAAkCAAAAAwAAAAkDAAAABAIAAAAWU3lzdGVtLk9yZGluYWxDb21wYXJlcgEAAAALX2lnbm9yZUNhc2UAAQEHAwAAAAABAAAAAwAAAAPkAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQT8////5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0CAAAAA2tleQV2YWx1ZQECBgUAAAALVmFsaWRTZWFyY2gIAQEB+v////z///8GBwAAAAVUYW5kQwgBAQH4/////P///wYJAAAADEVycm9yTWVzc2FnZQYKAAAANkluY29ycmVjdCB2ZXJpZmljYXRpb24gdGV4dCBlbnRlcmVkLiBQbGVhc2UgdHJ5IGFnYWluLgs=',
                           'dnt': '1',
                           'referer': 'https://www.scottishepcregister.org.uk/CustomerFacingPortal/EPCPostcodeSearchResults?pageNumber=2&pageRecordCount=10&sortBy=InspectionDate&sortDirection=Ascending&postcode=vpWROC8%2FDz7xx7mlcZrcca0oW39CXDsBke7ZJXRA%2BZ0%3D&propertytype=-1',
                           'sec-fetch-dest': 'document',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-site': 'same-origin',
                           'sec-fetch-user': '?1',
                           'upgrade-insecure-requests': '1',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                        }}

    def parse(self, response):
        with open('postcodes.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        for postcode in data:
            form_data = {'Postcode': postcode[0], 'CaptchaDeText': 'd30e27ccf2bd4d8b8bcca06033ba6a5b',
                         'CaptchaInputText': '9ywnq3'}

            yield scrapy.http.FormRequest('https://www.scottishepcregister.org.uk/CustomerFacingPortal/EPCPostcodeSearchResults', formdata=form_data, callback=self.parse_results)

    def parse_results(self, response):
        addresses = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[1]/text()').extract()]
        RRN = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[2]/text()').extract()]
        pdf_links = ["https://www.scottishepcregister.org.uk{u}".format(u=u) for u in response.xpath('//tr/td/a/@href').extract()]

        data = list(zip(addresses, RRN, pdf_links))

        for d in data:
            path = os.path.abspath("pdfs/{p}.pdf".format(p=d[1]))
            yield scrapy.Request(d[2], meta={'path': path}, callback=self.save_pdf)
            yield {'Address': d[0], 'RRN': d[1], 'PDF URL': d[2]}

        next_page = ["https://www.scottishepcregister.org.uk{u}".format(u=u) for u in response.xpath('//li[contains(., "Next")]/a/@href').extract()]

        if len(next_page) > 0:
            yield scrapy.Request(next_page[0], callback=self.parse_results)

        else:
            global n

            n += 1
            print(" >> SCRAPED {n} POSTCODES".format(n=n))

    def save_pdf(self, response):
        if len(response.body) > 0:
            print('Saving PDF {p}'.format(p=response.meta['path']))
            with open(response.meta['path'], 'wb') as f:
                f.write(response.body)

        else:
            print('Unable to save PDF {p}'.format(p=response.meta['path']))
