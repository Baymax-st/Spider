import requests
url = 'https://www.amazon.com/JBL-TUNE-720BT-Lightweight-comfortable/dp/B0CTBCDD6D/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.95e3c82b-9ea6-43eb-b61b-74b03c38d434&dib=eyJ2IjoiMSJ9.p3rdOiiOUgFwnWfhpfGMLqab6V9Li2-xVE9XTfBX_qWO_vK06EWLSAlVMzfeVkNrjInW1CPaizNFT20QoYnZQvOpIVlXpTAIyXTG8Xio3H_Bxssq9gymhtXWI-iSXKjRuP4iI98VnzKCW89ANk-OAWOH9FB-WLVKE14SNClvshuRozH3q1cr9PPwB9SV18pmjQf2ByPNSQ6PjpRsuekqD2TvAurxQKkG1uWgK9oUsNg.cBXVqFXbwQjojaRRgtcSnmkuayRJmUHcn-l5Xtm8yW0&dib_tag=se&keywords=headphones&pd_rd_r=7f0e1ac3-9fb6-48cf-981b-0b2fab597938&pd_rd_w=zl1xj&pd_rd_wg=TM2ZZ&qid=1744644148&sr=8-1&th=1'
r = requests.get(url, timeout=30)
print(r.status_code)  # 打印状态码
r.encoding = r.apparent_encoding


def getHTMLTEXT(url):
    header = {'user':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = 'https://www.amazon.com/JBL-TUNE-720BT-Lightweight-comfortable/dp/B0CTBCDD6D/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.95e3c82b-9ea6-43eb-b61b-74b03c38d434&dib=eyJ2IjoiMSJ9.p3rdOiiOUgFwnWfhpfGMLqab6V9Li2-xVE9XTfBX_qWO_vK06EWLSAlVMzfeVkNrjInW1CPaizNFT20QoYnZQvOpIVlXpTAIyXTG8Xio3H_Bxssq9gymhtXWI-iSXKjRuP4iI98VnzKCW89ANk-OAWOH9FB-WLVKE14SNClvshuRozH3q1cr9PPwB9SV18pmjQf2ByPNSQ6PjpRsuekqD2TvAurxQKkG1uWgK9oUsNg.cBXVqFXbwQjojaRRgtcSnmkuayRJmUHcn-l5Xtm8yW0&dib_tag=se&keywords=headphones&pd_rd_r=7f0e1ac3-9fb6-48cf-981b-0b2fab597938&pd_rd_w=zl1xj&pd_rd_wg=TM2ZZ&qid=1744644148&sr=8-1&th=1' # 亚马逊商品页面
    html = getHTMLTEXT(url)  # 获取页面内容
    print(html[:10000])  # 打印页面内容