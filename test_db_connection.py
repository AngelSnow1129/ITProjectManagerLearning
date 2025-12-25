#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库连接测试工具
"""

import pymysql

try:
    from db_config import DB_CONFIG
except ImportError:
    print("错误: 找不到 db_config.py 文件")
    print("请先创建 db_config.py 并配置数据库信息")
    exit(1)

def test_connection():
    """测试数据库连接"""
    print("=" * 60)
    print("数据库连接测试")
    print("=" * 60)
    
    print(f"\n连接信息:")
    print(f"  主机: {DB_CONFIG['host']}")
    print(f"  端口: {DB_CONFIG['port']}")
    print(f"  用户: {DB_CONFIG['user']}")
    print(f"  数据库: {DB_CONFIG['database']}")
    
    try:
        print("\n正在连接数据库...")
        conn = pymysql.connect(**DB_CONFIG)
        print("✓ 数据库连接成功!")
        
        cursor = conn.cursor()
        
        # 测试查询
        print("\n测试查询...")
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ MySQL版本: {version[0]}")
        
        # 查看现有表
        print("\n查看现有表...")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        if tables:
            print(f"✓ 找到 {len(tables)} 个表:")
            for table in tables:
                print(f"  - {table[0]}")
                
                # 查看表结构
                cursor.execute(f"DESCRIBE {table[0]}")
                columns = cursor.fetchall()
                print(f"    字段数: {len(columns)}")
                
                # 查看记录数
                cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
                count = cursor.fetchone()[0]
                print(f"    记录数: {count}")
        else:
            print("  数据库中暂无表")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 60)
        print("测试完成!")
        print("=" * 60)
        
    except pymysql.Error as e:
        print(f"\n✗ 数据库错误: {e}")
        print("\n请检查:")
        print("  1. 数据库密码是否正确")
        print("  2. 数据库服务是否可访问")
        print("  3. 用户权限是否足够")
    except Exception as e:
        print(f"\n✗ 未知错误: {e}")

if __name__ == '__main__':
    test_connection()
