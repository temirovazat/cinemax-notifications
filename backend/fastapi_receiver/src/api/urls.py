from fastapi.routing import APIRoute

from api.v1 import views

routes = [
    APIRoute(
        path='/new_user',
        methods=['POST'],
        summary='Publish a new user',
        endpoint=views.publish_new_user,
    ),
    APIRoute(
        path='/like_comment',
        methods=['POST'],
        summary='Publish a like to a comment',
        endpoint=views.publish_like_comment,
    ),
    APIRoute(
        path='/notification',
        methods=['POST'],
        summary='Publish a notification to users',
        endpoint=views.publish_notification,
    ),
]
