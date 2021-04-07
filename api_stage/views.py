from django.http.response import JsonResponse
# Add to upload files
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Importation of models and serializers
from api_stage.models import (Users, Posts, Comments)
from api_stage.serializers import (UserSerializer, PostSerializer, FileSerializer, CommentSerializer)


# Create your views here.

# ***************************************************#
# ********* Users Manage API ************************#
# ***************************************************#

@api_view(['GET', 'POST', 'DELETE'])
def manage_users(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'User successfully created',
            }
            return Response(response, status=status_code)
            # return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Users.objects.all().delete()
        return JsonResponse({'message': '{} users were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users_serializer = UserSerializer(user)
        return JsonResponse(users_serializer.data)

    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(user, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# ***************************************************#
# ********* Posts Manage API ************************#
# ***************************************************#

@api_view(['GET', 'POST', 'DELETE'])
def manage_posts(request):
    if request.method == 'GET':
        posts = Posts.objects.all()

        # keys = request.GET.get('mots_recherche', None)
        # if keys is not None:
        #     posts = posts.filter(keys__icontains=keys)

        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        posts_data = JSONParser().parse(request)
        mots = posts_data['mots_recherche']
        print(str(mots))
        # if mots:
        #     twitter_posts(mots)
        posts_serializer = PostSerializer(data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'Posts successfully created',
            }
            return Response(response, status=status_code)
            # return JsonResponse(posts_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Posts.objects.all().delete()
        return JsonResponse({'message': '{} posts were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    try:
        one_post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return JsonResponse({'message': 'The Posts does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts_serializer = PostSerializer(one_post)
        return JsonResponse(posts_serializer.data)

    elif request.method == 'PUT':
        posts_data = JSONParser().parse(request)
        posts_serializer = PostSerializer(one_post, data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse(posts_serializer.data)
        return JsonResponse(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        one_post.delete()
        return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# ***************************************************#
# ********* Files Manage API ************************#
# ***************************************************#
@api_view(['GET', 'POST', 'DELETE'])
def file_store(request):
    if request.method == 'POST':

        files_serializer = FileSerializer(data=request.data)

        if 'file_name' not in request.FILES or not files_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # Single File
            # handle_uploaded_file(request.FILES['file'])

            # Multiple Files
            files = request.FILES.getlist('file_name')
            print(files)
            for f in files:
                handle_uploaded_file(f)

            files_serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'File has been uploaded successfully',
            }
            return Response(response, status=status_code)


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# ***************************************************#
# ********* Login Party ************************#
# ***************************************************#
# # Get the JWT settings
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# ***************************************************#
# ********* Comments Manage API ************************#
# ***************************************************#

@api_view(['GET', 'POST', 'DELETE'])
def manage_comments(request):
    if request.method == 'GET':
        comments = Comments.objects.all()
        comments_serializer = CommentSerializer(comments, many=True)
        return JsonResponse(comments_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        comments_data = JSONParser().parse(request)
        comments_serializer = CommentSerializer(data=comments_data)
        if comments_serializer.is_valid():
            comments_serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'Comment successfully created',
            }
            return Response(response, status=status_code)
            # return JsonResponse(comments_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(comments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Comments.objects.all().delete()
        return JsonResponse({'message': '{} comments were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def comments_detail(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return JsonResponse({'message': 'The comment does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comments_serializer = CommentSerializer(comment)
        return JsonResponse(comments_serializer.data)

    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comments_serializer = CommentSerializer(comment, data=comment_data)
        if comments_serializer.is_valid():
            comments_serializer.save()
            return JsonResponse(comments_serializer.data)
        return JsonResponse(comments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return JsonResponse({'message': 'Comment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)