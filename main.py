import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_university_rank(page_num):
    # 示例URL（需根据实际目标网站调整，此处以某排名网站为例）
    url = f"https://www.example.com/university-rank?page={page_num}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 提取数据（需根据目标网站的HTML结构调整标签和属性）
        rank_list = []
        rows = soup.find_all("tr", class_="rank-item")  # 假设每一行对应一所高校
        for row in rows:
            rank = row.find("td", class_="rank").text.strip()  # 排名
            name = row.find("td", class_="name").text.strip()  # 学校名称
            score = row.find("td", class_="score").text.strip()  # 总分
            rank_list.append({"排名": rank, "学校名称": name, "总分": score})
        
        return rank_list
    
    except Exception as e:
        print(f"第{page_num}页爬取失败：{e}")
        return []

# 爬取多页数据（假设共30页，每页20所高校，覆盖600所）
all_data = []
for page in range(1, 31):  # 页码范围需根据实际网站调整
    page_data = get_university_rank(page)
    all_data.extend(page_data)
    print(f"已爬取第{page}页，累计{len(all_data)}所高校")

# 保存数据到Excel
df = pd.DataFrame(all_data)
df.to_excel("中国大学排名.xlsx", index=False)
print("数据已保存至“中国大学排名.xlsx”")# 在这里编写代码
