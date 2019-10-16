import re

Liste = [
    "https://www.simplilearn.com/ice9/free_resources_article_thumb/Data-Science-vs.-Big-Data-vs.jpg",
    "https://img.deusm.com/darkreading/1331840_Slideshow/Slide1CoverArt.jpg",
    "https://images.squarespace-cdn.com/content/v1/55fdfa38e4b07a55be8680a4/1560870741788-O52K0BL47DGFV7VNHA1U/ke17ZwdGBToddI8pDm48kFdj1LU3QXNrC7XCDJRXSjl7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1US_GH6w34F4AbXQYP1mTMh6WZrJMPe9RIQ00FIMO_YvQxJ-BQGo94klLBA8TVf45lA/image-asset.jpeg?format=2500w",
    "https://www.epfl.ch/education/master/wp-content/uploads/2018/11/IC_DS_MA_X-1536x864.jpg",
    "https://www.swinburne.edu.au/media/swinburneeduau/research-institutes/data-science/economics-innovation-analytics.jpg",
    "https://storage2.ischool.syr.edu/ischool.syr.edu/static/media/7757d1ed5a12d6a1ebac02edeca2e952/cache/1200_630_middle_applied-data-science-feature-image.jpg",
    "https://www.simplilearn.com/ice9/article_detailed_content_img/expert-talk-data-science-data-analytics-machine-learning.jpg",
    "https://dataanalyticspost.com/wp-content/uploads/2018/10/Dossier_innovation_data_poc.jpg",
    "http://www.apu.edu.my/sites/default/files/msc-in-data-science-and-business-analytics.jpg"
]


def num_there(s):
    return any(i.isdigit() for i in s)


def special_there(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(string) is None:
        return False
    else:
        return True
