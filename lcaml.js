console.log("loading lcaml.js");

let currentScriptPath = document.currentScript.src;

function getDirectoryPath(filePath) {
    const directory = filePath.substring(0, filePath.lastIndexOf('/'));
    return directory || '/';
}

function populateScriptContentThenCall(callback, script, ...otherArgs) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", script.src)
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            script.textContent = xhr.responseText;
            callback(script, ...otherArgs);
        }
    };
    xhr.send();
}

function getDefaultLcamlContext() {
    let parser = new DOMParser();
    return {"parseFromString": (content, doctype) => parser.parseFromString(content, doctype)};
}

/**
 * Initialize LCaml functionality: brython and type="text/lcaml" scripts
 * @param {object} cache brython parameter: whether to cache compiled modules (reduces load time massively)
 * @param {number} debug brython parameter: debug level (0, 1, 2, 10)
 */
function initLcaml(cache = false, debug = 0) {
    if (typeof cache !== "boolean") {
        throw new Error("cache must be a boolean");
    }
    if (typeof debug !== "number") {
        throw new Error("debug must be a number");
    }
    if (debug !== 0 && debug !== 1 && debug !== 2 && debug !== 10) {
        throw new Error("debug must be 0, 1, 2, or 10");
    }
    if (window.lcamlContext !== undefined || window.runLcaml !== undefined)
        return;
    let script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/brython@3.11.1/brython.min.js";
    script.onload = () => {
        let script = document.createElement("script");
        script.src = "https://cdn.jsdelivr.net/npm/brython@3.11.1/brython_stdlib.js";
        script.onload = () => {
            let script = document.createElement("script");
            script.src = `${getDirectoryPath(currentScriptPath)}/lcaml_main.py`;
            script.type = "text/python";
            let runScript = (script, lcamlMain) => {
                if (script.src && !script.textContent) {
                    populateScriptContentThenCall(runScript, script, lcamlMain);
                    return;
                }
                let scriptName;
                if (script.src)
                    scriptName = script.src;
                else
                    scriptName = "<inline-script>";
                console.log(`running script ${scriptName}`);
                try {
                    window.lcamlContext = lcamlMain(
                        script.src ? script.src : "<unknown>",
                        script.textContent,
                        window.lcamlContext,
                    );
                } catch (error) {
                    console.error("error executing lcaml script:", error);
                }
            };
            let scriptExecutor = (lcamlMain) => {
                console.log("successfully loaded lcaml.js functionality");
                let scripts = document.querySelectorAll('script[type="text/lcaml"]');
                window.lcamlContext = getDefaultLcamlContext();
                window.runLcaml = (script) => runScript(script, lcamlMain);
                scripts.forEach(window.runLcaml);
            };
            window.brythonLoadLcamlMainCallback = (lcamlMain) => {
                if (document.readyState !== "loading")
                    scriptExecutor(lcamlMain);
                else
                    document.addEventListener("DOMContentLoaded", () => scriptExecutor(lcamlMain));
            };
            document.head.appendChild(script);
            brython({cache: cache, debug: debug});
        };
        document.head.appendChild(script);
    };
    document.head.appendChild(script);
}

window.initLcaml = initLcaml;