from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("handle-text/", views.handle_text, name="handle_text"),
    path("new_chat/", views.new_chat, name="new_chat"),
    path("chats/", views.chats, name="chats"),
    path("userpage/", views.userpage, name="userpage"),
    path("userprofile/", views.userprofile, name="userprofile"),
    path("chats/copy_message/", views.copy_message, name="copy_message"),
    path("get_instructions/", views.get_instructions, name="get_instructions"),
    path("delete/", views.delete_chat, name="delete_chat"),
    path("edit_message/", views.edit_message, name="edit_message"),
    path("chats/load_messages/", views.load_messages, name="load_messages"),
    path("rename-chat/", views.rename_chat, name="rename_chat"),
    path("create_character/", views.create_character, name="create_character"),
    path("user_characters/", views.user_characters, name="user_characters"),
    path("create_conversation/", views.create_conversation, name="create_conversation"),
    path("delete_character/", views.delete_character, name="delete_character"),
    path("browse_characters/", views.browse_characters, name="browse_characters"),
    path("search_results/", views.search_results, name="search_results"),
    path("public_status/", views.public_status, name="public_status"),
    path("test/", views.test, name="test"),
]