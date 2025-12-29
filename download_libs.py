#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载所有必需的 JavaScript 库到本地
实现完全离线运行
"""

import os
import urllib.request
import ssl

# 创建 SSL 上下文（忽略证书验证）
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def download_file(url, output_path):
    """下载文件"""
    try:
        print(f"📥 下载: {url}")
        
        # 创建目录
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 下载文件
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            content = response.read()
        
        # 保存文件
        with open(output_path, 'wb') as f:
            f.write(content)
        
        file_size = len(content) / 1024  # KB
        print(f"   ✅ 成功: {output_path} ({file_size:.1f} KB)")
        return True
    except Exception as e:
        print(f"   ❌ 失败: {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始下载必需的 JavaScript 库...\n")
    
    # 定义要下载的库
    libraries = [
        {
            'name': 'Marked.js',
            'url': 'https://cdn.jsdelivr.net/npm/marked@9.1.6/marked.min.js',
            'output': 'web/libs/marked.min.js',
            'fallback_urls': [
                'https://unpkg.com/marked@9.1.6/marked.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js'
            ]
        },
        {
            'name': 'MathJax',
            'url': 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
            'output': 'web/libs/mathjax/tex-mml-chtml.js',
            'fallback_urls': [
                'https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js'
            ]
        },
        {
            'name': 'GitHub Markdown CSS',
            'url': 'https://cdn.jsdelivr.net/npm/github-markdown-css@5.2.0/github-markdown.min.css',
            'output': 'web/libs/github-markdown.min.css',
            'fallback_urls': [
                'https://unpkg.com/github-markdown-css@5.2.0/github-markdown.min.css'
            ]
        }
    ]
    
    # 下载每个库
    success_count = 0
    failed_count = 0
    
    for lib in libraries:
        print(f"\n{'='*60}")
        print(f"📦 {lib['name']}")
        print(f"{'='*60}")
        
        # 尝试主 URL
        if download_file(lib['url'], lib['output']):
            success_count += 1
            continue
        
        # 尝试备用 URL
        downloaded = False
        for fallback_url in lib.get('fallback_urls', []):
            print(f"   🔄 尝试备用 URL...")
            if download_file(fallback_url, lib['output']):
                success_count += 1
                downloaded = True
                break
        
        if not downloaded:
            failed_count += 1
            print(f"   ❌ 所有 URL 都失败了")
    
    # 总结
    print(f"\n{'='*60}")
    print(f"📊 下载完成")
    print(f"{'='*60}")
    print(f"成功: {success_count}/{len(libraries)}")
    print(f"失败: {failed_count}/{len(libraries)}")
    
    if success_count == len(libraries):
        print(f"\n✅ 所有库下载成功！")
        print(f"\n📝 下一步：运行 update_html_to_local.py 更新 HTML 文件")
    else:
        print(f"\n⚠️ 部分库下载失败，请检查网络连接")

if __name__ == '__main__':
    main()
