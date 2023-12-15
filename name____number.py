conda import re


# 从txt文件中读取文本
with open(r'C:\Users\Administrator\Desktop\doc.txt','r') as f:
    text = f.read()

# 将文本分割成单独的论文
papers = text.strip().split("\n\n")

# 创建字典来存储作者和对应的页码
authors_dict = {}

# 遍历每篇论文
for paper in papers:
    lines = paper.split("\n")
    if len(lines) < 2:
        continue

    # 提取页码和作者
    page_number = re.findall(r'\d+', lines[0])[-1]  # 假设最后一个数字是页码
    authors = lines[1].split(" ")

    # 将页码添加到字典中的每个作者下
    for author in authors:
        if author:  # 检查作者名字非空
            if author in authors_dict:
                authors_dict[author].add(page_number)
            else:
                authors_dict[author] = {page_number}

# 格式化输出
formatted_output = []
for author, pages in authors_dict.items():
    pages_string = ",".join(sorted(pages))
    formatted_output.append(f"{author}..................{pages_string}")

# 将所有格式化字符串连接起来
final_output = "\n".join(formatted_output)
with open(r'C:\Users\Administrator\Desktop\output.txt', 'w') as f:
    f.write(final_output)

