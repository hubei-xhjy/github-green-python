import random
import subprocess
from datetime import datetime, timedelta
import os

def main():
    # 设置开始时间
    start_time = datetime(2019, 5, 16, 10, 19, 0)
    # 结束时间为当前时间
    end_time = datetime.now()

    # 获取用户输入的邮箱和 GitHub 登录 Token
    email = input("请输入您的邮箱地址: ")
    user = input("请输入您的用户名: ")
    repo_url = input("请输入您的仓库 URL: ")
    
    random.seed()

    # 设置 Git 用户信息
    config_email_cmd = ['git', 'config', '--global', 'user.email', email]
    config_user_cmd = ['git', 'config', '--global', 'user.name', user]
    subprocess.run(config_email_cmd, check=True)
    subprocess.run(config_user_cmd, check=True)

    # 克隆仓库
    subprocess.run(['git', 'config', '--global', '--unset', 'credential.helper'], check=True)
    subprocess.run(['git', 'clone', repo_url, 'repo-folder'], check=True)
    # 进入仓库目录
    os.chdir('repo-folder')

    # 当结束时间晚于开始时间时循环
    while end_time > start_time:
        num_commits = random.randint(0, 5)  # 生成 0 - 5 之间的随机数
        for i in range(num_commits):
            # 生成随机时分秒
            random_time = random.randint(0, 24 * 3600 - 1)  # 一天的秒数

            commit_date = (start_time + timedelta(seconds=random_time)).strftime('%c %z')
            # --allow-empty 允许空提交 --date 设置提交时间
            cmd = ['git', 'commit', '--allow-empty', '--date', commit_date, '-m', 'Green everyday!']
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(e)

        # 增加一天
        start_time += timedelta(days=1)

    # 推送到远程仓库
    subprocess.run(['git', 'push', 'origin', 'master'], check=True)
    print("Done!")

if __name__ == '__main__':
    main()