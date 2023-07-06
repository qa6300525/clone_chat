
marked.setOptions({
  highlight: function (code) {
    return hljs.highlightAuto(code).value;
  },
  escapes: {
      ')': ')',
      ']': ']'
    }
});

// TODO: https://www.npmjs.com/package/marked-highlight
//marked.use(markedHighlight({
//  langPrefix: 'hljs language-',
//  highlight(code, lang) {
//    const language = hljs.getLanguage(lang) ? lang : 'plaintext';
//    return hljs.highlight(code, { language }).value;
//  }
//}));


function convertMarkdownToHTML(markdownText) {
  // 使用 marked.js 将 Markdown 转换为 HTML
  const htmlText = marked.parse(markdownText);
  return htmlText;
}