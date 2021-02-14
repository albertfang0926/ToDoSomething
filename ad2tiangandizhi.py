# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:34:18 2021

@author: Albert
"""

"""
十天干发音：甲（jiǎ）、乙（yǐ）、丙（bǐng）、丁（dīng）、戊（wù）、己（jǐ）、庚（gēng）、
辛（xīn）、壬（rén）、癸（guǐ）；

十二地支对应十二生肖——子：鼠；丑：牛；寅：虎；卯：兔；辰：龙；巳：蛇； 午：马；未：羊；
申：猴；酉：鸡；戌：狗；亥：猪。
"""
import numpy as np
import json

tiangan_squence = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸',]
dizhi_squence   = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥', ]

def get_TianganDizhi_squence():
    tiangan_squence_60 = np.tile(tiangan_squence, 6)
    dizhi_squence_60   = np.tile(dizhi_squence, 5)
    tiangandizhi_squence = []
    for index, tiangan in enumerate(tiangan_squence_60):
        tiangandizhi_squence.append(tiangan + dizhi_squence_60[index])
    filename = r'F:/mycode/ToDoSomething\tiangandizhi_squence.json'
    with open(filename, 'w', encoding='utf-8') as f_obj: 
        json.dump(tiangandizhi_squence, f_obj)
    return

def ad2tiangandizhi(year, adbd='AD'):
    """
    parameters: 
        year : int
                公元纪年的数字
        adbd : string
                指定该数字为公元前（BC）还是公元后(AD)，默认值为AD
                
    returns:
        tiangandizhi : string
                返回的值为天干地支纪年
    """
    if adbd == 'AD':
        year -= 3
        tiangan_index = year % 10
        dizhi_index   = year % 12
    elif adbd == 'BC':
        year += 3
        tiangan_index = year % 10
        dizhi_index   = year % 12
    else:
        print("请指定公元前还是公元后：adbd='AD'或者 adbd='BC'")
        return
    # print(tiangan_index, dizhi_index)
    return tiangan_squence[tiangan_index-1] + dizhi_squence[dizhi_index-1]

if __name__ == '__main__':
    tiangan_dizhi = ad2tiangandizhi(2021)
    print(tiangan_dizhi)
    # get_TianganDizhi_squence()
    # filename = r'F:\mycode\ToDoSomething\tiangandizhi_squence.json'
    # with open(filename) as f_obj:
    #     tiangandizhi_squence = json.load(f_obj)
    # print(tiangandizhi_squence)
        