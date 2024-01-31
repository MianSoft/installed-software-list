# 读取软件名文件
with open('software_names.txt', 'r', encoding='utf-8') as file:
    software_names = [line.strip() for line in file.readlines()]

# 按软件名排序
sorted_software_names = sorted(software_names)

# 将排序后的结果写回文件
with open('sorted_software_names.txt', 'w', encoding='utf-8') as file:
    for software_name in sorted_software_names:
        file.write(software_name + '\n')

print("软件名已按名称排序并保存到 sorted_software_names.txt 文件中。")
