from django.utils import timezone
from django.db import models
from django.shortcuts import get_object_or_404
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import lil_matrix

class books(models.Model):
    authorname=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    cover_page=models.FileField(upload_to='coverpages')
    file=models.FileField(upload_to='pdf')
    rating=models.IntegerField(default=0)
    hitrate=models.IntegerField(default=0)
    onestar=models.IntegerField(default=0)
    twostar=models.IntegerField(default=0)
    threestar=models.IntegerField(default=0)
    fourstar=models.IntegerField(default=0)
    fivestar=models.IntegerField(default=0)
    avgrating=models.FloatField(default=0.0,max_length=3)
    oneper=models.IntegerField(default=0)
    twoper=models.IntegerField(default=0)
    threeper=models.IntegerField(default=0)
    fourper=models.IntegerField(default=0)
    fiveper=models.IntegerField(default=0)
    readrate=models.IntegerField(default=0)
    



    def __str__(self):
        return f"{self.authorname} {self.email} {self.title}"
    
    def delete(self,*args,**kwargs):
        self.file.delete()
        self.cover_page.delete()
        super().delete(*args,**kwargs)


# Create your models here.

class readrate(models.Model):
    title=models.CharField(max_length=254)
    readrate=models.IntegerField()
    genre=models.CharField(max_length=254)
    date_time=models.DateTimeField(default=timezone.now)

class cart(models.Model):
    title=models.CharField(max_length=254)
    price=models.IntegerField()
    genre=models.CharField(max_length=254)
    quant=models.IntegerField()
    totalpayable=models.IntegerField()
    

class recom(models.Model):
    name=models.CharField(max_length=254)
    bookname=models.CharField(max_length=254)
    rating=models.IntegerField(default=0)
    avgrating=models.FloatField(default=0.0,max_length=3)





class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.name} - {self.book.title}: {self.rating}'


class BookRecommender:
    def __init__(self, ratings):
        self.ratings = ratings
        self.model = None

    def train_model(self):
        user_ids = self.ratings.values_list('user_id', flat=True).distinct()
        book_ids = self.ratings.values_list('book_id', flat=True).distinct()

        rating_matrix = lil_matrix((len(user_ids), len(book_ids)))
        user_id_to_index = {}
        book_id_to_index = {}
        for i, user_id in enumerate(user_ids):
            user_id_to_index[user_id] = i
        for i, book_id in enumerate(book_ids):
            book_id_to_index[book_id] = i

        for rating in self.ratings:
            user_index = user_id_to_index[rating.user_id]
            book_index = book_id_to_index[rating.book_id]
            rating_matrix[user_index, book_index] = rating.rating

        svd = TruncatedSVD(n_components=100)
        reduced_matrix = svd.fit_transform(rating_matrix)

        self.model = svd

    def get_recommendations(self, user_id, num_recommendations=5):
        user_ratings = Rating.objects.filter(user_id=user_id)

        book_ids = [rating.book_id for rating in user_ratings]

        other_ratings = Rating.objects.exclude(user_id=user_id)

        book_features = other_ratings.values('book_id', 'rating').order_by('book_id', 'user_id')
        book_features = book_features.pivot(index='book_id', columns='user_id', values='rating').fillna(0)
        similarity_matrix = cosine_similarity(book_features)

        user_ratings_dict = {rating.book_id: rating.rating for rating in user_ratings}
        recommendations = []
        for book_id in range(len(similarity_matrix)):
            if book_id not in book_ids:
                similarity_scores = similarity_matrix[book_id]
                weighted_sum = sum(similarity_scores * [user_ratings_dict.get(i, 0) for i in range(len(similarity_scores))])
                recommendations.append((book_id, weighted_sum))

        recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:num_recommendations]

        recommended_books = []
        for book_id, _ in recommendations:
            book = get_object_or_404(Book, id=book_id)
            recommended_books.append(book)

        return recommended_books

    
