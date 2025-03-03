import requests
import re

def remove_html_tags(text):
    while True:
        start_script = text.find("<script")
        end_script = text.find("</script>")
        if start_script == -1 or end_script == -1:
            break
        text = text[:start_script] + text[end_script + len("</script>"):]
    while True:
        start_style = text.find("<style")
        end_style = text.find("</style>")
        if start_style == -1 or end_style == -1:
            break
        text = text[:start_style] + text[end_style + len("</style>"):]
    text = re.sub(r'&#[0-9]+;', '', text)
    inside_tag = False
    result = ""

    for i in range(len(text)):
        if text[i] == "<":
            inside_tag = True
        elif text[i] == ">":
            inside_tag = False
        elif not inside_tag:
            result += text[i]
    result = result.split("\n")
    body = ""
    for line in result:
        if line.strip()=="":
            body += line.strip()
        else:
            body += "\n"+line.strip()      
            

    return body


def scrap(html_content):
    title_index = html_content.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html_content.find("</title>")
    title = html_content[start_index:end_index]

    body = remove_html_tags(html_content)

    links = []
    start_i = 0

    for i in range(html_content.count("href=\"")):
        start_i = html_content.find("href=\"", start_i)
        if start_i == -1:
            break
        start_i += len("href=\"")
        end_i = html_content.find("\"", start_i)
        link = html_content[start_i:end_i]
        prefix = "https://"
        if link[:len(prefix)] == prefix:
            links.append(link)
        start_i = end_i + 1

    return title, body, links

def main():
    url = input("Enter the URL: ")
    response = requests.get(url)
    html_content = response.text
    title, body, links = scrap(html_content)
    print("Title:", title)
    print("\nPage Body:", body)
    print("\nLinks found on the webpage:")
    for link in links:
        print(link)

main()