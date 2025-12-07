// Python code execution using Pyodide
let pyodide = null;

async function loadPyodideRuntime() {
    if (pyodide) return pyodide;
    
    try {
        // Use window.loadPyodide provided by the CDN
        if (typeof window.loadPyodide === 'undefined') {
            throw new Error('Pyodide not loaded. Make sure pyodide.js is included in your HTML.');
        }
        
        pyodide = await window.loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });
        console.log("Pyodide loaded successfully");
        return pyodide;
    } catch (error) {
        console.error("Error loading Pyodide:", error);
        throw error;
    }
}

async function runPythonCode(code) {
    try {
        if (!pyodide) {
            await loadPyodideRuntime();
        }
        
        // Capture stdout
        await pyodide.runPythonAsync(`
import sys
import io
sys.stdout = io.StringIO()
        `);
        
        // Run user code
        await pyodide.runPythonAsync(code);
        
        // Get output
        const output = await pyodide.runPythonAsync("sys.stdout.getvalue()");
        
        return {
            success: true,
            output: output,
            error: null
        };
    } catch (error) {
        return {
            success: false,
            output: null,
            error: error.message
        };
    }
}

async function runPythonTests(code, tests) {
    try {
        if (!pyodide) {
            await loadPyodideRuntime();
        }
        
        // Run user code
        await pyodide.runPythonAsync(code);
        
        const results = [];
        let allPassed = true;
        
        for (const test of tests) {
            try {
                const result = await pyodide.runPythonAsync(test.code);
                const passed = result === test.expected || String(result) === String(test.expected);
                
                results.push({
                    name: test.name,
                    passed: passed,
                    expected: test.expected,
                    got: result
                });
                
                if (!passed) allPassed = false;
            } catch (error) {
                results.push({
                    name: test.name,
                    passed: false,
                    error: error.message
                });
                allPassed = false;
            }
        }
        
        return {
            success: true,
            allPassed: allPassed,
            results: results
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

// SQL execution using sql.js
let SQL = null;
let db = null;

async function loadSqlJs() {
    if (SQL) return SQL;
    
    try {
        SQL = await initSqlJs({
            locateFile: file => `https://cdn.jsdelivr.net/npm/sql.js@1.8.0/dist/${file}`
        });
        console.log("sql.js loaded successfully");
        return SQL;
    } catch (error) {
        console.error("Error loading sql.js:", error);
        throw error;
    }
}

async function initDatabase(schema) {
    try {
        if (!SQL) {
            await loadSqlJs();
        }
        
        db = new SQL.Database();
        
        // Execute schema
        if (schema) {
            db.run(schema);
        }
        
        return {
            success: true,
            message: "Database initialized"
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

async function runSQLQuery(query) {
    try {
        if (!db) {
            throw new Error("Database not initialized");
        }
        
        const result = db.exec(query);
        
        return {
            success: true,
            result: result,
            rowsAffected: db.getRowsModified()
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

async function runSQLTests(userQuery, tests) {
    try {
        if (!db) {
            throw new Error("Database not initialized");
        }
        
        const results = [];
        let allPassed = true;
        
        // Run user query
        const userResult = db.exec(userQuery);
        
        for (const test of tests) {
            try {
                const expected = db.exec(test.expectedQuery);
                
                // Compare results
                const passed = JSON.stringify(userResult) === JSON.stringify(expected);
                
                results.push({
                    name: test.name,
                    passed: passed,
                    userResult: userResult,
                    expected: expected
                });
                
                if (!passed) allPassed = false;
            } catch (error) {
                results.push({
                    name: test.name,
                    passed: false,
                    error: error.message
                });
                allPassed = false;
            }
        }
        
        return {
            success: true,
            allPassed: allPassed,
            results: results
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

// Exercise submission
async function submitExercise(exerciseId, exerciseType, code, testsPassed, score) {
    try {
        const response = await fetch(`/exercises/${exerciseId}/submit/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                passed: testsPassed,
                score: score,
                attempt_data: {
                    code: code,
                    type: exerciseType,
                    timestamp: new Date().toISOString()
                }
            })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error submitting exercise:", error);
        return {
            success: false,
            error: error.message
        };
    }
}

// Utility function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Export functions
window.runPythonCode = runPythonCode;
window.runPythonTests = runPythonTests;
window.initDatabase = initDatabase;
window.runSQLQuery = runSQLQuery;
window.runSQLTests = runSQLTests;
window.submitExercise = submitExercise;
