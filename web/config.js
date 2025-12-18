// 信息系统项目管理师学习平台配置文件

const CONFIG = {
    // 考试类型配置
    examTypes: {
        projectmanager: {
            name: '信息系统项目管理师',
            description: '软考高级资格考试',
            chapters: [
                { 
                    id: '01', 
                    name: '信息化发展', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '02', 
                    name: '信息技术发展', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '03', 
                    name: '信息系统治理', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '04', 
                    name: '信息系统管理', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '05', 
                    name: '信息系统工程', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '06', 
                    name: '项目管理概论', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '07', 
                    name: '项目立项管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '08', 
                    name: '项目整合管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '09', 
                    name: '项目范围管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '10', 
                    name: '项目进度管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '11', 
                    name: '项目成本管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '12', 
                    name: '项目质量管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '13', 
                    name: '项目资源管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '14', 
                    name: '项目沟通管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '15', 
                    name: '项目风险管理', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '16', 
                    name: '项目采购管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '17', 
                    name: '项目干系人管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '18', 
                    name: '项目绩效域', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '19', 
                    name: '配置与变更管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '20', 
                    name: '高级项目管理', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '21', 
                    name: '项目管理科学基础', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '22', 
                    name: '组织通用治理', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '23', 
                    name: '法律法规与标准规范', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '24', 
                    name: '项目管理案例分析', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '25', 
                    name: '论文写作指导', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                }
            ]
        }
    },

    // 视图类型配置
    viewTypes: {
        normal: {
            name: '完整章节',
            icon: '📖',
            folder: '',
            suffix: ''
        },
        keypoint: {
            name: '重点提纲',
            icon: '⭐',
            folder: 'keypoint',
            suffix: '_知识提纲'
        },
        mustknow: {
            name: '必背内容',
            icon: '🎯',
            folder: 'keypoint',
            suffix: '_必背补充'
        }
    },

    // 特殊文件映射（处理文件名不一致的情况）
    fileMapping: {
        keypoint: {},
        mustknow: {}
    }
};

// 导出配置
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
