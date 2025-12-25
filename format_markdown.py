#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Markdown格式化工具
按照规范修复Markdown文件格式
"""

import os
import re
from pathlib import Path


def format_markdown_file(file_path):
    """
    格式化单个Markdown文件
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. 修复OCR导致的编号断裂 (如 "1 . 1" -> "1.1")
    content = re.sub(r'(\d+)\s*\.\s*(\d+)\s*\.\s*(\d+)', r'\1.\2.\3', content)
    content = re.sub(r'(\d+)\s*\.\s*(\d+)', r'\1.\2', content)
    
    # 2. 修复术语中的空格 (如 "P M P" -> "PMP", "I T" -> "IT")
    # 常见术语列表
    terms = [
        ('P M P', 'PMP'), ('P M I', 'PMI'), ('P M B O K', 'PMBOK'),
        ('I T', 'IT'), ('O T', 'OT'), ('I o T', 'IoT'), ('I o V', 'IoV'),
        ('A I', 'AI'), ('5 G', '5G'), ('6 G', '6G'), ('4 G', '4G'),
        ('I P v 6', 'IPv6'), ('I P v 4', 'IPv4'),
        ('E R P', 'ERP'), ('M E S', 'MES'), ('P L C', 'PLC'),
        ('I a a S', 'IaaS'), ('P a a S', 'PaaS'), ('S a a S', 'SaaS'),
        ('T S N', 'TSN'), ('A p p', 'App'),
    ]
    for old, new in terms:
        content = content.replace(old, new)
    
    # 3. 标题层级重构
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # 检测 X.X.X 格式的标题 (四级标题)
        match_4 = re.match(r'^(\d+\.\d+\.\d+)\s+(.+)$', stripped)
        if match_4 and not stripped.startswith('#'):
            new_lines.append(f'#### {stripped}')
            continue
        
        # 检测 X.X 格式的标题 (三级标题)
        match_3 = re.match(r'^(\d+\.\d+)\s+(.+)$', stripped)
        if match_3 and not stripped.startswith('#'):
            new_lines.append(f'### {stripped}')
            continue
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 4. 列表符号统一 (● * 等 -> -)
    content = re.sub(r'^(\s*)●\s*', r'\1- ', content, flags=re.MULTILINE)
    content = re.sub(r'^(\s*)\*\s+(?!\*)', r'\1- ', content, flags=re.MULTILINE)
    content = re.sub(r'^(\s*)•\s*', r'\1- ', content, flags=re.MULTILINE)
    content = re.sub(r'^(\s*)◆\s*', r'\1- ', content, flags=re.MULTILINE)
    content = re.sub(r'^(\s*)○\s*', r'\1- ', content, flags=re.MULTILINE)
    
    # 5. 标点符号规范化 (中文语境下英文标点转中文)
    # 但要排除代码块、数字小数点、英文术语
    def replace_punctuation(text):
        # 分割代码块
        parts = re.split(r'(```[\s\S]*?```|`[^`]+`)', text)
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 1:  # 代码块，保持不变
                result.append(part)
            else:
                # 替换标点，但保护数字中的点和英文缩写
                # 逗号: 中文字符后的英文逗号
                part = re.sub(r'([\u4e00-\u9fff]),', r'\1，', part)
                part = re.sub(r',([\u4e00-\u9fff])', r'，\1', part)
                # 句号: 中文字符后的英文句号（排除数字）
                part = re.sub(r'([\u4e00-\u9fff])\.(?!\d)', r'\1。', part)
                # 问号
                part = re.sub(r'([\u4e00-\u9fff])\?', r'\1？', part)
                part = re.sub(r'\?([\u4e00-\u9fff])', r'？\1', part)
                # 感叹号
                part = re.sub(r'([\u4e00-\u9fff])!', r'\1！', part)
                part = re.sub(r'!([\u4e00-\u9fff])', r'！\1', part)
                # 冒号
                part = re.sub(r'([\u4e00-\u9fff]):', r'\1：', part)
                part = re.sub(r':([\u4e00-\u9fff])', r'：\1', part)
                # 分号
                part = re.sub(r'([\u4e00-\u9fff]);', r'\1；', part)
                part = re.sub(r';([\u4e00-\u9fff])', r'；\1', part)
                result.append(part)
        return ''.join(result)
    
    content = replace_punctuation(content)
    
    # 6. 移除列表项之间的空行
    content = re.sub(r'(^- .+$)\n\n+(^- )', r'\1\n\2', content, flags=re.MULTILINE)
    
    # 7. 确保段落之间有一个空行
    # 先统一多个空行为两个换行
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 保存文件
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def format_all_chapters(directory):
    """
    格式化目录下所有章节文件
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"目录不存在: {directory}")
        return
    
    md_files = sorted(dir_path.glob('*.md'))
    formatted_count = 0
    
    for md_file in md_files:
        print(f"处理: {md_file.name}")
        if format_markdown_file(md_file):
            formatted_count += 1
            print(f"  已格式化")
        else:
            print(f"  无需修改")
    
    print(f"\n完成！共处理 {len(md_files)} 个文件，格式化了 {formatted_count} 个文件")


if __name__ == "__main__":
    chapters_dir = r"md\基础知识\第00章-教材完整版\split_chapters"
    format_all_chapters(chapters_dir)
