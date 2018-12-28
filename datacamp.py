from scrapy import Selector
html = '''
<html>
    <body>
        <div class="hello datacamp">
            <p>Hello World!</p>
        </div>
    </body>
</html>
'''

sel = Selector(text = html)
sel.xpath("//p")

sel.xpath("//p").extract()
sel.xpath("//p").extract_first()

# or

ps = sel.xpath("//p")
second_p = ps[1]
second_p.extract()