from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from users.models import ForumUser as User

from .models import *

@login_required
def create_post(request):
    context = {}
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except KeyError:
        return render(request, 'posts/create_post.html', context)
    else:
        username = request.user.username
        user = User.objects.get(username=username)
        new_question = Question(title=title, description=description, user=user)
        new_question.save()
        for tag_name in tags.split(','):
            if(len(tag_name) == 0):
                continue
            tag_name = tag_name.strip()
            tag_res = Tag.objects.filter(name=tag_name)
            if (len(tag_res) == 0):
                new_tag = Tag(name=tag_name)
                new_tag.save()
            else:
                new_tag = tag_res[0]
            new_question_tag = QuestionTag(question=new_question, tag=new_tag)
            new_question_tag.save()
        return redirect("/all-posts") # TODO: redirect to post page


def post(request):
    context = {
        'title': 'Pergunta'
    }
    return render(request, 'posts/post.html', context)

def edit_post(request, post_id):
    question = get_object_or_404(Question, pk=post_id)
    
    question_tags = QuestionTag.objects.filter(question=post_id)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
        
    context = {
        'title': 'Editar pergunta',
        'question': question,
        'tags': tags
    }
    
    # Verificação de usuário
    user_id = request.user.id
    if(user_id != question.user.id):
        context['error_message'] = "Usuário atual não é o criador da pergunta"
        return redirect("/all-posts")
    
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except (KeyError):
        return render(request, 'posts/edit_post.html', context)
    else:
        question.title = title
        question.description = description
        question.save()
        
        QuestionTag.objects.filter(question=post_id).delete()
        
        for tag_name in tags.split(','):
            if(len(tag_name) == 0):
                continue
            print (tag_name)
            tag_name = tag_name.strip()
            tag_res = Tag.objects.filter(name=tag_name)
            if (len(tag_res) == 0):
                new_tag = Tag(name=tag_name)
                new_tag.save()
            else:
                new_tag = tag_res[0]
            new_question_tag = QuestionTag(question=question, tag=new_tag)
            new_question_tag.save()
        return redirect("/all-posts") # TODO: redirect to post page