# -*- coding: utf-8 -*-
import scrapy

from ..items import TeamItem


class TeamSpider(scrapy.Spider):
    name = "team"
    allowed_domains = ["it.wikipedia.org"]
    start_urls = (
        'http://it.wikipedia.org/wiki/Serie_A_2013-2014',
    )

    def parse(self, response):
        """
        This method is used to parse the web page. Even if you can use a better code architecture,
         for example using an Item Pipeline (in this case: TeamPipeline) to perform more complex operations,
         in this case we use the simpler approach for learning purposes
        """
        items = []

        # Gets the table removing the first line (it's the table header)
        team_table = response.xpath("//*[@id='mw-content-text']/center/table//tr")[1:]
        for team in team_table:
            # creates an instance of our item
            item = TeamItem()

            # extract fields from the table it uses the following syntax:
            # from this xpath position (./), get the second column (td[2]/) and its content (text())
            # this operation extracts the content as a list of objects

            # because position extract a string such as "1.", we remove the ending '.' and convert everything as int()
            item["position"] = int(team.xpath("./td[2]/text()").extract()[0].replace(".", ""))

            # for other objects, we don't need anything particular
            item["name"] = team.xpath("./td[3]//a/text()").extract()[0]
            item["points"] = int(team.xpath("./td[4]//b/text()").extract()[0])
            item["played"] = int(team.xpath("./td[5]/text()").extract()[0])
            item["won"] = int(team.xpath("./td[6]/text()").extract()[0])
            item["drawn"] = int(team.xpath("./td[7]/text()").extract()[0])
            item["lost"] = int(team.xpath("./td[8]/text()").extract()[0])
            item["goals_for"] = int(team.xpath("./td[9]/text()").extract()[0])
            item["goals_against"] = int(team.xpath("./td[10]/text()").extract()[0])
            item["goal_difference"] = team.xpath("./td[11]/text()").extract()[0]

            items.append(item)

        return items
