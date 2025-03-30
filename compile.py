import os
import shutil

def organize_markdown_files(root_dir):
    # 确保根目录存在
    if not os.path.exists(root_dir):
        print(f"错误：目录 {root_dir} 不存在")
        return

    # 遍历根目录下的所有文件
    for filename in os.listdir(root_dir):
        # 检查是否为.md文件
        if filename.endswith('.md'):
            # 获取文件名（不带扩展名）
            base_name = os.path.splitext(filename)[0]
            
            # 创建新目录路径
            new_dir = os.path.join(root_dir, base_name)
            
            # 创建目录（如果不存在）
            os.makedirs(new_dir, exist_ok=True)
            
            # 构建源文件和目标文件路径
            src_path = os.path.join(root_dir, filename)
            dest_path = os.path.join(new_dir, 'index.md')
            
            # 复制文件（保留元数据）
            shutil.copy2(src_path, dest_path)
            print(f"已处理：{filename} -> {new_dir}/index.md")

if __name__ == "__main__":
    # 设置要处理的根目录
    target_directory = "./"
    
    # 执行文件整理
    organize_markdown_files(target_directory)
    print("所有Markdown文件已整理完成！")
