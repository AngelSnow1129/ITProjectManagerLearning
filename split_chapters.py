#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Markdown章节切分工具
将完整的Markdown教材按章节切分为独立文件
"""

import os
import re
from pathlib import Path


def split_markdown_by_chapters(source_file, output_dir=None):
    """
    按章节切分Markdown文件
    
    Args:
        source_file: 源文件路径
        output_dir: 输出目录，默认为源文件同级的split_chapters目录
    """
    source_path = Path(source_file)
    
    # 检查源文件是否存在
    if not source_path.exists():
        raise FileNotFoundError(f"源文件不存在: {source_file}")
    
    # 确定输出目录
    if output_dir is None:
        output_dir = source_path.parent / "split_chapters"
    else:
        output_dir = Path(output_dir)
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 读取源文件
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式查找所有章节标题
    chapter_pattern = re.compile(r'^## 第(\d+)章\s+(.+)$', re.MULTILINE)
    matches = list(chapter_pattern.finditer(content))
    
    file_count = 0
    
    # 保存前言部分（第1章之前的内容）
    if matches:
        preface_content = content[:matches[0].start()].strip()
        if preface_content:
            preface_file = output_dir / "00_前言_目录.md"
            with open(preface_file, 'w', encoding='utf-8') as f:
                f.write(preface_content)
            file_count += 1
            print(f"已保存: {preface_file.name}")
    
    # 切分各章节
    for i, match in enumerate(matches):
        chapter_num = match.group(1)
        chapter_title = match.group(2).strip()
        
        # 确定章节内容的起止位置
        start_pos = match.start()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        
        chapter_content = content[start_pos:end_pos].strip()
        
        # 清理文件名中的特殊字符
        safe_title = re.sub(r'[\\/:*?"<>|\r\n]', '', chapter_title)
        safe_title = safe_title.strip()
        
        # 生成文件名
        filename = f"{int(chapter_num):02d}_第{chapter_num}章 {safe_title}.md"
        output_file = output_dir / filename
        
        # 保存章节文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        file_count += 1
        print(f"已保存: {filename}")
    
    print(f"\n切分完成！")
    print(f"总共生成文件数: {file_count}")
    print(f"输出目录: {output_dir.absolute()}")
    
    return file_count, output_dir


if __name__ == "__main__":
    # 源文件路径
    source_file = r"md\基础知识\第00章-教材完整版\信息系统项目管理师教程-第四版.md"
    
    try:
        split_markdown_by_chapters(source_file)
    except Exception as e:
        print(f"错误: {e}")
