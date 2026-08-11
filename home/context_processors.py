from home.models import Settings

def announcement(request):
    settings = Settings.objects.first()
    if not settings or not hasattr(request, "session") or request.path != "/":
        return {}

    ANNOUNCEMENT_VERSION = settings.ANNOUNCEMENT_VERSION
    ANNOUNCEMENT_TEXT = settings.ANNOUNCEMENT_TEXT
    
    seen = request.session.get("seen_announcement") == ANNOUNCEMENT_VERSION
    
    if not seen:
        request.session["seen_announcement"] = ANNOUNCEMENT_VERSION

    return {
        "show_announcement": not seen,
        "announcement_version": ANNOUNCEMENT_VERSION,
        "announcement_text": ANNOUNCEMENT_TEXT,
    }