// 完整的离线Markdown解析器
// 当所有CDN都无法访问时使用

(function() {
    'use strict';

    // 等待一段时间检查marked是否加载
    let checkCount = 0;
    const maxChecks = 30; // 3秒
    
    const checkInterval = setInterval(() => {
        checkCount++;
        
        if (typeof marked !== 'undefined') {
            console.log('✓ Marked.js已从CDN加载');
            clearInterval(checkInterval);
            return;
        }
        
        if (checkCount >= maxChecks) {
            console.warn('⚠ 所有CDN加载失败，启用离线Markdown解析器');
            clearInterval(checkInterval);
            initOfflineParser();
        }
    }, 100);

    function initOfflineParser() {
        window.marked = {
            parse: function(markdown) {
                if (!markdown) return '';
                return parseMarkdown(markdown);
            },
            setOptions: function(options) {
                // 兼容性方法
            }
        };
        
        console.log('✓ 离线Markdown解析器已启用');
        
        // 触发自定义事件通知页面
        window.dispatchEvent(new Event('markedReady'));
    }

    function parseMarkdown(markdown) {
        let html = markdown;
        
        // 保存代码块
        const codeBlocks = [];
        html = html.replace(/```(\w*)\n?([\s\S]*?)```/g, (match, lang, code) => {
            codeBlocks.push({ lang, code: code.trim() });
            return `__CODEBLOCK_${codeBlocks.length - 1}__`;
        });
        
        // 保存行内代码
        const inlineCodes = [];
        html = html.replace(/`([^`\n]+)`/g, (match, code) => {
            inlineCodes.push(code);
            return `__INLINECODE_${inlineCodes.length - 1}__`;
        });
        
        // 标题
        html = html.replace(/^######\s+(.*)$/gm, '<h6>$1</h6>');
        html = html.replace(/^#####\s+(.*)$/gm, '<h5>$1</h5>');
        html = html.replace(/^####\s+(.*)$/gm, '<h4>$1</h4>');
        html = html.replace(/^###\s+(.*)$/gm, '<h3>$1</h3>');
        html = html.replace(/^##\s+(.*)$/gm, '<h2>$1</h2>');
        html = html.replace(/^#\s+(.*)$/gm, '<h1>$1</h1>');
        
        // 水平线
        html = html.replace(/^---+$/gm, '<hr>');
        html = html.replace(/^\*\*\*+$/gm, '<hr>');
        
        // 表格
        html = parseTable(html);
        
        // 引用块
        html = html.replace(/^>\s+(.*)$/gm, '<blockquote>$1</blockquote>');
        
        // 粗体
        html = html.replace(/\*\*([^\*\n]+)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/__([^_\n]+)__/g, '<strong>$1</strong>');
        
        // 斜体
        html = html.replace(/\*([^\*\n]+)\*/g, '<em>$1</em>');
        html = html.replace(/_([^_\n]+)_/g, '<em>$1</em>');
        
        // 删除线
        html = html.replace(/~~([^~\n]+)~~/g, '<del>$1</del>');
        
        // 链接
        html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
        
        // 图片
        html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" loading="lazy">');
        
        // 列表
        html = parseList(html);
        
        // 段落
        html = html.split('\n\n').map(para => {
            para = para.trim();
            if (!para) return '';
            if (para.match(/^<(h[1-6]|ul|ol|pre|blockquote|hr|table|div)/)) {
                return para;
            }
            if (para.includes('</li>') || para.includes('</h')) {
                return para;
            }
            return `<p>${para}</p>`;
        }).join('\n');
        
        // 恢复行内代码
        inlineCodes.forEach((code, i) => {
            html = html.replace(`__INLINECODE_${i}__`, `<code>${escapeHtml(code)}</code>`);
        });
        
        // 恢复代码块
        codeBlocks.forEach((block, i) => {
            const langClass = block.lang ? ` class="language-${block.lang}"` : '';
            html = html.replace(`__CODEBLOCK_${i}__`, 
                `<pre><code${langClass}>${escapeHtml(block.code)}</code></pre>`);
        });
        
        // 换行
        html = html.replace(/\n/g, '<br>');
        
        // 清理
        html = html.replace(/<br><\/h/g, '</h');
        html = html.replace(/<br><\/li>/g, '</li>');
        html = html.replace(/<br><\/blockquote>/g, '</blockquote>');
        html = html.replace(/<br><hr>/g, '<hr>');
        html = html.replace(/<hr><br>/g, '<hr>');
        html = html.replace(/<br><\/pre>/g, '</pre>');
        html = html.replace(/<pre><br>/g, '<pre>');
        html = html.replace(/<br><\/table>/g, '</table>');
        html = html.replace(/<table><br>/g, '<table>');
        
        return html;
    }

    function parseTable(html) {
        const lines = html.split('\n');
        const result = [];
        let i = 0;
        
        while (i < lines.length) {
            const line = lines[i];
            
            // 检查是否是表格行
            if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
                const tableLines = [line];
                i++;
                
                // 收集表格的所有行
                while (i < lines.length && lines[i].trim().startsWith('|')) {
                    tableLines.push(lines[i]);
                    i++;
                }
                
                // 解析表格
                if (tableLines.length >= 2) {
                    result.push(buildTable(tableLines));
                } else {
                    result.push(...tableLines);
                }
            } else {
                result.push(line);
                i++;
            }
        }
        
        return result.join('\n');
    }

    function buildTable(lines) {
        let table = '<table>\n';
        
        // 表头
        const headers = lines[0].split('|').filter(h => h.trim()).map(h => h.trim());
        table += '<thead>\n<tr>\n';
        headers.forEach(h => {
            table += `<th>${h}</th>\n`;
        });
        table += '</tr>\n</thead>\n';
        
        // 跳过分隔行
        if (lines.length > 2) {
            table += '<tbody>\n';
            for (let i = 2; i < lines.length; i++) {
                const cells = lines[i].split('|').filter(c => c.trim()).map(c => c.trim());
                if (cells.length > 0) {
                    table += '<tr>\n';
                    cells.forEach(c => {
                        table += `<td>${c}</td>\n`;
                    });
                    table += '</tr>\n';
                }
            }
            table += '</tbody>\n';
        }
        
        table += '</table>';
        return table;
    }

    function parseList(html) {
        const lines = html.split('\n');
        const result = [];
        let inList = false;
        let listType = null;
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const trimmed = line.trim();
            
            // 无序列表
            if (trimmed.match(/^[\*\-\+]\s+/)) {
                if (!inList || listType !== 'ul') {
                    if (inList) result.push(`</${listType}>`);
                    result.push('<ul>');
                    inList = true;
                    listType = 'ul';
                }
                result.push(`<li>${trimmed.replace(/^[\*\-\+]\s+/, '')}</li>`);
            }
            // 有序列表
            else if (trimmed.match(/^\d+\.\s+/)) {
                if (!inList || listType !== 'ol') {
                    if (inList) result.push(`</${listType}>`);
                    result.push('<ol>');
                    inList = true;
                    listType = 'ol';
                }
                result.push(`<li>${trimmed.replace(/^\d+\.\s+/, '')}</li>`);
            }
            // 非列表行
            else {
                if (inList) {
                    result.push(`</${listType}>`);
                    inList = false;
                    listType = null;
                }
                result.push(line);
            }
        }
        
        if (inList) {
            result.push(`</${listType}>`);
        }
        
        return result.join('\n');
    }

    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
})();
