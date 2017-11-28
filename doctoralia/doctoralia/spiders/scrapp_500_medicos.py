# -*- coding: utf-8 -*-
import scrapy


class doctSpider(scrapy.Spider):
    name = 'doctoralia'
#    allowed_domains = ['http://www.doctoralia.com.br/medicos']
    start_urls = ['http://www.doctoralia.com.br/medicos']

    def parse(self, response):
        for doc in response.css("article.media"):
            doc_name = doc.css("h3 a::text").extract_first().strip("\r\n ")
            # doctor specialities
            doc_spec = doc.css("p.specialities::text").extract()
            doc_spec = [d for d in [d.strip("\r\n ") for d in doc_spec] if d!='']
            # doctor location
            doc_loca = doc.css("ul.locations li span.city::text").extract()
            doc_loca = [d for d in [d.strip("\r\n ") for d in doc_loca] if d!='']
            yield {"Nome do Medico": doc_name,
                   "Especialidade": doc_spec,
                   "Localizacao": doc_loca}

        # navigating to next pages
        href = response.css("li.PagedList-skipToNext a::attr(href)").extract_first()
        # this will make us get only the 500 first doctors
        if int(href.replace('medicos', '').replace('/', '')) <= 25:
            yield response.follow(href, callback=self.parse)
