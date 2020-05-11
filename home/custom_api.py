import requests,os
from bs4 import BeautifulSoup
from tabulate import tabulate
from django.shortcuts import HttpResponse
def get_news(requsest):
    url = ("""http://newsapi.org/v2/top-headlines?q=corona&country=in&apiKey=8c07312c2c8a4767974edc5f9d7a99fd""")
    exportdata = """"""
    try:
        print('retrieve news..........')
        response = requests.get(url)
        data =  response.json()
        for newses in data['articles']:
            exportdata += """<li><a href="#">%s</a></li>"""%(newses['title'])
        print('news!')
    except:
        print('news API Error!')
        exportdata +="""<li><a href="#" class="text-danger">Error : could not retrieve the news from API! Check your internet Connection</a></li>""" 
    return HttpResponse(exportdata)
def get_status(requset):
    newsdata = """<div class="row justify-content-center">"""
    try:
        print('retrieve status..........')
        extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
        URL = 'https://www.mohfw.gov.in/'
        SHORT_HEADERS = ['SI No','	Name of State / UT','Cases','Cured','Death']
        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents(soup.tr.find_all('th'))
        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            if stat:
                if len(stat) == 5:
                    stat = list(stat)
                    stat.pop(0)
                    # last row
                    stats.append(stat)
                elif len(stat) == 6:
                    stats.append(stat)
        #print(stats[-1][1] )
        #stats[-1][1] = "Total Cases"
        #stats.remove(stats[-1])
        objects = []
        stats.sort(reverse=True,key = lambda x: int(x[1]))
        x=1
        x_list = []
        for stat in stats:
            stat.insert(0,x)
            objects.append(stat)
            x_list.append(x)
            x+=1
        table = tabulate(objects, headers=SHORT_HEADERS,tablefmt='html')
        print('status!')
        newsdata += """<div class="col-lg-8 col-md-8 col-sm-10" id="status">
        <h2 class="text-center">Covid 19 Current Stats</h2>
        %s
        <script>
        $(document).ready(function(){
            $("#status table").addClass("table text-center table-responsive-sm table-bordered table-striped");
             arr = %s;
             $.each(arr,function (i,val) {
                    elem = "#status table tr:nth-child("+val+") td:nth-child(2)";
                    var texttocheck = $(elem).text();
                    if (texttocheck.trim() == "Kerala") {
                         $(elem).parent().addClass("text-white bg-danger red");
                    }
                });
            });
        </script>
        <p style="font-size:8pt" class="text-right">source:Ministry of Health and Family Welfare (Government of India)</p></div>"""%(table,x_list)
    except:
        print('Status API Error!')
        newsdata +="""<p class="text-danger"> Error : Could not Load the Status</p>"""
    finally:
        newsdata +="""</div>"""
    return HttpResponse(newsdata)