// Monaco Editor setup for NSI Portal
let monacoEditor = null;

/**
 * Initialize Monaco Editor for code exercises
 * @param {string} elementId - ID of the container element
 * @param {string} language - Programming language (python or sql)
 * @param {string} initialCode - Starting code
 * @returns {Promise<object>} The Monaco editor instance
 */
async function initializeMonacoEditor(elementId, language, initialCode = '') {
    // Wait for Monaco to be loaded
    if (typeof monaco === 'undefined') {
        console.error('Monaco Editor not loaded');
        return null;
    }

    // Map exercise types to Monaco languages
    const languageMap = {
        'PYTHON': 'python',
        'SQL': 'sql',
        'python': 'python',
        'sql': 'sql'
    };

    const monacoLanguage = languageMap[language] || 'python';

    // Create editor
    monacoEditor = monaco.editor.create(document.getElementById(elementId), {
        value: initialCode,
        language: monacoLanguage,
        theme: 'vs-dark',
        automaticLayout: true,
        minimap: {
            enabled: false
        },
        fontSize: 14,
        lineNumbers: 'on',
        roundedSelection: false,
        scrollBeyondLastLine: false,
        readOnly: false,
        cursorStyle: 'line',
        wordWrap: 'on',
        wrappingIndent: 'indent',
        formatOnPaste: true,
        formatOnType: true,
        suggestOnTriggerCharacters: true,
        acceptSuggestionOnEnter: 'on',
        tabCompletion: 'on',
        quickSuggestions: true,
        snippetSuggestions: 'inline',
        scrollbar: {
            vertical: 'visible',
            horizontal: 'visible',
            useShadows: false,
            verticalScrollbarSize: 10,
            horizontalScrollbarSize: 10
        },
        // Enhanced Python features
        ...(monacoLanguage === 'python' && {
            suggest: {
                showWords: true,
                showFunctions: true,
                showVariables: true
            }
        })
    });

    // Add keyboard shortcuts
    monacoEditor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, function() {
        if (typeof testCode === 'function') {
            testCode();
        }
    });

    monacoEditor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, function() {
        if (typeof testCode === 'function') {
            testCode();
        }
    });

    // Add Python-specific completions
    if (monacoLanguage === 'python') {
        monaco.languages.registerCompletionItemProvider('python', {
            provideCompletionItems: (model, position) => {
                const suggestions = [
                    {
                        label: 'def',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'def ${1:function_name}(${2:params}):\n    ${3:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'Define a function'
                    },
                    {
                        label: 'for',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'for ${1:item} in ${2:iterable}:\n    ${3:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'For loop'
                    },
                    {
                        label: 'if',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'if ${1:condition}:\n    ${2:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'If statement'
                    },
                    {
                        label: 'while',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'while ${1:condition}:\n    ${2:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'While loop'
                    },
                    {
                        label: 'class',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'class ${1:ClassName}:\n    def __init__(self, ${2:params}):\n        ${3:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'Define a class'
                    },
                    {
                        label: 'try',
                        kind: monaco.languages.CompletionItemKind.Snippet,
                        insertText: 'try:\n    ${1:pass}\nexcept ${2:Exception} as ${3:e}:\n    ${4:pass}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'Try-except block'
                    }
                ];
                return { suggestions: suggestions };
            }
        });
    }

    // Add SQL-specific completions
    if (monacoLanguage === 'sql') {
        monaco.languages.registerCompletionItemProvider('sql', {
            provideCompletionItems: (model, position) => {
                const suggestions = [
                    {
                        label: 'SELECT',
                        kind: monaco.languages.CompletionItemKind.Keyword,
                        insertText: 'SELECT ${1:*} FROM ${2:table}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'SELECT statement'
                    },
                    {
                        label: 'WHERE',
                        kind: monaco.languages.CompletionItemKind.Keyword,
                        insertText: 'WHERE ${1:condition}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'WHERE clause'
                    },
                    {
                        label: 'JOIN',
                        kind: monaco.languages.CompletionItemKind.Keyword,
                        insertText: 'JOIN ${1:table} ON ${2:condition}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'JOIN clause'
                    },
                    {
                        label: 'GROUP BY',
                        kind: monaco.languages.CompletionItemKind.Keyword,
                        insertText: 'GROUP BY ${1:column}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'GROUP BY clause'
                    },
                    {
                        label: 'ORDER BY',
                        kind: monaco.languages.CompletionItemKind.Keyword,
                        insertText: 'ORDER BY ${1:column} ${2|ASC,DESC|}',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                        documentation: 'ORDER BY clause'
                    }
                ];
                return { suggestions: suggestions };
            }
        });
    }

    return monacoEditor;
}

/**
 * Get the current code from Monaco Editor
 * @returns {string} The current code
 */
function getMonacoEditorValue() {
    if (monacoEditor) {
        return monacoEditor.getValue();
    }
    return '';
}

/**
 * Set the code in Monaco Editor
 * @param {string} code - Code to set
 */
function setMonacoEditorValue(code) {
    if (monacoEditor) {
        monacoEditor.setValue(code);
    }
}

/**
 * Resize Monaco Editor (useful for responsive layouts)
 */
function resizeMonacoEditor() {
    if (monacoEditor) {
        monacoEditor.layout();
    }
}

/**
 * Toggle Monaco Editor theme
 * @param {string} theme - Theme name ('vs', 'vs-dark', 'hc-black')
 */
function setMonacoEditorTheme(theme = 'vs-dark') {
    if (monacoEditor) {
        monaco.editor.setTheme(theme);
    }
}

/**
 * Dispose Monaco Editor (cleanup)
 */
function disposeMonacoEditor() {
    if (monacoEditor) {
        monacoEditor.dispose();
        monacoEditor = null;
    }
}

// Handle window resize
window.addEventListener('resize', () => {
    resizeMonacoEditor();
});
