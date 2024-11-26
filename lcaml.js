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

/**
 * Initialize LCaml functionality: brython and type="text/lcaml" scripts
 */
function initLcaml() {
    if (window.lcamlData !== undefined)
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
                    window.lcamlData.lcamlContext = lcamlMain(
                        script.src ? script.src : "<unknown>",
                        script.textContent,
                        window.lcamlData.lcamlContext,
                    );
                } catch (error) {
                    console.error("error executing lcaml script:", error);
                }
            };
            let scriptExecutor = (lcamlMain) => {
                console.log("successfully loaded lcaml.js functionality");
                let scripts = document.querySelectorAll('script[type="text/lcaml"]');
                window.lcamlData = {}
                window.lcamlData.lcamlContext = {}
                window.lcamlData.runLcaml = (script) => runScript(script, lcamlMain)
                scripts.forEach(window.lcamlData.runLcaml);
            };
            window.brythonLoadLcamlMainCallback = (lcamlMain) => {
                if (document.readyState !== "loading")
                    scriptExecutor(lcamlMain);
                else
                    document.addEventListener("DOMContentLoaded", () => scriptExecutor(lcamlMain));
            };
            document.head.appendChild(script);
            brython();
        };
        document.head.appendChild(script);
    };
    document.head.appendChild(script);
}

window.initLcaml = initLcaml;