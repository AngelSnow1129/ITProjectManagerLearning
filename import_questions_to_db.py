#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
软考系统架构师题库数据导入工具
"""

import pymysql
import json
import os
from pathlib import Path

# 导入数据库配置
try:
    from db_config import DB_CONFIG
except ImportError:
    # 如果没有配置文件，使用默认配置
    DB_CONFIG = {
        'host': 'mysql2.sqlpub.com',
        'port': 3307,
        'user': 'system4ai',
        'password': '',  # 请填写密码
        'database': 'system4ai',
        'charset': 'utf8mb4'
    }

def print_header():
    """打印标题"""
    print("=" * 60)
    print("软考系统架构师题库数据导入工具")
    print("=" * 60)

def connect_db():
    """连接数据库"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print(f"✓ 成功连接到数据库: {DB_CONFIG['host']}:{DB_CONFIG['port']}")
        return conn
    except Exception as e:
        print(f"✗ 数据库连接失败: {e}")
        return None

def create_tables(conn):
    """创建数据表"""
    print("\n[1/4] 创建数据表...")
    cursor = conn.cursor()
    
    # 选择题表
    create_select_table = """
    CREATE TABLE IF NOT EXISTS sl_arc_select_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        year VARCHAR(10) COMMENT '年份',
        exam_type VARCHAR(20) COMMENT '考试类型(上午/下午)',
        question_no INT COMMENT '题号',
        question_text TEXT COMMENT '题目内容',
        option_a TEXT COMMENT '选项A',
        option_b TEXT COMMENT '选项B',
        option_c TEXT COMMENT '选项C',
        option_d TEXT COMMENT '选项D',
        correct_answer VARCHAR(10) COMMENT '正确答案',
        explanation TEXT COMMENT '解析',
        knowledge_point VARCHAR(200) COMMENT '知识点',
        difficulty VARCHAR(20) COMMENT '难度',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        INDEX idx_year (year),
        INDEX idx_knowledge (knowledge_point)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='选择题题库';
    """
    
    # 案例题表
    create_case_table = """
    CREATE TABLE IF NOT EXISTS sl_arc_case_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        year VARCHAR(10) COMMENT '年份',
        case_no INT COMMENT '案例编号',
        case_background TEXT COMMENT '案例背景',
        question_no INT COMMENT '问题编号',
        question_text TEXT COMMENT '问题内容',
        reference_answer TEXT COMMENT '参考答案',
        scoring_points TEXT COMMENT '评分要点',
        knowledge_point VARCHAR(200) COMMENT '知识点',
        difficulty VARCHAR(20) COMMENT '难度',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        INDEX idx_year (year),
        INDEX idx_case (case_no)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='案例分析题库';
    """
    
    # 论文题表
    create_essay_table = """
    CREATE TABLE IF NOT EXISTS sl_arc_essay_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        year VARCHAR(10) COMMENT '年份',
        essay_no INT COMMENT '论文编号',
        topic TEXT COMMENT '论文题目',
        requirements TEXT COMMENT '写作要求',
        key_points TEXT COMMENT '关键要点',
        sample_outline TEXT COMMENT '参考提纲',
        knowledge_point VARCHAR(200) COMMENT '知识点',
        difficulty VARCHAR(20) COMMENT '难度',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        INDEX idx_year (year)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='论文题库';
    """
    
    try:
        cursor.execute(create_select_table)
        cursor.execute(create_case_table)
        cursor.execute(create_essay_table)
        conn.commit()
        print("✓ 数据表创建完成")
        return True
    except Exception as e:
        print(f"警告: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def import_select_questions(conn):
    """导入选择题"""
    print("\n[2/4] 导入选择题...")
    cursor = conn.cursor()
    
    # 示例数据
    sample_questions = [
        {
            'year': '2024',
            'exam_type': '上午',
            'question_no': 1,
            'question_text': '以下关于信息系统的描述，正确的是？',
            'option_a': '信息系统只包括硬件和软件',
            'option_b': '信息系统是由人、硬件、软件、数据和网络组成的系统',
            'option_c': '信息系统不需要人的参与',
            'option_d': '信息系统只处理数字信息',
            'correct_answer': 'B',
            'explanation': '信息系统是一个人机结合的系统，包括人、硬件、软件、数据和网络等要素。',
            'knowledge_point': '信息系统基础',
            'difficulty': '简单'
        }
    ]
    
    insert_sql = """
    INSERT INTO sl_arc_select_questions 
    (year, exam_type, question_no, question_text, option_a, option_b, option_c, option_d, 
     correct_answer, explanation, knowledge_point, difficulty)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        count = 0
        for q in sample_questions:
            cursor.execute(insert_sql, (
                q['year'], q['exam_type'], q['question_no'], q['question_text'],
                q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_answer'], q['explanation'], q['knowledge_point'], q['difficulty']
            ))
            count += 1
        
        conn.commit()
        print(f"✓ 成功导入 {count} 条选择题")
        return count
    except Exception as e:
        print(f"✗ 导入选择题失败: {e}")
        conn.rollback()
        return 0
    finally:
        cursor.close()

def import_case_questions(conn):
    """导入案例题"""
    print("\n[3/4] 导入案例题...")
    cursor = conn.cursor()
    
    # 示例数据
    sample_cases = [
        {
            'year': '2024',
            'case_no': 1,
            'case_background': '某企业计划开发一个电子商务系统...',
            'question_no': 1,
            'question_text': '请简述该项目的主要风险及应对措施。',
            'reference_answer': '主要风险包括：技术风险、进度风险、成本风险等...',
            'scoring_points': '识别风险(3分)、应对措施(4分)',
            'knowledge_point': '项目风险管理',
            'difficulty': '中等'
        }
    ]
    
    insert_sql = """
    INSERT INTO sl_arc_case_questions 
    (year, case_no, case_background, question_no, question_text, reference_answer, 
     scoring_points, knowledge_point, difficulty)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        count = 0
        for c in sample_cases:
            cursor.execute(insert_sql, (
                c['year'], c['case_no'], c['case_background'], c['question_no'],
                c['question_text'], c['reference_answer'], c['scoring_points'],
                c['knowledge_point'], c['difficulty']
            ))
            count += 1
        
        conn.commit()
        print(f"✓ 成功导入 {count} 条案例题")
        return count
    except Exception as e:
        print(f"✗ 导入案例题失败: {e}")
        conn.rollback()
        return 0
    finally:
        cursor.close()

def import_essay_questions(conn):
    """导入论文题"""
    print("\n[4/4] 导入论文题...")
    cursor = conn.cursor()
    
    # 示例数据
    sample_essays = [
        {
            'year': '2024',
            'essay_no': 1,
            'topic': '论信息系统项目的风险管理',
            'requirements': '请围绕以下三个方面进行论述：1.项目背景 2.风险识别 3.风险应对',
            'key_points': '风险识别方法、风险评估、风险应对策略',
            'sample_outline': '一、项目背景\n二、风险识别\n三、风险应对\n四、总结',
            'knowledge_point': '项目风险管理',
            'difficulty': '困难'
        }
    ]
    
    insert_sql = """
    INSERT INTO sl_arc_essay_questions 
    (year, essay_no, topic, requirements, key_points, sample_outline, knowledge_point, difficulty)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        count = 0
        for e in sample_essays:
            cursor.execute(insert_sql, (
                e['year'], e['essay_no'], e['topic'], e['requirements'],
                e['key_points'], e['sample_outline'], e['knowledge_point'], e['difficulty']
            ))
            count += 1
        
        conn.commit()
        print(f"✓ 成功导入 {count} 条论文题")
        return count
    except Exception as e:
        print(f"✗ 导入论文题失败: {e}")
        conn.rollback()
        return 0
    finally:
        cursor.close()

def main():
    """主函数"""
    print_header()
    
    # 连接数据库
    conn = connect_db()
    if not conn:
        return
    
    try:
        # 创建表
        create_tables(conn)
        
        # 导入数据
        select_count = import_select_questions(conn)
        case_count = import_case_questions(conn)
        essay_count = import_essay_questions(conn)
        
        # 统计
        print("\n" + "=" * 60)
        print("导入完成!")
        print("=" * 60)
        print(f"选择题: {select_count} 条")
        print(f"案例题: {case_count} 条")
        print(f"论文题: {essay_count} 条")
        print(f"总计: {select_count + case_count + essay_count} 条")
        print("=" * 60)
        
    finally:
        conn.close()
        print("\n数据库连接已关闭")

if __name__ == '__main__':
    main()
