from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Count 


def home(request):
    msg = request.GET.get('msg', '')
    posts = post.objects.annotate(
        likes_count=Count('like', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-id') # Optional: orders by newest first

    return render(request, 'home.html', {'posts': posts, 'msg': msg})

def about(request):
    return render(request, 'about.html')
def login(request):
    if request.method == 'POST':
        ue = request.POST['email']
        up = request.POST['password']
        user = userlogin.objects.filter(email=ue, password=up)

        if user:
            request.session['email'] = ue
            return redirect('home')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = userloginform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html')


def userlogout(request):
    logout(request)
    return redirect('home')


def update(request, id):
    msg=""
    if not request.session.get('email'):
        msg = "You must be logged in to update a post."
        return redirect('/?msg=' + msg)
    post_obj = post.objects.get(id=id)

    if request.method == 'POST':
        form = postform(request.POST,instance=post_obj)
        if form.is_valid():
            form.save()
            print("Updated Successfully")
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = postform(instance=post_obj)
            
    return render(request, 'update.html', {'form': form})

# views.py

def create_post(request):
    if request.method == 'POST':
        # 1. Get the current logged-in user's email from session
        user_email = request.session.get('email')
        
        # 2. Find the user object in the database
        user_obj = userlogin.objects.get(email=user_email)
        
        # 3. Save the form with the author
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) # Don't write to DB yet
            instance.author = user_obj         # Assign the author
            instance.save()                    # Now save
            return redirect('home')
            
    return render(request, 'create_post.html', {'form': postform()})

def delete(request, id):
   if not request.session.get('email'):
        msg = "You must be logged in to delete a post."
        return redirect('/?msg=' + msg)
   post_obj=post.objects.get(id=id)
   post_obj.delete()
   return redirect('home')

def detail_post(request, id):
    post_obj = post.objects.annotate(
        likes_count=Count('like', distinct=True)
    ).get(id=id)

    comments = Comment.objects.filter(post=post_obj)
    comments_count = comments.count()

    user_email = request.session.get('email')
    user = None
    if user_email:
        user = userlogin.objects.get(email=user_email)

    return render(request, 'detail.html', {
        'post': post_obj,
        'comments': comments,
        'comments_count': comments_count,
        'user': user
    })

def like_post(request, id):
    user_email = request.session.get('email')
    if not user_email:
        return redirect('/?msg=Login required')

    user = userlogin.objects.get(email=user_email)
    post_obj = post.objects.get(id=id)

    like = Like.objects.filter(user=user, post=post_obj)

    if like.exists():
        like.delete()
    else:
        Like.objects.create(user=user, post=post_obj)

    return redirect(request.META.get('HTTP_REFERER', 'home'))


def comment_post(request, id):
    user_email = request.session.get('email')
    if not user_email:
        return redirect('/?msg=Login required')

    user = userlogin.objects.get(email=user_email)
    post_obj = post.objects.get(id=id)

    Comment.objects.create(
        user=user,
        post=post_obj,
        text=request.POST['comment']
    )

    return redirect('detail_post', id=id)


def follow_author(request, id):
    user_email = request.session.get('email')
    if not user_email:
        return redirect('/?msg=Login required')

    follower = userlogin.objects.get(email=user_email)
    following = userlogin.objects.get(id=id)

    already = Follow.objects.filter(follower=follower, following=following)

    if already.exists():
        already.delete()
    else:
        Follow.objects.create(follower=follower, following=following)

    return redirect('detail_post', id=id)
