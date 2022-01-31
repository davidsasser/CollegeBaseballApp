import pandas as pd
import os
# from simple_image_download import simple_image_download as simp

# response = simp.simple_image_download

# df = pd.read_csv('../teams_final.csv')

# df['search'] = df['school name'] + ' ' + df['nickname'] + ' logo png' 

# search_queries = df['search'].tolist()
# id_list = df['team_id'].tolist()



  
# def downloadimages(query):
#     # keywords is the search query
#     # format is the image file format
#     # limit is the number of images to be downloaded
#     # print urs is to print the image file url
#     # size is the image size which can
#     # be specified manually ("large, medium, icon")
#     # aspect ratio denotes the height width ratio
#     # of images to download. ("tall, square, wide, panoramic")
#     response().download(query, 5)
  
# Driver Code
# for query in search_queries:
#     downloadimages(query) 
#     print() 

for path, subdirs, files in os.walk('./simple_images'):
    for name in files:
        if('png_4' in name or 'png_5' in name):
            print(os.path.join(path, name))
            os.remove(os.path.join(path, name))