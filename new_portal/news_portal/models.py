from django.contrib.auth.models import User
from django.db import models


# from django.db.models import Sum, SmallIntegerField
# import datetime


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0, verbose_name='authorRating')

    def update_rating(self):
        post_rating = Post.objects.filter(PostAuthor=self).values('postRating')
        post_rating = sum(p['postRating'] for p in post_rating) * 3

        comment_rating = Comment.objects.filter(commentUser=self).values('comRating')
        comment_rating = sum(c['comRating'] for c in comment_rating)

        authorRating = post_rating + comment_rating
        self.authorRating = authorRating
        self.save()

        return f'{self.authorRating}'


class Category(models.Model):
    categoryname = models.CharField('Категория', max_length=64, unique=True)


class Post(models.Model):
    PostAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORIES = [
        ('NW', 'Новость'),
        ('AR', 'Статья')
    ]
    categoryType = models.CharField(max_length=2, choices=CATEGORIES)
    pubData = models.DateTimeField('дата и время добавления новости', auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='postCategory')
    postTitle = models.CharField('название публикации', max_length=255)
    postText = models.TextField('текст публикации')
    postRating = models.SmallIntegerField('рейтинг публикации', default=0)

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        return f'{self.postText[:124]}...'

    def __str__(self):
        return f'{self.postTitle} {self.postText}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commentUser = models.ForeignKey(Author, on_delete=models.CASCADE)
    commentText = models.CharField('текст комментария', max_length=255)
    dataPub = models.DateTimeField('время и дата комментария', auto_now_add=True)
    comRating = models.SmallIntegerField('рейтинг комментария', default=0)

    def __str__(self):
        return self.commentUser.username

    def like(self):
        self.comRating += 1
        self.save()

    def dislike(self):
        self.comRating -= 1
        self.save()

