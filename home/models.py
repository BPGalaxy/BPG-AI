from django.db import models

class Message(models.Model):
    messageid = models.IntegerField(default=0)
    chatid = models.TextField(default="")
    accountid = models.TextField(default="AnonymousUser")
    senderuser = models.TextField(default='message ai')
    text = models.TextField("")

    def __str__(self):
        return self.text[:30]

class Status(models.Model):
    accountid = models.TextField(default="AnonymousUser")
    Generate_status = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_VIP = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    is_limit = models.BooleanField(default=False)
    currentchat = models.TextField(default="none")
    remaining_messages = models.IntegerField(default=100)
    user_profile = models.ImageField(blank=True, null=True, upload_to="user_profiles/")

    def __str__(self):
        return self.accountid

class Customization(models.Model):
    accountid = models.TextField(default="AnonymousUser")
    CustomInstructions = models.TextField(default="")
    Name = models.TextField(default="")
    Emoji = models.TextField(default="")
    Occupation = models.TextField(default="")
    Interests = models.TextField(default="")

    def __str__(self):
        return self.Name

class Chats(models.Model):
    chatid = models.TextField(default="")
    accountid = models.TextField(default="AnonymousUser")
    chatname = models.TextField(default="")
    avatar = models.TextField(default="")
    last_message = models.TextField(default="")
    is_deleted = models.BooleanField(default=False)
    AI_Prompt = models.TextField(default="", blank=True, null=True)
    AI_Name = models.TextField(default="", blank=True, null=True)
    summary = models.TextField(default="", blank=True, null=True)
    is_rp = models.BooleanField(default=True, blank=True, null=True)
    CustomInstructions = models.TextField(default="", blank=True, null=True)
    Name = models.TextField(default="", blank=True, null=True)
    Emoji = models.TextField(default="", blank=True, null=True)
    Occupation = models.TextField(default="", blank=True, null=True)
    Interests = models.TextField(default="", blank=True, null=True)
    CharacterID = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.accountid}_{self.chatname}"

class Characters(models.Model):
    accountid = models.TextField(default="AnonymousUser")
    Name = models.TextField(default="")
    ProfilePicture = models.ImageField(blank=True, null=True, upload_to="character_profiles/")
    avatar = models.TextField(default="")
    last_message = models.TextField(default="")
    Description = models.TextField(default="")
    Prompt = models.TextField(default="")
    OpeningLine = models.TextField(default="")
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Name

class Settings(models.Model):
    today = models.IntegerField(default=0)