from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse as h
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Question, Choice
from django.views import generic


# Create your views here.

def home(request):
    # return h("<h1>this is index</h1>")
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # print(latest_question_list)
    # list_ = {'latest_question_list': latest_question_list, 'j': "jimmy"}
    return render(request, 'src/index.html',)

def index(request):
    # return h("<h1>this is index</h1>")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    list_ = {'latest_question_list': latest_question_list, 'j': "jimmy"}
    return render(request, 'polls/index.html', list_)


def detail(request, pk):  # pk是url传递过来的参数
    print(pk)
    question = get_object_or_404(Question, pk=pk)  # 快捷方式get_object_or_404（表,查询字）
    print('primkey ='+pk+'/res='+str(question))
    return render(request, 'polls/detail.html', {'question': question})


def results(request, pk):
    # response = "You're looking at the results of question %s."
    # return h(response % question_id)
    print(pk)
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return h("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    # print(request.POST["choice"])
    # post_id = request.POST['choice']  # post传递的参数
    # print('request.post'+request.POST['choice'])  # 该Question 外键对应choice
    try:
        # print(request.POST['choice'])
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'err': 'vote',
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('ns_polls:results', args=(p.id,)))
        # 成功处理POST数据后总是返回一个HttpResponseRedirect
        # reverse()函数是为了不用硬解码url地址 返回字符串

# class IndexView(generic.ListView):  # 继承通用视图的“显示一个对象列表‘
#     template_name = 'polls/index.html'  # 要返回的模板
#     context_object_name = 'latest_question_list'  # 执行返回方法后得到的数据
#
#     def get_queryset(self):  # 返回数据的方法
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):  # 继承通用视图的 ’显示一个特定类型对象的详细信息页面‘
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'



