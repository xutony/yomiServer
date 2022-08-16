from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import YomiForm
from yomi import Kana_Table


def get_kana_s(pinyin):
    result = []
    for k in Kana_Table:
        if pinyin == k.pinyin:
            result.append(k.kanji + ' -- ' + k.kana_s)
    return result


# Create your views here.
def yomi(request):
    # use form template
    return render(request, 'yomi/index.html', {'form': YomiForm()})


def get_pinyin(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = YomiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pinyin = form.cleaned_data['pinyin']
            # redirect to a new URL:
            result = get_kana_s(pinyin)
            return render(request, 'yomi/results.html', {'result': result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = YomiForm()

    return render(request, 'yomi/index.html', {'form': form})
