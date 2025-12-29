#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动清理 md 文件夹中未使用的图片（无需确认）
"""

import os
import re
from datetime import datetime

def extract_image_references(md_file):
    """从 Markdown 文件中提取所有图片引用"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'!\[.*?\]\((.*?)\)'
        matches = re.findall(pattern, content)
        
        image_names = []
        for match in matches:
            img_name = os.path.basename(match.strip())
            if img_name:
                image_names.append(img_name)
        
        return set(image_names)
    except Exception as e:
        return set()

def find_images_in_folder(folder):
    """查找文件夹中的所有图片文件"""
    images = []
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'}
    
    if not os.path.exists(folder):
        return []
    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                images.append(file)
    
    return images

def analyze_and_cleanup_chapter(chapter_path, chapter_name, dry_run=False):
    """分析并清理单个章节"""
    # 查找 Markdown 文件
    md_files = []
    for file in os.listdir(chapter_path):
        if file.endswith('.md'):
            md_files.append(os.path.join(chapter_path, file))
    
    if not md_files:
        return 0, 0, 0
    
    # 提取引用的图片
    referenced_images = set()
    for md_file in md_files:
        refs = extract_image_references(md_file)
        referenced_images.update(refs)
    
    # 查找实际存在的图片
    images_folder = os.path.join(chapter_path, 'images')
    if not os.path.exists(images_folder):
        return 0, 0, 0
    
    existing_images = find_images_in_folder(images_folder)
    
    # 找出未使用的图片
    unused_images = [img for img in existing_images if img not in referenced_images]
    
    # 删除未使用的图片
    deleted = 0
    if not dry_run and unused_images:
        for img in unused_images:
            try:
                img_path = os.path.join(images_folder, img)
                os.remove(img_path)
                deleted += 1
            except Exception as e:
                print(f"   ✗ 删除失败: {img}, 错误: {e}")
    
    return len(existing_images), len(referenced_images), len(unused_images)

def main():
    """主函数"""
    base_dir = 'md'
    
    print("🔍 开始清理未使用的图片...\n")
    print("⚠️  注意：此操作将自动删除未使用的图片，无法撤销！\n")
    
    # 统计
    total_chapters = 0
    total_existing = 0
    total_referenced = 0
    total_deleted = 0
    
    # 遍历所有类别
    for category in ['基础知识', '案例分析', '搜集资料']:
        category_path = os.path.join(base_dir, category)
        if not os.path.exists(category_path):
            continue
        
        print(f"\n{'='*60}")
        print(f"📁 {category}")
        print(f"{'='*60}\n")
        
        # 遍历章节
        for chapter in sorted(os.listdir(category_path)):
            chapter_path = os.path.join(category_path, chapter)
            if not os.path.isdir(chapter_path):
                continue
            
            total_chapters += 1
            
            # 分析并清理
            existing, referenced, unused = analyze_and_cleanup_chapter(
                chapter_path, chapter, dry_run=False
            )
            
            total_existing += existing
            total_referenced += referenced
            total_deleted += unused
            
            if unused > 0:
                print(f"🗑️  {chapter}")
                print(f"   删除: {unused} 个未使用图片 (保留: {referenced}/{existing})")
    
    # 总结
    print(f"\n{'='*60}")
    print(f"✅ 清理完成！")
    print(f"{'='*60}")
    print(f"总章节数: {total_chapters}")
    print(f"图片总数: {total_existing}")
    print(f"已使用: {total_referenced}")
    print(f"已删除: {total_deleted}")
    print(f"节省空间: ~{total_deleted * 50}KB (估算)")
    
    # 生成报告
    report_file = f'cleanup_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("图片清理报告\n")
        f.write("="*60 + "\n\n")
        f.write(f"清理时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"总章节数: {total_chapters}\n")
        f.write(f"图片总数: {total_existing}\n")
        f.write(f"已使用: {total_referenced}\n")
        f.write(f"已删除: {total_deleted}\n")
        f.write(f"使用率: {total_referenced/total_existing*100:.1f}%\n" if total_existing > 0 else "使用率: N/A\n")
    
    print(f"\n📄 报告已保存: {report_file}")

if __name__ == '__main__':
    main()
