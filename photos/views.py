from django.shortcuts import render, redirect
from .models import Location, Category, Photo
# Create your views here.

def gallery(request):
    locations=request.GET.get('location')
    if locations == None :
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(location = locations)


    categories = Category.objects.all()
    location = Location.objects.all()
    # photos = Photo.objects.all()
    context = {'categories':categories, 'location':location, 'photos':photos}

    return render(request, 'photos/gallery.html',context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()
    if request.method =='POST':
        data = request.POST
        image = request.FILES.get('image')
        
        # print('data:',data)

    
        if data['category']!='none':
            category = Category.objects.get(id=data['category'])

        elif data['category'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category= None

        photo = Photo.objects.create(
            category = category,
            location = data['location'],
            description = data['description'],
            image = image,
        )

        return redirect('gallery')

    context = {'categories':categories}
    return render(request, 'photos/add.html', context)


def search_category(request):
    categorys = request.GET.get('category')

    print('categorys:', categorys)

    photos = Photo.objects.filter(category__name=categorys)
    return render(request, 'photos/search.html', {'photos': photos})