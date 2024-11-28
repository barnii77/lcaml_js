import wcaml
from browser import window
from lcaml_py_repo.lcaml_py.core import interpreter as interpreter_mod
from lcaml_py_repo.lcaml_py.core import interpreter_vm as interpreter_vm_mod
from lcaml_py_repo.lcaml_py.core import lcaml_expression
from lcaml_py_repo.lcaml_py.core import pyffi
from lcaml_py_repo.lcaml_py.core.lcaml_lexer import Syntax
from lcaml_py_repo.lcaml_py.core.lcaml_utils import get_marked_code_snippet


def get_lcaml_traceback(exc: Exception) -> str:
    tb_lines = ["LCaml Traceback (most recent call last):"]
    if not hasattr(exc, "__lcaml_traceback_info"):
        tb_lines.append("Unable to construct lcaml traceback.")
    else:
        tb_info = getattr(exc, "__lcaml_traceback_info")
        code_lines = None
        for loc in reversed(tb_info):
            if isinstance(loc, interpreter_mod.Interpreter):
                tb_lines.append(f"In file {loc.vm.file}:\n")
                code_lines = loc.code.splitlines()
            elif isinstance(loc, interpreter_vm_mod.InterpreterVM):
                tb_lines.append(f"On line {loc.statement_line}:")
                tb_lines.append(
                    get_marked_code_snippet(code_lines, loc.statement_line - 1, 3)
                    if code_lines is not None
                    else "<code unavailable>"
                )
                tb_lines.append("")
            elif isinstance(loc, int):
                tb_lines.append(f"On line {loc}:")
                tb_lines.append(
                    get_marked_code_snippet(code_lines, loc - 1, 3)
                    if code_lines is not None
                    else "<code unavailable>"
                )
                tb_lines.append("")
            elif (
                isinstance(loc, tuple)
                and len(loc) == 2
                and isinstance(loc[0], str)
                and isinstance(loc[1], str)
            ):
                file, code = loc
                tb_lines.append(f"In file {file}:\n")
                code_lines = code.splitlines()
            elif isinstance(loc, str):
                tb_lines.append("Note: " + loc + "\n")
            else:
                raise TypeError("Invalid traceback entry encountered.")

    # this chaos below improves error output format by trying to parse `repr(exc)` to some degree
    r = repr(exc)
    exc_name = ""
    while r[0].isalnum():
        exc_name += r[0]
        r = r[1:]
    if r.startswith("('") or r.startswith('("'):
        r = r[2:]
    elif r.startswith("("):
        r = r[1:]
    if r.endswith("')") or r.endswith('")'):
        r = r[:-2]
    elif r.endswith(")"):
        r = r[:-1]
    if r:
        r = ": " + r
    out = exc_name + r
    if out:
        out = "Raised " + out
    tb_lines.append(out)
    return "\n".join(tb_lines)


def main(file, code, context_js_obj):
    lcaml_expression.SUPPRESS_JIT = True
    try:
        interpreter = interpreter_mod.Interpreter(code, file=file)
        context = interpreter_mod.get_builtins()
        context.update(wcaml.module(context).value.fields)
        for k in context_js_obj:
            context[k] = context_js_obj[k]
        result = interpreter.execute(context)

        # context cleanup
        out_context = context.copy()
        out_context["->"] = pyffi._lcaml_to_python(result)
        if Syntax._interpreter_intrinsic in out_context:
            out_context.pop(Syntax._interpreter_intrinsic)
        if Syntax._vm_intrinsic in out_context:
            out_context.pop(Syntax._vm_intrinsic)
        if Syntax._this_intrinsic in out_context:
            out_context.pop(Syntax._this_intrinsic)
    except Exception as e:
        print(get_lcaml_traceback(e))
        raise e
    return out_context


if __name__ == "__main__":
    window.brythonLoadLcamlMainCallback(main)
