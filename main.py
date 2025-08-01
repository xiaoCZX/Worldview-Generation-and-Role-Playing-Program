import os
from dotenv import load_dotenv
from src import world_generation, role_play, error_handler
import json
from src.error_handler import error_handler
from src import load_summary
import random


load_dotenv()

def get_daily_quote():
    with open("src/daily_quotes.json", "r", encoding="utf-8") as file:
        quotes = json.load(file).get("quotes", [])
    return random.choice(quotes) if quotes else "今日无名言，明日再试！"

def main_menu():
    os.system('cls')  # 清屏    
    daily_quote = get_daily_quote()
    while True:
        print("\n██╗    ██╗ ██████╗  █████╗ ██████╗ ██████╗")
        print("██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔══██╗")
        print("██║ █╗ ██║██║   ██║███████║██████╔╝██████╔╝")
        print("██║███╗██║██║   ██║██╔══██║██╔═══╝ ██╔═══╝")
        print("╚███╔███╔╝╚██████╔╝██║  ██║██║     ██║")
        print(" ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝")
        print("\n=== WGARP - 世界观生成与角色扮演程序 ===")
        print(f"每日一言：{daily_quote}")
        print("\n=== 主菜单 ===")
        print("1. 读取存档开始游戏")
        print("2. 开始新游戏")
        print("3. 退出")
        choice = input("请选择操作（输入数字）：")
        if choice == "1":
            # 读取存档并进入角色扮演
            world_desc, summary_text, save_name, last_conversation,role = load_summary.load_summary()
            if world_desc and summary_text:
                os.system('cls')  # 清屏
                print(f"\n已加载存档：{save_name}")
                if last_conversation:
                    role_play.start_role_play(world_desc, summary_text, save_name, last_conversation,role)
                return  # 结束主菜单
        elif choice == "2":
            background = input("请输入你想要的世界观背景（如：地理、历史、文化、魔法体系等，留空为默认）：")
            if not background.strip():
                background = "地理、历史、文化、魔法体系"
            os.system('cls')  # 清屏
            while True:
                print("\n正在生成世界观...")
                world_desc = world_generation.generate_world(background)
                print(f"\n世界观描述：\n{world_desc}\n")
                while True:
                    print("1. 重新生成")
                    print("2. 重新输入背景并生成")
                    print("3. 继续进入角色扮演")
                    sub_choice = input("请选择操作（输入数字）：")
                    if sub_choice == "1":
                        break  # 跳出当前循环，重新生成
                    elif sub_choice == "2":
                        background = input("请输入新的世界观背景：")
                        if not background.strip():
                            background = "地理、历史、文化、魔法体系"
                        break  # 跳出当前循环，重新生成
                    elif sub_choice == "3":
                        os.system('cls')  # 清屏
                        print("\n进入角色扮演模式...")
                        role_play.start_role_play(world_desc, None, None,None)
                        return  # 结束主菜单
                    else:
                        print("无效选择，请重新输入")
        elif choice == "3":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main_menu()
