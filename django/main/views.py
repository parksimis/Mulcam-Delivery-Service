from django.shortcuts import render
import userfunc

# Create your views here.
def index(request):
    result_list = userfunc.select_main_table()

    main_line_lbl, main_line_val = userfunc.main_line_data()
    main_pie_lbl, main_pie_val = userfunc.main_pie_data()


    context = {
        'result_list': result_list,
        'main_line_lbl': main_line_lbl,
        'main_line_val': main_line_val,
        'main_pie_lbl': main_pie_lbl,
        'main_pie_val': main_pie_val,
    }
    return render(request, 'main/index.html', context)


def chicken_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('chicken', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('chicken', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/chicken_result.html', context)


def ilsik_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('ilsik', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('ilsik', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/ilsik_result.html', context)

def bunsik_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('bunsik', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('bunsik', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/bunsik_result.html', context)

def yasik_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('yasik', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('yasik', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/yasik_result.html', context)


def jokbal_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('jokbal', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('jokbal', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/jokbal_result.html', context)


def jungsik_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('jungsik', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('jungsik', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/jungsik_result.html', context)


def jimtang_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('jimtang', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('jimtang', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/jimtang_result.html', context)


def cafe_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('cafe', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('cafe', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/cafe_result.html', context)



def fastfood_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('fastfood', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('fastfood', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/fastfood_result.html', context)


def hansik_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('hansik', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('hansik', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/hansik_result.html', context)

def etc_result(request):

    sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val = userfunc.execute_all('etc', '일자별')
    sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val = userfunc.execute_all('etc', '시간대별')


    context = {
        'sl_daily_lbl': sl_daily_lbl,
        'sl_daily_val': sl_daily_val,
        'sl_hour_lbl': sl_hour_lbl,
        'sl_hour_val': sl_hour_val,
        'gg_daily_lbl': gg_daily_lbl,
        'gg_daily_val': gg_daily_val,
        'gg_hour_lbl': gg_hour_lbl,
        'gg_hour_val': gg_hour_val,
    }

    return render(request, 'main/etc_result.html', context)
