"""
【项目01】  商铺数据加载及存储
作业要求：
1、成功读取“商铺数据.csv”文件
2、解析数据，存成列表字典格式：[{'var1':value1,'var2':value2,'var3':values,...},...,{}]
3、数据清洗：
① comment，price两个字段清洗成数字
② 清除字段缺失的数据
③ commentlist拆分成三个字段，并且清洗成数字
4、结果存为.pkl文件
"""
import json


def process1(data: dict):
    comment: str = data.get("comment").strip()
    price: str = data.get("price").strip()
    if comment:
        if " " in comment:
            data.update({"comment": comment.split(" ")[0]})
        else:
            data.update({"comment": "缺失数据"})
    else:
        data.update({"comment": "缺失数据"})
    if price:
        if "￥" in price:
            data.update({"price": price.split("￥")[-1]})
        else:
            data.update({"price": "缺失数据"})
    else:
        data.update({"price": "缺失数据"})
    return data


def process2(data: dict):
    commentlist: str = data.get("commentlist").strip()
    if commentlist:
        if "口味" in commentlist:
            lw = commentlist.split("口味")[-1].split("环境")[0].strip()
            hj = commentlist.split("环境")[-1].split("服务")[0].strip()
            fw = commentlist.split("服务")[-1]
            data.update({"commentlist": "{},{},{}".format(lw, hj, fw)})
        else:
            data.update({"commentlist": "缺失数据"})
    else:
        data.update({"commentlist": "缺失数据"})

    return data


if __name__ == '__main__':
    # 1.读取文件
    file_path = "D:\\Java development resource\\学习\\python数据处理\\02\\商铺数据.csv"
    datas = []
    with open(file_path, "r", encoding="UTF-8") as f:
        index = 0
        while True:
            buffer = f.readline()
            if buffer:
                if index != 0:
                    param = buffer.split(",")
                    datas.append({"classify": param[0], "name": param[1], "comment": param[2],
                                  "star": param[3], "price": param[4], "address": param[5],
                                  "commentlist": param[6].replace("\n", "")})
            else:
                break
            index += 1

        datas = list(map(process1, datas))
        datas = list(map(process2, datas))
        file = open("D:\\Java development resource\\学习\\python数据处理\\02\\商铺数据.json",
                    "w", encoding="utf8")
        json.dump(datas, file, ensure_ascii=False)
        file.close()
