"""
@Author: Bluemangoo
@Date: 2022.11
@Copyright: 2022 Bluemangoo. All rights reserved.
@Description: 
"""
import datetime
import os
import re
import shutil

import requests
import json
import markdownify

k = 0


def parse_page(url):
    json_data = json.loads(download_page_data(url))
    data = {
        "name": json_data["bsData"]["superlanding"][0]["itemData"]["header"],
        "author": json_data["bsData"]["superlanding"][0]["itemData"]["infoBaiJiaHao"]["name"],
        "content": "",
        "content2": ""
    }
    time = json_data["bsData"]["superlanding"][0]["itemData"]["infoBaiJiaHao"]["date"]
    if len(time) < 8:
        time = str(datetime.datetime.today().year) + '-' + time
    else:
        time = "20" + time
    time += " " + json_data["bsData"]["superlanding"][0]["itemData"]["infoBaiJiaHao"]["time"] + ":00"
    data["time"] = time
    for paragraph in json_data["bsData"]["superlanding"][0]["itemData"]["sections"]:
        if paragraph["type"] == "text":
            data_html = paragraph["data_html"]
            data["content"] += data_html
        elif paragraph["type"] == "img":
            link = re.search(r'.*(?=@)', paragraph["link"]).group(0)
            data["content"] += "<img src=\"" + link + "\"></img><br><br>"
    return data


def download_page_data(url):
    raw_html = bytes.decode(requests.get(url).content)
    page_data = re.search(r'(?<=<script>window\.jsonData = ).*(?=;window\.firstScreenTime = Date\.now\(\);)',
                          raw_html).group(0)
    return page_data


def main(url):
    if not os.path.exists('Markdown'):
        os.makedirs('Markdown')
    if not os.path.exists('Docx'):
        os.makedirs('Docx')
    # if not os.path.exists('HTML'):
    #     os.makedirs('HTML')

    data = parse_page(url)

    markdown = markdownify.markdownify(data["content"], heading_style="ATX")
    markdown = "# " + data["name"] + "\n\n" + markdown
    markdown = f"---\ntitle: {data['name']}\nauthor: {data['author']}\ndate: {data['time']}\n---\n\n" + markdown
    with open('markdown/' + data["name"] + ".md", 'w', encoding='utf-8') as file:
        file.write(markdown)
    # with open("tmp.md", 'w', encoding='utf-8') as file:
    #     file.write(markdown)
    #
    # os.system(f"pandoc tmp.md -f markdown -t docx -s -o tmp.docx")
    # # os.system(f"pandoc tmp.md -f markdown -t html -s -o tmp.html")
    #
    # shutil.move("tmp.docx", 'docx/' + data["name"] + ".docx")
    # os.remove("tmp.md")


if __name__ == "__main__":
    while True:
        try:
            inp = input()
            main(inp)
            print("Done!")
        except AttributeError:
            print("Error! Please try again")
