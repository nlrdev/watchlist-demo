from .core import (
    HttpResponse,
    is_ajax,
    render_to_string,
    get_object_or_404,
    bleach,
    json,
    is_post,
    is_get,
    render,
    log,
    render,
    push_msg,
    to_list,
)
from .forms import CryptoModelForm

def app(request, page="dashboard", function="index"):
    _page = bleach.clean(page)
    _function = bleach.clean(function)
    current_page = bleach.clean(request.path.split("/")[-2])

    if request.POST.get("action"):
        _action = bleach.clean(request.POST.get("action"))
    else:
        _action = _page

    context = {
        "current_page": current_page if current_page != "" else "dashboard",
        "page": _page,
        "function": _function,
        "template": f"app/{_page}/index.html",
        "action": _action,
        "javascript": [
            f"js/{_page}.js",
        ],
    }

    context_factory = {
        "dashboard": dashboard_context,
    }

    try:
        _context = context_factory[_page](request)
        context |= _context if _context else no_context()
    except Exception as e:
        log(e)

    if is_post(request):
        try:
            return HttpResponse(json.dumps(context), content_type="application/json")
        except Exception as e:
            log(e)
            return HttpResponse(
                json.dumps({"alert": "Failed to proccess the request!"}),
                content_type="application/json",
            )

    if is_get(request):
        try:
            return render(request, "index.html", context)
        except Exception as e:
            log(e)
            push_msg(request, "Failed to find the page or resource!", "alert-warning")
            return render(request, "index.html", {"template": "src/error.html"})


def dashboard_context(request):
    if is_get(request):
        if "crypto_watchlist" in request.session:
            data = to_list(request.session["crypto_watchlist"])
        else:
            data = {}
        return{
            "crypto_form" : CryptoModelForm,
            "crypto_watchlist" :  data,
        }
        
    if is_ajax(request):      
        form = CryptoModelForm(request.POST)
        if form.is_valid():
            crypto = form.cleaned_data['name']
            log(crypto)
            if "crypto_watchlist" in request.session:
                _data = request.session["crypto_watchlist"] + f", {crypto}"
                request.session["crypto_watchlist"] = _data
            else:
                request.session["crypto_watchlist"] = f"{crypto}"
                           
            ctx = {
                "crypto_watchlist" :  to_list(request.session["crypto_watchlist"]),
            }
            return {
                "html": render_to_string(
                    "app/dashboard/items.html",
                    ctx,
                    request,
                ),
            }


def no_context(*args, **kwargs):
    return {}