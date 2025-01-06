from browser import window, document, ajax, alert, bind, timer
from lcaml_py_repo.lcaml_py.core import pyffi
from lcaml_py_repo.lcaml_py.core import interpreter_types
from typing import Any


def wrap_argless_lcaml_func(func):
    """returns a function that you can call without any parameters that automatically passes a () value as the 1
    required parameter of the lcaml function"""
    return lambda: func(interpreter_types.Object(interpreter_types.DType.UNIT, None))


def nested_set(item, attr: str, value: Any):
    path = attr.split(".")
    attr = path[-1]
    path = path[:-1]
    sub_item = item
    for p in path:
        sub_item = sub_item[p]
    sub_item[attr] = value


def nested_get(item, attr: str):
    path = attr.split(".")
    sub_item = item
    for p in path:
        sub_item = sub_item[p]
    return sub_item


def nested_exists(item, attr: str):
    path = attr.split(".")
    sub_item = item
    for p in path:
        try:
            sub_item = sub_item[p]
        except KeyError:
            return False
    return True


@pyffi.interface(name="wcaml_winset")
def wcaml_win_set(attr: str, value: Any):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    nested_set(window, attr, value)


@pyffi.interface(name="wcaml_winget")
def wcaml_win_get(attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    return nested_get(window, attr)


@pyffi.interface(name="wcaml_docset")
def wcaml_doc_set(attr: str, value: Any):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    nested_set(document, attr, value)


@pyffi.interface(name="wcaml_docget")
def wcaml_doc_get(attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    return nested_get(document, attr)


@pyffi.interface(name="wcaml_set")
def wcaml_set(el, attr: str, value: Any):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    nested_set(el, attr, value)


@pyffi.interface(name="wcaml_get")
def wcaml_get(el, attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    return nested_get(el, attr)


@pyffi.interface(name="wcaml_set_attr")
def wcaml_set_attr(el, attr: str, value: Any):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    nested_set(el.attrs, attr, value)


@pyffi.interface(name="wcaml_get_attr")
def wcaml_get_attr(el, attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    return nested_get(el.attrs, attr)


@pyffi.interface(name="wcaml_del_attr")
def wcaml_del_attr(el, attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    del el.attrs[attr]


@pyffi.interface(name="wcaml_has_attr")
def wcaml_has_attr(el, attr: str):
    if not isinstance(attr, str):
        raise TypeError(f"invalid type {type(attr)} for argument attr: expected string")
    return nested_exists(el, attr)


@pyffi.interface(name="wcaml_get_attrs")
def wcaml_get_attrs(el):
    return el.attrs


@pyffi.interface(name="wcaml_remove")
def wcaml_remove(el):
    el.remove()


@pyffi.interface(name="wcaml_get_children")
def wcaml_get_children(el):
    return list(iter(el))


@pyffi.interface(name="wcaml_request")
def wcaml_request(method: str, *args):
    if len(args) == 0:  # allow currying method
        return lambda *a: wcaml_request(method, *a)
    default_values = [
        None,
        None,
        True,
        {},
        False,
        "text/plain",
        {},
        None,
        lambda: None,
        False,
    ]
    if len(args) > len(default_values):
        raise RuntimeError(
            f"too many arguments: expected at most {len(default_values)} ({len(default_values) + 1} if you count method parameter)"
        )
    if len(args) < 2:
        raise RuntimeError(
            f"too few arguments: the first 3 arguments (method, url, callback) are required (got only {len(args) + 1} arguments)"
        )
    for i, arg in enumerate(args):
        default_values[i] = arg
    (
        url,
        callback,
        run_async,
        data,
        send_as_form,
        mimetype,
        headers,
        timeout,
        timeout_callback,
        with_credentials,
    ) = default_values
    # make request using standard web api interface provided by brython
    req = ajax.Ajax()
    req.bind("complete", callback)
    req.open(method, url, run_async)
    for k, v in headers.items():
        req.set_header(k, v)
    if timeout is not None:
        req.set_timeout(timeout, timeout_callback)
    req.withCredentials = with_credentials
    req.mimeType = mimetype
    if send_as_form:
        form = ajax.form_data()
        if isinstance(data, dict):
            for k, v in data.items():
                form.append(k, v)
        else:
            form.append("data", data)
        data = form
    req.send(data)


@pyffi.interface(name="wcaml_get_element_by_id")
def wcaml_get_element_by_id(el_id: str):
    return document.getElementById(el_id)


@pyffi.interface(name="wcaml_query_selector_all")
def wcaml_query_selector_all(selector: str):
    return document.select(selector)


@pyffi.interface(name="wcaml_query_selector")
def wcaml_query_selector(selector: str):
    return document.select_one(selector)


@pyffi.interface(name="wcaml_create_element")
def wcaml_create_element(tag: str):
    return document.createElement(tag)


@pyffi.interface(name="wcaml_create_text_node")
def wcaml_create_text_node(content: str):
    return document.createTextNode(content)


@pyffi.interface(name="wcaml_append_child")
def wcaml_append_child(el, child):
    return el.appendChild(child)


@pyffi.interface(name="wcaml_head_append_child")
def wcaml_head_append_child(child):
    return document.head.appendChild(child)


@pyffi.interface(name="wcaml_body_append_child")
def wcaml_body_append_child(child):
    return document.body.appendChild(child)


@pyffi.interface(name="wcaml_doc_append_child")
def wcaml_doc_append_child(child):
    return document.appendChild(child)


@pyffi.interface(name="wcaml_alert")
def wcaml_alert(message):
    alert(message)


@pyffi.interface(name="wcaml_bind")
def wcaml_bind(el, event: str, callback):
    if not isinstance(event, str):
        raise TypeError(f"invalid type for event: expected string, got {type(event)}")
    el.bind(event, callback)


@pyffi.interface(name="wcaml_unbind")
def wcaml_unbind(el, event: str, callback):
    if not isinstance(event, str):
        raise TypeError(f"invalid type for event: expected string, got {type(event)}")
    el.unbind(event, callback)


@pyffi.interface(name="wcaml_events")
def wcaml_events(el, event: str):
    if not isinstance(event, str):
        raise TypeError(f"invalid type for event: expected string, got {type(event)}")
    return el.events(event)


@pyffi.interface(name="wcaml_prevent_default")
def wcaml_prevent_default(ev):
    ev.preventDefault()


@pyffi.interface(name="wcaml_stop_propagation")
def wcaml_stop_propagation(ev):
    ev.stopPropagation()


@pyffi.interface(name="wcaml_fire_event")
def wcaml_fire_event_on_el(el, ev):
    el.dispatchEvent(ev)


@pyffi.interface(name="wcaml_get_text")
def wcaml_get_text(el):
    return el.text


@pyffi.interface(name="wcaml_get_html")
def wcaml_get_html(el):
    return el.html


@pyffi.interface(name="wcaml_set_timeout")
def wcaml_set_timeout(func, ms):
    return timer.set_timeout(wrap_argless_lcaml_func(func), ms)


@pyffi.interface(name="wcaml_clear_timeout")
def wcaml_clear_timeout(timer_id):
    timer.clear_timeout(timer_id)


@pyffi.interface(name="wcaml_set_interval")
def wcaml_set_interval(func, ms):
    return timer.set_interval(wrap_argless_lcaml_func(func), ms)


@pyffi.interface(name="wcaml_clear_interval")
def wcaml_clear_interval(timer_id):
    timer.clear_interval(timer_id)


@pyffi.interface(name="wcaml_parse_from_string")
def wcaml_parse_from_string(content, doctype):
    return window.lcamlContext.parseFromString(content, doctype)


@pyffi.interface(name="wcaml_run_lcaml_script")
def wcaml_run_lcaml_script(script_el):
    window.runLcaml(script_el)


@pyffi.pymodule
def module(context):
    return {
        "wcaml": {
            "js_window": window,
            "js_document": document,
            "run_lcaml_script": wcaml_run_lcaml_script,
            "set": wcaml_set,
            "get": wcaml_get,
            "win_set": wcaml_win_set,
            "win_get": wcaml_win_get,
            "doc_set": wcaml_doc_set,
            "doc_get": wcaml_doc_get,
            "request": wcaml_request,
            "get_element_by_id": wcaml_get_element_by_id,
            "query_selector_all": wcaml_query_selector_all,
            "query_selector": wcaml_query_selector,
            "create_element": wcaml_create_element,
            "create_text_node": wcaml_create_text_node,
            "append_child": wcaml_append_child,
            "head_append_child": wcaml_head_append_child,
            "body_append_child": wcaml_body_append_child,
            "doc_append_child": wcaml_doc_append_child,
            "alert": wcaml_alert,
            "bind": wcaml_bind,
            "unbind": wcaml_unbind,
            "events": wcaml_events,
            "prevent_default": wcaml_prevent_default,
            "stop_propagation": wcaml_stop_propagation,
            "fire_event_on_el": wcaml_fire_event_on_el,
            "get_text": wcaml_get_text,
            "get_html": wcaml_get_html,
            "set_attr": wcaml_set_attr,
            "get_attr": wcaml_get_attr,
            "get_attrs": wcaml_get_attrs,
            "del_attr": wcaml_del_attr,
            "has_attr": wcaml_has_attr,
            "remove": wcaml_remove,
            "set_timeout": wcaml_set_timeout,
            "clear_timeout": wcaml_clear_timeout,
            "set_interval": wcaml_set_interval,
            "clear_interval": wcaml_clear_interval,
            "parse_from_string": wcaml_parse_from_string,
        }
    }
