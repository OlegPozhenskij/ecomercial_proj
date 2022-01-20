from .models import Category

def categories(request):
    return {
        # контекстный процессор, когда данные должены отображаться на всех страницах
        'categories': Category.objects.all()
    }