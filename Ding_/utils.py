def daoguanwang():
    import time
    for i in range(100000):
        print('变态王向你发起了视频邀请：')
        a = input('请输入1接受邀请，输入2拒绝邀请：')
        if a == '1':
            for i in range(10):
                if i % 1 == 0:
                    print(f'变态王开始导管了！！他导了{i+1}下！！!')
                time.sleep(1)
            print('变态王🐍了！')
            break
        elif a =='2':
            for i in range(10000):
                print('变态王大笑一声并再次向你发起了视频邀请：')
                a = input('请输入1接受邀请，输入2拒绝邀请：')
                if a == '1' and i % 1000 == 0:
                    print(f'变态王开始导管了！他导了{i + 1}下！！！')
                else:
                    print('请正确输入！')
        else:
            print('请正确输入！')




