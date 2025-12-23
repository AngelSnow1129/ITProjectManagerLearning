/**
 * 访问统计功能
 * 热度：总访问次数
 * 关注度：唯一IP访问次数
 */

class VisitStatistics {
    constructor() {
        this.storageKey = 'visit_statistics';
        this.ipStorageKey = 'visit_ips';
        this.sessionKey = 'current_session_counted';
    }

    // 初始化统计数据
    initStats() {
        const stats = this.getStats();
        if (!stats) {
            const initialStats = {
                totalVisits: 0,
                uniqueVisits: 0,
                lastUpdate: new Date().toISOString()
            };
            localStorage.setItem(this.storageKey, JSON.stringify(initialStats));
            localStorage.setItem(this.ipStorageKey, JSON.stringify([]));
            return initialStats;
        }
        return stats;
    }

    // 获取统计数据
    getStats() {
        const data = localStorage.getItem(this.storageKey);
        return data ? JSON.parse(data) : null;
    }

    // 获取IP列表
    getIPs() {
        const data = localStorage.getItem(this.ipStorageKey);
        return data ? JSON.parse(data) : [];
    }

    // 生成浏览器指纹作为IP替代
    async generateFingerprint() {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        ctx.textBaseline = 'top';
        ctx.font = '14px Arial';
        ctx.fillText('Browser Fingerprint', 2, 2);
        
        const fingerprint = canvas.toDataURL();
        const screen = `${window.screen.width}x${window.screen.height}`;
        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const language = navigator.language;
        const platform = navigator.platform;
        
        const data = `${fingerprint}-${screen}-${timezone}-${language}-${platform}`;
        
        // 简单哈希
        let hash = 0;
        for (let i = 0; i < data.length; i++) {
            const char = data.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return hash.toString(36);
    }

    // 记录访问
    async recordVisit() {
        // 检查本次会话是否已计数
        if (sessionStorage.getItem(this.sessionKey)) {
            return this.getStats();
        }

        const stats = this.initStats();
        const fingerprint = await this.generateFingerprint();
        const ips = this.getIPs();

        // 增加总访问次数（热度）
        stats.totalVisits++;

        // 检查是否为新的唯一访问者（关注度）
        if (!ips.includes(fingerprint)) {
            ips.push(fingerprint);
            stats.uniqueVisits++;
            localStorage.setItem(this.ipStorageKey, JSON.stringify(ips));
        }

        stats.lastUpdate = new Date().toISOString();
        localStorage.setItem(this.storageKey, JSON.stringify(stats));
        
        // 标记本次会话已计数
        sessionStorage.setItem(this.sessionKey, 'true');

        return stats;
    }

    // 格式化数字显示
    formatNumber(num) {
        if (num >= 10000) {
            return (num / 10000).toFixed(1) + 'w';
        } else if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'k';
        }
        return num.toString();
    }

    // 显示统计信息
    async displayStats(containerId) {
        const stats = await this.recordVisit();
        const container = document.getElementById(containerId);
        
        if (container) {
            container.innerHTML = `
                <div style="display: flex; gap: 20px; align-items: center; font-size: 14px; color: #666;">
                    <div style="display: flex; align-items: center; gap: 5px;">
                        <span style="color: #ff6b6b;">🔥</span>
                        <span>热度: <strong style="color: #ff6b6b;">${this.formatNumber(stats.totalVisits)}</strong></span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 5px;">
                        <span style="color: #4ecdc4;">👁️</span>
                        <span>关注度: <strong style="color: #4ecdc4;">${this.formatNumber(stats.uniqueVisits)}</strong></span>
                    </div>
                </div>
            `;
        }
    }

    // 重置统计（仅用于测试）
    resetStats() {
        localStorage.removeItem(this.storageKey);
        localStorage.removeItem(this.ipStorageKey);
        sessionStorage.removeItem(this.sessionKey);
        console.log('统计数据已重置');
    }
}

// 创建全局实例
const visitStats = new VisitStatistics();

// 获取当前年份
function getCurrentYear() {
    return new Date().getFullYear();
}

// 更新页面中的年份
function updateCopyrightYear() {
    const yearElements = document.querySelectorAll('.copyright-year, [data-year]');
    const currentYear = getCurrentYear();
    
    yearElements.forEach(element => {
        element.textContent = currentYear;
    });

    // 更新所有包含 "© 2024" 的文本
    const allElements = document.querySelectorAll('p, span, div');
    allElements.forEach(element => {
        if (element.childNodes.length === 1 && element.childNodes[0].nodeType === 3) {
            const text = element.textContent;
            if (text.includes('© 2024') || text.includes('© 2025')) {
                element.textContent = text.replace(/© \d{4}/, `© ${currentYear}`);
            }
        }
    });
}

// 页面加载完成后执行
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        updateCopyrightYear();
        visitStats.displayStats('visit-stats');
    });
}
