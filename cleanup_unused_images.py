#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理 md 文件夹中未使用的图片
分析每个章节的 Markdown 文件，找出未被引用的图片并删除
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def find_markdown_files(base_dir):
    """查找所有 Markdown 文件"""
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def extract_image_references(md_file):
    """从 Markdown 文件中提取所有图片引用"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配 Markdown 图片语法: ![](path) 或 ![alt](path)
        pattern = r'!\[.*?\]\((.*?)\)'
        matches = re.findall(pattern, content)
        
        # 提取图片文件名（去除路径）
        image_names = []
        for match in matches:
            # 处理相对路径
            img_path = match.strip()
            # 获取文件名
            img_name = os.path.basename(img_path)
            if img_name:
                image_names.append(img_name)
        
        return set(image_names)
    except Exception as e:
        print(f"❌ 读取文件失败: {md_file}, 错误: {e}")
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

def analyze_chapter(chapter_path):
    """分析单个章节，返回未使用的图片列表"""
    # 查找该章节的所有 Markdown 文件
    md_files = []
    for file in os.listdir(chapter_path):
        if file.endswith('.md'):
            md_files.append(os.path.join(chapter_path, file))
    
    if not md_files:
        return [], [], []
    
    # 提取所有 Markdown 文件中引用的图片
    referenced_images = set()
    for md_file in md_files:
        refs = extract_image_references(md_file)
        referenced_images.update(refs)
    
    # 查找 images 文件夹中的所有图片
    images_folder = os.path.join(chapter_path, 'images')
    if not os.path.exists(images_folder):
        return [], [], list(referenced_images)
    
    existing_images = find_images_in_folder(images_folder)
    
    # 找出未使用的图片
    unused_images = []
    for img in existing_images:
        if img not in referenced_images:
            unused_images.append(img)
    
    return unused_images, existing_images, list(referenced_images)

def main():
    """主函数"""
    base_dir = 'md'
    
    if not os.path.exists(base_dir):
        print(f"❌ 目录不存在: {base_dir}")
        return
    
    print("🔍 开始分析 md 文件夹中的图片使用情况...\n")
    
    # 统计信息
    total_chapters = 0
    total_existing_images = 0
    total_referenced_images = 0
    total_unused_images = 0
    
    # 存储所有未使用的图片信息
    all_unused = []
    
    # 遍历所有子目录
    for category in ['基础知识', '案例分析', '搜集资料']:
        category_path = os.path.join(base_dir, category)
        if not os.path.exists(category_path):
            continue
        
        print(f"\n{'='*60}")
        print(f"📁 分析类别: {category}")
        print(f"{'='*60}\n")
        
        # 遍历该类别下的所有章节
        for chapter in sorted(os.listdir(category_path)):
            chapter_path = os.path.join(category_path, chapter)
            if not os.path.isdir(chapter_path):
                continue
            
            total_chapters += 1
            
            # 分析章节
            unused, existing, referenced = analyze_chapter(chapter_path)
            
            total_existing_images += len(existing)
            total_referenced_images += len(referenced)
            total_unused_images += len(unused)
            
            # 显示结果
            status = "✅" if len(unused) == 0 else "⚠️"
            print(f"{status} {chapter}")
            print(f"   📊 图片总数: {len(existing)}")
            print(f"   ✓ 已使用: {len(referenced)}")
            print(f"   ✗ 未使用: {len(unused)}")
            
            if unused:
                print(f"   📝 未使用的图片:")
                for img in sorted(unused)[:5]:  # 只显示前5个
                    print(f"      - {img}")
                if len(unused) > 5:
                    print(f"      ... 还有 {len(unused) - 5} 个")
                
                # 记录未使用的图片
                for img in unused:
                    img_path = os.path.join(chapter_path, 'images', img)
                    all_unused.append({
                        'category': category,
                        'chapter': chapter,
                        'image': img,
                        'path': img_path
                    })
            print()
    
    # 显示总结
    print(f"\n{'='*60}")
    print(f"📊 统计总结")
    print(f"{'='*60}")
    print(f"总章节数: {total_chapters}")
    print(f"图片总数: {total_existing_images}")
    print(f"已使用图片: {total_referenced_images}")
    print(f"未使用图片: {total_unused_images}")
    print(f"使用率: {total_referenced_images/total_existing_images*100:.1f}%" if total_existing_images > 0 else "使用率: N/A")
    
    # 询问是否删除
    if all_unused:
        print(f"\n⚠️  发现 {len(all_unused)} 个未使用的图片")
        print(f"\n是否删除这些未使用的图片？")
        print(f"输入 'yes' 确认删除，输入其他任何内容取消")
        
        response = input("\n请输入: ").strip().lower()
        
        if response == 'yes':
            print(f"\n🗑️  开始删除未使用的图片...\n")
            deleted_count = 0
            failed_count = 0
            
            for item in all_unused:
                try:
                    os.remove(item['path'])
                    print(f"✓ 已删除: {item['category']}/{item['chapter']}/{item['image']}")
                    deleted_count += 1
                except Exception as e:
                    print(f"✗ 删除失败: {item['path']}, 错误: {e}")
                    failed_count += 1
            
            print(f"\n✅ 删除完成!")
            print(f"   成功删除: {deleted_count} 个")
            if failed_count > 0:
                print(f"   删除失败: {failed_count} 个")
        else:
            print(f"\n❌ 已取消删除操作")
    else:
        print(f"\n✅ 太好了！所有图片都在使用中，无需清理。")
    
    # 生成报告文件
    report_file = 'unused_images_report.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("未使用图片分析报告\n")
        f.write("="*60 + "\n\n")
        f.write(f"分析时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"总章节数: {total_chapters}\n")
        f.write(f"图片总数: {total_existing_images}\n")
        f.write(f"已使用图片: {total_referenced_images}\n")
        f.write(f"未使用图片: {total_unused_images}\n\n")
        
        if all_unused:
            f.write("未使用的图片列表:\n")
            f.write("-"*60 + "\n")
            for item in all_unused:
                f.write(f"{item['category']}/{item['chapter']}/{item['image']}\n")
        else:
            f.write("所有图片都在使用中！\n")
    
    print(f"\n📄 详细报告已保存到: {report_file}")

if __name__ == '__main__':
    main()
