from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import books,readrate
from django.urls import reverse
from django.http import FileResponse



# Create your views here.
def texteditor(request):
    template =loader.get_template('index.html')
    return HttpResponse(template.render())

def upload(request):
    template =loader.get_template('upload_books.html')
    return HttpResponse(template.render({},request))



def addrecord(request):
    a= request.POST['name'].title()
    b= request.POST['email'].lower()
    c= request.POST['title'].title()
    d= request.POST['genre'].title()
    
    record = books(authorname=a, email=b,title=c,genre=d,cover_page=request.FILES['cover'],file=request.FILES['pdf'])
    record.save()
    

    return HttpResponseRedirect(reverse('submission'))

def show(request):
    template =loader.get_template('show.html')
    records=books.objects.all().values()
    context={
        'records':records,
        

    }
    return HttpResponse(template.render(context,request))

def search(request):
    if request.method=='GET':
        query=request.GET.get('q')
        query=query.title()
        submitbutton=request.GET.get('submit')
        records=books.objects.all().filter(
                genre=query
            )
        if records.count()==0:
                records=books.objects.all().filter(
                    title=query
               )
        context={
            'records':records,
            'submitbutton':submitbutton,
          
        }
        return render(request,'show.html',context)
    
def submission(request):
     template =loader.get_template('submission.html')
     return HttpResponse(template.render({},request))




## Manupulation By Pratham
def rate(request):
     rating=request.GET.get('r')
     gettitle=request.GET.get('title')
     record1=books.objects.get(title=gettitle)
     totalhits=record1.hitrate
     record1.hitrate=totalhits+1
     ar=0.0

     # calculating % of rating
     one=record1.onestar
     two=record1.twostar
     three=record1.threestar
     four=record1.fourstar
     five=record1.fivestar
     match int(rating):
          case 1:
               record1.onestar=one+1
               record1.oneper=((one+1)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               ar=((one+1)*1+two*2+three*3+four*4+five*5)/((totalhits+1))
               
               
               

          case 2:
               record1.twostar=two+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two+1)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               ar=(one*1+(two+1)*2+three*3+four*4+five*5)/((totalhits+1))
               

          case 3:
               record1.threestar=three+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three+1)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               ar=(one*1+two*2+(three+1)*3+four*4+five*5)/((totalhits+1))
               

          case 4:
               record1.fourstar=four+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four+1)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               ar=(one*1+two*2+three*3+(four+1)*4+five*5)/((totalhits+1))
               

          case 5:
               record1.fivestar=five+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five+1)*100)/(totalhits+1)
               ar=(one*1+two*2+three*3+four*4+(five+1)*5)/((totalhits+1))
               
     record1.avgrating=round(ar,1)    
     request.session['title'] =gettitle        
     record1.save()




     print("here is rating",rating,gettitle)
     return redirect('/bookscollection/')


def reading(request):
    rating=request.GET.get('f')
    gettitle=request.GET.get('title')
    record1=books.objects.get(title=gettitle)
    readrating=record1.readrate
    readtitle= request.session.get('readtitle', None)
    if(readtitle==gettitle):
          print(gettitle ,"already read")
    else:
          record1.readrate=readrating+1
          record1.save()
          request.session['readtitle'] =gettitle
         
   
    x='/media/'+rating
    print(gettitle)

    return redirect(x)





## Pratham


from .models import User, Book, Rating, BookRecommender

def recommend_books(request, user_id):
    # Retrieve the user based on the user_id
    user = User.objects.get(id=user_id)

    # Create an instance of BookRecommender
    recommender = BookRecommender(Rating.objects.all())

    # Train the recommendation model
    recommender.train_model()

    # Get recommended books for the user
    recommended_books = recommender.get_recommendations(user_id)

    # Pass the recommended books to the template
    context = {
        'user': user,
        'recommended_books': recommended_books
    }

    return render(request, 'recommendation.html', context)



## lord vishnu help

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(request):
# Step 1: Data Collection
# Assuming you have a dataset with columns: 'title', 'author', 'genre', 'description'

# Step 2: Data Preprocessing
# Assuming your dataset is in a CSV file named 'books.csv'
    data = pd.read_csv('static\Book1.csv')
    print(data.head())
    print("sdjfnia",data['genre'][0][1])
    genredata=data['genre'][0]

    for x in genredata:
        print("genredata",x)
# Step 3: Feature Engineering
# Creating a feature vector by combining relevant features
    data['features'] = data['title'] + ' ' + data['author'] + ' ' + data['genre'] + ' ' + data['description']

# Step 4: Model Training
# Vectorize the feature text using TF-IDF
    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(data['features'])
    print(feature_matrix)

# Compute the cosine similarity between feature vectors
    similarity_matrix = cosine_similarity(feature_matrix)
    print("sjdfhai",similarity_matrix)
# Step 5: Generating Recommendations
# def get_recommendations():
    num_recommendations=3
    book_title = "The Hobbit"
    book_index = data[data['title'] == book_title].index[0]  # Get index of the book

    # Get similarity scores for the book
    book_similarities = similarity_matrix[book_index]

    # Get top similar books based on similarity scores
    top_indices = book_similarities.argsort()[::-1][1:num_recommendations+1]
    top_books = data.iloc[top_indices]['title'].values
    for book in top_books:
        print("hello therr",book)
    # record1=books.objects.values('authorname','title')
    # record2=books.objects.values_list('authorname')
    # print(record1)
    # print(record2)
    # features1 = [entry.authorname for entry in record1]   
    # print(features1) 
    

# Step 6: Using the Recommendation System
# book_title = "The Catcher in the Rye"
# recommendations = get_recommendations(book_title)
# print(f"Recommendations for '{book_title}':")
# for book in recommendations:
#     print(book)


# import csv
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# csv_file_path = os.path.join(BASE_DIR, 'static', 'Book1.csv')

# with open(csv_file_path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow('hi','hi','hi','hi')

# import csv
# import os

# def insert_data_to_csv(request):
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     csv_file_path = os.path.join(BASE_DIR, 'static', 'Book1.csv')

#     with open(csv_file_path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['hill','hill','hi','hi'])



#     csvfile.close()

import csv
import os

def insert_data_to_csv(data_list):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(BASE_DIR, 'static', 'Book1.csv')

    # Check if the CSV file already exists
    file_exists = os.path.isfile(csv_file_path)

    with open(csv_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row if the file is newly created
        if not file_exists:
            header = ['title', 'author', 'genre','description']  # Replace with your header column names
            writer.writerow(header)

        writer.writerow(['hill','hill','hi','hi'])

    csvfile.close()

   



     
