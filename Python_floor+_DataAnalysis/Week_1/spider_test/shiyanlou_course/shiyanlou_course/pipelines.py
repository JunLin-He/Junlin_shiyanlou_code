# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class ShiyanlouCoursePipeline(object):
    # At spider working
    def process_item(self, item, spider):
        # Read item's data
        name = item['name']
        description = item['description']
        image = item['image']
        # Compose every data to a df_tmp
        df_tmp = pd.DataFrame([[name, description, image]], columns=['name', 'description', 'image'])
        self.df = self.df.append(df_tmp, ignore_index=True)
        return item

    # At the begin of the spider starting
    def open_spider(self, spider):
    	# New a empty df with column name
    	self.df = pd.DataFrame(columns=['name', 'description', 'image'])

    # At the end of the spider closing
    def close_spider(self, spider):
    	# Store the csv file as df
    	pd.DataFrame.to_csv(self.df, "courses.csv")