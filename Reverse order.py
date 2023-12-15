def reverse_strings(strings):
    return [s[::-1] for s in strings]



strings = input("请输入字符串：")
print(f"你输入的字符串是：{strings}")
reversed_string = strings[::-1]
print(reversed_string)

import itchat

# # 登录微信
# itchat.auto_login()

# # 获取特定联系人
# contact = itchat.search_friends(name='崔牡丹')[0]

# # 定义处理消息的函数
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     # 检查消息是否来自于特定联系人
#     if msg['FromUserName'] == contact['UserName']:
#         # 检查消息是否是文本消息，并且不包含表情
#         if msg['Type'] == 'Text' and not msg['Text'].startswith('[') and not msg['Text'].endswith(']'):
#             # 反转消息
#             reversed_msg = msg['Text'][::-1]
#             # 发送反转后的消息
#             return reversed_msg

# # 开始监听消息
# itchat.run()