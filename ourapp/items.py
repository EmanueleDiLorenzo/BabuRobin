# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeamItem(scrapy.Item):
    position = scrapy.Field()
    name = scrapy.Field()
    points = scrapy.Field()
    played = scrapy.Field()
    won = scrapy.Field()
    drawn = scrapy.Field()
    lost = scrapy.Field()
    goals_for = scrapy.Field()
    goals_against = scrapy.Field()
    goal_difference = scrapy.Field()
