import os
import markdown
from pathlib import Path

def main(root_dir=Path('.')):
    # 确保使用UTF-8编码处理文件
    for md_file in root_dir.glob('*.md'):
        # 获取文件名（不带扩展名）
        folder_name = md_file.stem
        
        # 创建新文件夹（如果不存在）
        folder_path = root_dir / folder_name
        folder_path.mkdir(exist_ok=True)
        
        # 读取Markdown文件内容
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 将Markdown转换为HTML
        html_content = markdown.markdown(content)
        
        # 将HTML写入新文件夹的index.html
        html_path = folder_path / 'index.html'
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # （可选）移动原始Markdown文件到新文件夹
        # 如果需要保留原始文件则注释掉下一行
        os.rename(md_file, folder_path / md_file.name)

if __name__ == '__main__':
    # 使用示例：将程序放在目标文件夹根目录执行
    main()
    print("所有Markdown文件已处理完成！")