

import requests
from requests.auth import HTTPBasicAuth
import logging
import sys
# Create and configure logger
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
 
# Creating an object
# logger = logging.getLogger()
 
# # Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# response=requests.get("https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/110.mp3")
# down_link="https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/110.mp3"
# content = response.content
#
# with open("C:\\Users\\mhdri\\Documents\\test.mp3", 'wb') as fp:
#     file_path="C:\\Users\\mhdri\\Documents\\test.mp3"
#     for name in range(110,115):
#         temp=
#         file_path=file_path.replace("test",
#         print(file_path)
class QuranDownloader:
    @staticmethod
    def download_quran():

        for name in range(1,115):
            logging.info(f'Downloding surah {name}')
            temp=str(name)
            rev='000'
            if len(temp)==1:
                new=rev[0:2]+temp
            elif len(temp)==2:
                new=rev[0:1]+temp
            else:
                new=temp

            response=requests.get(f'https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/{new}.mp3')
            content=response.content
            with open(f'/home/rilwan/Downloads/quran/{new}.mp3', 'wb') as fp:
                fp.write(content)


if __name__=="__main__":
    QuranDownloader.download_quran()