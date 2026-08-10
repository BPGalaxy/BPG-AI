from django.conf import settings

def announcement(request):
    if not hasattr(request, "session"):
        return {}

    seen = request.session.get("seen_announcement") == settings.ANNOUNCEMENT_VERSION

    if not seen:
        request.session["seen_announcement"] = settings.ANNOUNCEMENT_VERSION

    return {
        "show_announcement": not seen,
        "announcement_version": settings.ANNOUNCEMENT_VERSION,
        "announcement_text": settings.ANNOUNCEMENT_TEXT,
    }