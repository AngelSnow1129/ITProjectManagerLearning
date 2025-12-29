#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新所有 HTML 文件，使用本地库而不是 CDN
"""

import os
import re

def update_html_file(file_path):
    """更新单个 HTML 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 替换 GitHub Markdown CSS
        content = re.sub(
            r'https://cdn\.jsdelivr\.net/npm/github-markdown-css@[\d.]+/github-markdown\.min\.css',
            'libs/github-markdown.min.css',
            content
        )
        
        # 替换 Marked.js CDN
        content = re.sub(
            r'https://cdn\.jsdelivr\.net/npm/marked@[\d.]+/marked\.min\.js',
            'libs/marked.min.js',
            content
        )
        
        # 替换 MathJax CDN
        content = re.sub(
            r'https://cdn\.jsdelivr\.net/npm/mathjax@3/es5/tex-mml-chtml\.js',
            'libs/mathjax/tex-mml-chtml.js',
            content
        )
        
        # 如果内容有变化，保存文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"   ❌ 错误: {e}")
        return False

def main():
    """主函数"""
    print("🔧 开始更新 HTML 文件，使用本地库...\n")
    
    # 要更新的 HTML 文件
    html_files = [
        'web/index.html',
        'web/study.html',
        'web/chapters.html',
        'web/viewer.html',
        'web/file-browser.html',
        'web/nav.html',
        'web/resources.html',
        'web/offline-viewer.html',
        'web/stats-demo.html'
    ]
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        if not os.path.exists(html_file):
            print(f"⏭️  跳过: {html_file} (文件不存在)")
            skipped_count += 1
            continue
        
        print(f"📝 处理: {html_file}")
        if update_html_file(html_file):
            print(f"   ✅ 已更新")
            updated_count += 1
        else:
            print(f"   ⏭️  无需更新")
            skipped_count += 1
    
    # 总结
    print(f"\n{'='*60}")
    print(f"✅ 更新完成")
    print(f"{'='*60}")
    print(f"已更新: {updated_count} 个文件")
    print(f"跳过: {skipped_count} 个文件")
    
    if updated_count > 0:
        print(f"\n🎉 所有 HTML 文件已更新为使用本地库！")
        print(f"📝 现在可以完全离线运行了")
    else:
        print(f"\n⚠️ 没有文件需要更新")

if __name__ == '__main__':
    main()
