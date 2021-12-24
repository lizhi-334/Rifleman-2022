# -*- coding: utf-8 -*-
import sys
from Hephaestus.constant import CONFIG_DICT
from Hephaestus.process import main_proc
from Hephaestus.forge import forging
import sn_client as sn_client
sn_client=forging(sn_client)
import sndata as sndata
sndata=forging(sndata)




@main_proc("main")
def main(): # 主流程
    # CodeBlock
    a3=[0,0,66,0,0,0,0,98.78,0]
    b3=8179.97
    c3=8179.97
    d3=66
    e3=0
    # if
    if all([v==0 for v in a3]) and e3==0:
        # if
        if min(b3,c3)-d3<=0:
            # print
            print('额度不足')
            # 终止流程并回传流程结束描述
            _ = sn_client.order_finish(order_status='执行成功', desc='流程执行成功', func_desc='终止流程并回传流程结束描述|25a886af-135f-43b3-82ea-12c0874fb1a0')
        # elif
        elif min(b3,c3)-d3>0:
            # print
            print('不处理，截图留存，并发送OM、信用处理，结束流程')
    # elif
    elif any([v!=0 for v in a3]) or e3!=0:
        # if
        if min(b3,c3)-d3<0:
            # print
            print('逾期且额度不足')
            # 终止流程并回传流程结束描述
            _ = sn_client.order_finish(order_status='执行成功', desc='流程执行成功', func_desc='终止流程并回传流程结束描述|3a4e1277-c621-4dab-915d-dd9859396956')
        # elif
        elif min(b3,c3)-d3>=0:
            # print
            print('逾期')
        # CodeBlock
        import pandas
        #cus_num='42155'#ID有应收无信用
        #cus_num='10035'#ID有信用无应收
        #cus_num='114442'#有最迟无实际到期日
        cus_num='63861'#有实际有最迟
        #cus_num='10178'#有id无实际到期日无信用
        X=pandas._libs.tslibs.timestamps.Timestamp(0)
        B=pandas._libs.tslibs.timestamps.Timestamp(0)
        # 打开Excel数据表格
        df1 = sndata.read_excel(file_path=r'D:\SHTM\shtm_tt_v4.2.0.0\到期未结应收报表.xls', header=1, sheet_index=1, sheet_name=None, dtype={'客户编号':str}, kargs=None, func_desc='打开Excel数据表格，读取数据，保存为数据对象|17142c51-c2dd-4a5a-812b-d026c1475d29')
        # 筛选数据
        df1 = sndata.filter_excel(df=df1, field='客户编号', way="等于", keyword=cus_num, reverse='返回筛选得到的数据', func_desc='筛选数据|dcde17e6-06e9-48cf-bed2-8f7dd44d1072')
        # 打开Excel数据表格
        df2 = sndata.read_excel(file_path=r'D:\SHTM\shtm_tt_v4.2.0.0\临时信用额度.xls', header=1, sheet_index=1, sheet_name=None, dtype={'客户代码':str,'最迟到期日':str}, kargs=None, func_desc='打开Excel数据表格，读取数据，保存为数据对象|a119552c-fdc2-47b2-86f8-a6cde18811b4')
        # 筛选数据
        df2 = sndata.filter_excel(df=df2, field='客户代码', way="等于", keyword=cus_num, reverse='返回筛选得到的数据', func_desc='筛选数据|9ce69041-ffec-4254-b40f-789f30c16045')
        # if
        if df1['客户编号'].isnull().all():
            # print
            print('释放暂挂')
            # 终止流程并回传流程结束描述
            _ = sn_client.order_finish(order_status='执行成功', desc='流程执行成功', func_desc='终止流程并回传流程结束描述|2a26c359-67d2-4f83-930a-b25f0352af76')
        # if
        if df2['最迟到期日'].isnull().all():
            # print
            print('最迟到期日为空，未走临时')
            # 终止流程并回传流程结束描述
            _ = sn_client.order_finish(order_status='执行成功', desc='流程执行成功', func_desc='终止流程并回传流程结束描述|575f1cc4-f0ac-4d1d-b4a6-f187f71058dc')
        # CodeBlock
        A=max(df2['最迟到期日'])
        A=pandas._libs.tslibs.timestamps.Timestamp(A)
        # if
        if df1['实际到期日'].notnull().any():
            # CodeBlock
            B=max(df1['实际到期日'])
        # CodeBlock
        C=max(df1['到期日'])
        # if
        if B>=C:
            # CodeBlock
            X = B
        # elif
        elif B<C:
            # CodeBlock
            X = C
        # if
        if A<X:
            # CodeBlock
            print('A<X,未走临时')
        # elif
        elif A>=X:
            # CodeBlock
            print('A>=X,已走临时,进入4.6释放暂挂')
        # CodeBlock
        print('A:'+str(A))
        print('B:'+str(B))
        print('C:'+str(C))
        print('X:'+str(X))


if __name__ == '__main__':
    main()
