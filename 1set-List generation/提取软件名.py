from bs4 import BeautifulSoup

# 本地HTML文件的路径
html_file_path = 'pathtoyourfile.html'

with open(html_file_path, 'r', encoding='utf-8') as file
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有软件名所在的td元素
software_cells = soup.find_all('td', class_='normalborder', colspan='2')

# 提取软件名
software_names = [cell.get_text(strip=True) for cell in software_cells]

# 输出软件名到txt文件
with open('software_names.txt', 'w', encoding='utf-8') as file
    for software_name in software_names
        file.write(software_name + 'n')

print(软件名已提取并保存到 software_names.txt 文件中。)
